import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages

CURDIR = dirname(abspath(__file__))

with open(join(CURDIR, 'requirements.txt'), encoding='utf-8') as f:
    REQUIREMENTS = f.read().splitlines()

with open(join(CURDIR, 'src', 'Xray', '__init__.py')) as f:
    VERSION = re.search('\n__version__ = "(.*)"', f.read()).group(1)

setup(
    name = 'robotframework-xray',
    version = VERSION,
    author = 'Cleverson Sampaio',
    author_email = 'cleverson@sampaio.dev.br',
    url = 'https://github.com/kriffx/robotframework-xray',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = REQUIREMENTS,
)