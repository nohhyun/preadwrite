from setuptools import setup

setup(
    name='preadwrite',
    version='0.0.1',
    author='Nohhyun Park',
    author_email='nohhyun.park@gmail.com',
    license='MIT License',
    description='pread, pwrite interface for pypy 6.0',
    cffi_modules=["preadwrite/preadwrite_build.py:ffibuilder"],
    packages=['preadwrite'],
    install_requires=["cffi>=1.0.0"],
    setup_requires=["cffi>=1.0.0"]
)
