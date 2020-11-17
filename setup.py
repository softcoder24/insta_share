import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insta_share",
    version="0.0.1",
    author="soft_coder",
    description="Python package for sharing on Instagram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softcoder24/insta_share",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
