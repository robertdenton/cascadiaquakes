try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'Cascadia Quakes',
    'description': 'Alerts for earthquakes near Cascadia Subduction Zone',
    'author': 'Rob Denton',
    'url': 'https://github.com/robertdenton/cascadia-quakes/',
    'download_url': 'https://github.com/robertdenton/cascadia-quakes',
    'author_email': 'rob@robertrdenton.com',
    'version': '0.1',
    'install_requires': ['pytest','requests'],
    'packages': ['alert'],
    'scripts': []
}

setup(**config)

