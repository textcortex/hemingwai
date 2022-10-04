from setuptools import setup, find_packages

DESCRIPTION = "Python library for high-level access to the TextCortex API"

# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="textcortex",
    version="1.0.10",
    author="TextCortex AI",
    author_email="dev@textcortex.com",
    packages=find_packages(),
    url="https://github.com/textcortex/textcortex-python",
    license="MIT",
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "TextCortex AI",
        "gpt-2",
        "gpt-3",
        "gptNEO",
        "generate text",
        "natural language generation",
        "NLP",
        "transformer",
        "generate copy text using AI",
    ],
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
    ],
)
