"""
Setup script for physics-calculator package.
"""

from setuptools import setup, find_packages

setup(
    name="physics-calculator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python library for quantum mechanics calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/physics-calculator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
    ],
)
