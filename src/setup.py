try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import py2exe

config = {
    'description': 'Find the files by the pattern inside those files.',
    'author': 'Mukilan_E',
    'author_email': 'mukilan@5gindia.net',
    'version': '0.1',
    'install_requires': ['nose','py2exe'],
    'packages': ['findlog'],
    'scripts': ['findlog/findlog.py'],
    'name': 'findlog'

}

setup(**config)
setup(console=[r'findlog\findlog.py'])