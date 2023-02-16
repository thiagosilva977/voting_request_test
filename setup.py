from setuptools import setup, find_packages

setup(
    name='belvo_test',
    version='1.0.0',
    packages=find_packages(),
    url='',
    license='',
    author='Thiago Silva',
    author_email='thiagosilva977@hotmail.com',
    description='Elections to decide the pandas future.',
    setup_requires=['wheel'],
    install_requires=[
        "click>=8.1.2",
        "setuptools>=62.1.0",
        "requests>=2.27.1",
        "bs4>=0.0.1",
        "Shapely>=1.8.1.post1",
        "pymongo>=4.1.1",
        "pandas>=1.4.2",
        "fastparquet>=0.8.1",
        "pyarrow>=10.0.1",
        "fake_useragent>=1.1.1"
    ],
    entry_points={
        'console_scripts': [
            "start-elections=belvo_test.main:main"
        ]
    }

)
