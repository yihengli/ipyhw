import os
import click
import re
import nbformat
from nbconvert.exporters import MarkdownExporter
from nbconvert.writers import FilesWriter


FOLDER = os.path.dirname(os.path.realpath(__file__))
HIDE_TEMPLATE = os.path.join(FOLDER, 'assets', 'hide.tpl')


class MdFormatter():

    def clear(self, body):
        body = self._kill_multi_lines(body)
        body = self._table_border(body)
        body = self._table_styles(body)
        return body

    @staticmethod
    def _kill_multi_lines(body):
        return re.sub('(\\n){3,}', '\\n\\n', body)

    @staticmethod
    def _table_border(body):
        return re.sub(r'border="1"', r'border="0"', body)

    @staticmethod
    def _table_styles(body):
        styles = """
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>"""
        return re.sub(styles, '', body)


class PostProcesser():

    @staticmethod
    def res_path(res, out):
        for k in [k for k in res['outputs'].keys()]:
            res['outputs'][out + k] = res['outputs'].pop(k)
        return res


@click.command()
@click.option('-i', '--input', help='The input ipython notebook file')
@click.option('-o', '--output', default='', help='The output folder')
@click.option('-n', '--name', default='Homework', help='Output file name')
def main(input, output, name):
    exporter = MarkdownExporter(template_file=HIDE_TEMPLATE)
    writer = FilesWriter()

    with open(input, 'rb') as f:
        nb = nbformat.read(f, as_version=4)

    (body, res) = exporter.from_notebook_node(nb)
    writer.write(MdFormatter().clear(body),
                 PostProcesser().res_path(res, output),
                 notebook_name=output+name)


if __name__ == "__main__":
    main()
