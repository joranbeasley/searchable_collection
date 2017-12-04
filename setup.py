from setuptools import setup
from searchable_collection import __version__
setup(
    name='searchable_collection',
    version=__version__,
    packages=['searchable_collection'],
    url='http://searchablecollection.readthedocs.io/en/latest/',
    license='MIT',
    author='Joran Beasley',
    author_email='joranbeasley@gmail.com',
    repo='https://github.com/joranbeasley/searchable_collection',
    description='A searchable list implementation, written entirely in python.',
    classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Software Development :: Bug Tracking',
          'Topic :: Software Development :: Libraries',
          'Topic :: Database',
          'Topic :: Utilities',
          ]
)
