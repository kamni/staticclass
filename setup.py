from setuptools import setup, find_packages


setup(
    name='staticclass',
    version=0.1,
    description='Convert all methods to your class to static methods without a decorator.',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers'
    ],
    packages=find_packages(exclude=('tests',))
)
