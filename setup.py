from distutils.core import setup

setup(
    name='lib2to3',
    version='0.3',
    description='A description.',
    packages=['lib2to3', 'lib2to3.fixes', 'lib2to3.pgen2'],
    package_data={'lib2to3': ['Grammar.txt', 'PatternGrammar.txt']}
)
