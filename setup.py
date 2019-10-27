import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autodiscover",
    version="0.0.3",
    author="Nícolas Zein",
    author_email="niczein@gmail.com",
    description="Autodiscover modules in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nicolaszein/autodiscover",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
)
