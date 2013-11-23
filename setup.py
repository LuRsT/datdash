from setuptools import setup
from os.path import join as join_path
from os import walk


def files_in(package, directory):
    paths = []
    for root, dirs, files in walk(join_path(package, directory)):
        for file in files:
            paths.append(join_path(root, file)[(len(package) + 1):])
    return paths


additional_files = []
additional_files.extend(files_in('datdash', 'skeleton'))
additional_files.extend(files_in('datdash', 'javascript'))

setup(
    name='DatDash',
    version='0.1alpha',
    packages=['datdash'],
    package_data={'datdash': additional_files},
    license='MIT',
    long_description=open('README.md').read(),
    scripts=['bin/datdash'],
    install_requires=[
        'Flask',
        'CoffeeScript',
        'requests',
        'Flask-Sockets',
        'pyScss',
        'docopt',
        'pyScss',
    ]
)

