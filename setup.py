# Thank you for helping me out, Jonathan
# http://jtushman.github.io/blog/2013/06/17/sharing-code-across-applications-with-python/
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A simple and friendly mocking framework. Can we do more kazoo?',
    'author': 'Johannes C. Hofmeister',
    'url': 'https://github.com/cessor/kazookid',
    'download_url': 'https://github.com/cessor/kazookid',
    'author_email': 'py_kazookid@spam.cessor.de',
    'version': '1.3.1',
    'tests_require': ['nose'],
    'packages': ['kazookid'],
    'scripts': [],
    'name': 'kazookid'
}

setup(**config)
