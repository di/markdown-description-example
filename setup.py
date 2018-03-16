from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    author='Dustin Ingram',
    author_email='di@di.codes',
    description='A PyPI package with a Markdown README',
    long_description=long_description,
    long_description_content_type='text/markdown',  # This is important!
    name='markdown-description-example',
    url='http://github.com/di/markdown-description-example',
    version='0.0.1',
)
