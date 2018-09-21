from setuptools import setup, find_packages

setup(
    name='ipyhw',
    version='0.1.0',
    description='Convert your ipynb to the markdown format',
    author='Yiheng Li',
    packages=find_packages(),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python :: 3'
    ],
    install_requires=[
    ],
    entry_points={
        "console_scripts": ["ipyhw = ipyhw.ipyhw:main"]
    }
)
