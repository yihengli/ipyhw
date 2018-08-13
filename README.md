## Introduction

The CLI will convert a ipynb to a standardized markdown file that can be
rendered further as PDF. The original purpose of this project is to make
homework submission easier.

## How to use

```bash
python ipyhw.py -i homework.ipynb
```

## Features

- By using `hide.tpl`, the code blocks will be hidden in default
- Duplicated empty rows will be removed in the final output file.

## TODO

- More flexible to handle different `tpl`
- Using `pandoc` to directly render markdown as pdf
- Generate a cover page using Python
- Handle more complicated structures and jupyter markdown differences.
