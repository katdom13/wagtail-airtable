#!/usr/bin/env python

from setuptools import setup, find_packages

install_requires = [
    "wagtail>=2.15",
    "airtable-python-wrapper>=0.13.0",
    "djangorestframework>=3.11.0,<3.15.0",
]

setup(
    name='wagtail-airtable',
    version='0.2.2',
    description="Sync data between Wagtail and Airtable",
    author='Kalob Taulien',
    author_email='kalob.taulien@torchbox.com',
    url='https://github.com/wagtail/wagtail-airtable',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    license='BSD',
    long_description="An extension for Wagtail allowing content to be transferred between Airtable sheets and your Wagtail/Django models",
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Framework :: Django :: 3',
        'Framework :: Django :: 4',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Framework :: Wagtail :: 3',
        'Framework :: Wagtail :: 4',
    ],
    install_requires=install_requires,
)
