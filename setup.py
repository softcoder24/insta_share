import re

import setuptools

with open('insta_share/__init__.py') as f:
    version = re.search(r'([0-9]+(\.dev|\.|)){3}', f.read()).group(0)

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="insta_share",
    version=version,
    author="soft_coder",
    description="Python package for sharing on Instagram",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/softcoder24/insta_share",
    packages=setuptools.find_packages(),
    license='apache-2.0',
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3'
    ],
    python_requires='>=3.6',
)
