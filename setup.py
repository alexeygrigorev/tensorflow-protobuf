import pathlib
from setuptools import setup
from setuptools import find_packages

from version import __version__

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="tensorflow-protobuf",
    version=__version__,
    description="Protobuf files from TensorFlow and TensorFlow-Serving",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/alexeygrigorev/tensorflow-protobufr",
    author="TensorFlow authors",
    author_email="alexey@datatalks.club",
    license="Original Tensorflow licence",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=find_packages(include=('tensorflow*', )),
    include_package_data=True,
    install_requires=["protobuf"],
)