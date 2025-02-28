import re

from setuptools import setup

with open('requirements.txt') as f:
    requirements = f.read().splitlines()  # type: ignore

version = ''
with open('discohook/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)  # type: ignore

readme = ''
with open('README.md') as f:
    readme = f.read() # type: ignore

setup(
    name="discohook",
    version=version,
    description="discord http api wrapper for serverless apps",
    url="https://github.com/jnsougata/discohook",
    author="Sougata Jana",
    author_email="jnsougata@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["discohook"],
    python_requires=">=3.6",
    install_requires=requirements,
    long_description=readme,
    long_description_content_type="text/markdown",
)
