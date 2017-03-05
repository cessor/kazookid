# Thank you for helping me out, Jonathan
# http://jtushman.github.io/blog/2013/06/17/sharing-code-across-applications-with-python/
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Can we do more kazoo?',
    'author': 'Johannes Hofmeister',
    'url': 'https://github.com/cessor/kazoo',
    'download_url': 'https://github.com/cessor/kazoo',
    'author_email': '',
    'version': '1.0',
    'tests_require': ['nose'],
    'packages': ['kazoo'],
    'scripts': [],
    'name': 'kazoo'
}

setup(**config)
