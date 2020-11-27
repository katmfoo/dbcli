from setuptools import setup

setup(
    name='dbcli',
    version='0.0.1',
    url='https://github.com/pricheal/dbcli',
    author='Patrick Richeal',
    author_email='patrickricheal@gmail.com',
    description='Universal database repl written in python with prompt toolkit, yet to be named',
    license='MIT',
    packages=['dbcli'],
    install_requires=[
        'prompt_toolkit',
        'mysql-connector-python'
    ],
    entry_points={
        'console_scripts': [
            'dbcli=dbcli:main'
        ]
    }
)
