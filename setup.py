try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Alex Philip Gough',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'alexphilipgough@gmail.com.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)