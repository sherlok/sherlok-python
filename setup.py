from setuptools import setup, find_packages  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding

with open('README.rst') as f:
    readme = f.read()

setup(
    name='sherlok',
    version='0.1.3',
    description='A Python client for Sherlok',
    long_description=readme,
    url='https://github.com/renaud/sherlok-python',
    author='Renaud Richardet',
    author_email='renaud@apache.org',
    license='Apache License (2.0)',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3',
        #'Programming Language :: Python :: 3.2',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],
    keywords='distributed RESTful text mining',
    py_modules=['sherlok']
)
