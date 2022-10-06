boto3 1.24.87from setuptools import setup

setup(
    name='syncs3',
    version='0.1.0',    
    description='A package to give a document sync experience(and eficciency) like "repo sync", or "awscli s3 sync", and so forth.',
    url='https://github.com/TechnocultureResearch/syncs3',
    py_modules=['LocalObjectCache'],
    author='',
    author_email='',
    license='MIT License',
    package_dir={'':'syncs3'},
    install_requires=['boto3>=1.24.87'],
)
