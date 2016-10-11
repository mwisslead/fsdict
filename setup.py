from setuptools import setup

VERSION='0.2.0'

setup(
    name='fsdict',
    version=VERSION,
    description='Dictionary-like access to the file system',
    author='Michael Wisslead',
    author_email='michael.wisslead@gmail.com',
    url='https://github.com/mwisslead',
    packages=['fsdict'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ]
)
