import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    license = fh.read()

setuptools.setup(
    name='pydates',
    version='0.1',
    license=license,
    packages=setuptools.find_packages(
        exclude=('tests', 'docs')
    ),
    url='https://github.com/MikeSmithLab/pydates',
    install_requires=[
        'python-dateutil',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
    include_package_data=True,
)
