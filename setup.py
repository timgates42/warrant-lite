from setuptools import setup, find_packages


version = '1.0.3.2'

README="""Small Python library for process SRP requests for AWS Cognito. This library was initially included in the [Warrant](https://www.github.com/capless/warrant) library. We decided to separate it because not all projects and workfows need all of the helper classes and functions in Warrant."""

setup(
    name='warrant-lite42',
    version=version,
    description=README,
    long_description=README,
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Environment :: Web Environment",
    ],
    keywords='aws,cognito,srp,capless',
    author='Capless.io',
    author_email='opensource@capless.io',
    maintainer='Brian Jinwright',
    packages=find_packages(),
    url='https://github.com/capless/warrant-lite',
    license='Apache License 2.0',
    install_requires=[
        'boto3>=1.4.3',
        'envs>=1.2.4',
        'python-jose>=3.0.0',
        'requests>=2.18.4',
    ],
    include_package_data=True,
    zip_safe=True,

)
