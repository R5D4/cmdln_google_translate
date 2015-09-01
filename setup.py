try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Translate Lots of Files',
    'author': 'R5D4',
    'url': 'github when I upload it',
    'download_url': 'None',
    'author_email': 'None',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['gtrans'],
    'scripts': [],
    'name': 'gtrans'
}

setup(**config)
