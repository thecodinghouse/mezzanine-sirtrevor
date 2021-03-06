#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

setup(
    name='mezzanine-sirtrevor',
    version= '0.1.0',
    packages=['sirtrevor'],
    include_package_data=True,
    license='MIT License',
	zip_safe=False,
    description='Sir Trevor editor for Mezzanine',
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/thecodinghouse/mezzanine-sirtrevor',
	download_url = 'https://github.com/thecodinghouse/mezzanine-sirtrevor/tarball/v0.1.0',
    author='Abhinav Sohani',
    author_email='thecodinghouse12@gmail.com',
    install_requires=['markdown2', 'django-appconf', 'django', 'six'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
