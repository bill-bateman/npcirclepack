from setuptools import setup

setup(
    name="npcirclepack",
    version="0.1.0",
    author="Bill Bateman",
    author_email="bill@batemanzhou.com",
    packages=["npcirclepack"],
    url="https://github.com/bill-bateman/npcirclepack",
    license='ISC License',
    description="Circle packing utility using numpy arrays.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=["numpy"],
)