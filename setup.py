from setuptools import setup, find_packages

setup(
    name='glitchlib',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pyserial', 'matplotlib'
    ],
    author='Thomas \'stacksmashing\' Roth',
    author_email='code@stacksmashing.net',
    description='A library to control Pico based glitchers.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GPLv3 License',
        'Operating System :: OS Independent',
    ],
)