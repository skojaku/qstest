from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name='qstest',
    version='1.0.4',
    description='Python code for the (q,s)-test',
    long_description=long_description,
    url='https://github.com/skojaku/qstest.git',
    author='Sadamori Kojaku',
    author_email='sadamori.koujaku@bristol.ac.uk',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='network community significance test',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=['networkx>=2.0', 'scipy>=1.0', 'python-louvain==0.9', 'numpy', 'decorator'],
)
