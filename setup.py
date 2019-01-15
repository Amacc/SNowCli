from setuptools import find_packages, setup

setup(
    author='Adam Mcchesney',
    name='snow***REMOVED***',
    description='snow***REMOVED*** - playing around with ***REMOVED*** commands',
    license=open('LICENSE').read(),
    long_description=open('README.md').read(),
    py_modules=find_packages(),
    version='0.1.1',
    url='https://github.com/Amacc/SNowCli',
    install_requires=[
        'Click==7.0',
        'toolz==0.9.0'
    ],
    entry_points='''
        [console_scripts]
        snow***REMOVED***=snow***REMOVED***.main:main
    ''',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
