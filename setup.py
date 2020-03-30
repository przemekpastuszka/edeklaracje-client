from setuptools import setup, find_packages
import io

import edeklaracje


def read_lines(file_path):
    with open(file_path) as fp:
        return [line.strip() for line in fp]


setup(
    name="edeklaracjeclient",
    version=edeklaracje.__version__,
    author="Przemyslaw Pastuszka",
    author_email="pastuszka.przemyslaw@gmail.com",
    license="MIT",
    url="https://github.com/rtshadow/simple-dash",
    description=(
        "Library to simplify building Plotly Dash applications"
    ),
    long_description=io.open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    packages=find_packages(),
    install_requires=read_lines("requirements.txt")
)