from setuptools import setup, find_packages

setup(
    name='lib2to3',
    version='0.1',
    description='A description.',
    packages=find_packages(),
    package_data={'lib2to3': ['*']},
    include_package_data=True,
    install_requires=[],
)
