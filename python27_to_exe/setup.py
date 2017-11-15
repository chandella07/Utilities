from distutils.core import setup
import py2exe

setup(
    windows=[{'script': 'scrap.py'}],
    options={
        'py2exe': 
        {
            'includes': ['lxml.etree', 'lxml._elementpath', 'csv', 'json', 'os', 'sys', 'requests', 'exceptions', 'time'],
        }
    }
)
