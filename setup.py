from setuptools import setup, find_packages

setup(
    name='linux_sys_utils_py',
    version='0.1.0',
    packages=find_packages(),
    description='A collection of utilities for Linux system setup and configuration',
    author='Your Name',
    author_email='your.email@example.com',
    license='UNLICENSED',
    install_requires=[
        # List your project dependencies here,
        # e.g., 'requests>=2.25.1'
    ],
    scripts=[
        # List any script files you want to make executable and accessible,
        # e.g., 'bin/script1', 'bin/script2'
    ]
)