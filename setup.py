
from setuptools import setup, find_packages
from inventorytransfer.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='inventorytransfer',
    version=VERSION,
    description='App for transfering data between different inventory tools',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Gringosweb',
    author_email='contacto@gringosweb.com',
    url='https://github.com/johndoe/myapp/',
    license='unlicensed',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'inventorytransfer': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        inventorytransfer = inventorytransfer.main:main
    """,
)
