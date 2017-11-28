from distutils.core import setup

setup(
    name='lib2to3',
    version='0.4',
    description='A description.',
    packages=['lib2to3', 'lib2to3.fixes', 'lib2to3.pgen2'],
    package_data={'lib2to3': ['Grammar.txt', 'PatternGrammar.txt', 'Grammar2.7.2.final.0.pickle', 'PatternGrammar2.7.2.final.0.pickle']}
)
