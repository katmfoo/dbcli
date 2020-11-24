from setuptools import setup

setup(
    name='db-cli',
    version='0.0.1',
    url='https://github.com/pricheal/db-cli',
    author='Patrick Richeal',
    author_email='patrickricheal@gmail.com',
    description='Universal database repl written in python with prompt toolkit, yet to be named',
    license='MIT',
    packages=['db-cli'],
    install_requires=[
        'prompt_toolkit'
    ],
    entry_points={
        'console_scripts': [
            'db-cli=db-cli:main'
        ]
    }
)
