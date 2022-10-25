from setuptools import setup

setup(
    name="discohook",
    version="0.0.1",
    description="discord webhook wrapper for serverless apps",
    url="https://github.com/jnsougata/discohook",
    author="jnsougata",
    author_email="jnsougata@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["discohook"],
    python_requires=">=3.6",
    install_requires=["fastapi", "aiohttp", "PyNaCl"],
)
