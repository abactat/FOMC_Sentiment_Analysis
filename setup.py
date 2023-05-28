from setuptools import find_packages, setup

setup(
    name='src',
    packages=find_packages(),
    version='0.1.0',
    description='Training an NLP model to ingest the Fed's FOMC minutes and, with other variables, predict the Fed's next policy action.',
    author='Alexander Bactat',
    license='MIT',
)
