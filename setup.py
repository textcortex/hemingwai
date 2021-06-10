from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'Generate product descriptions, blogs, ads and more using GPT architecture with a single request to ' \
              'TextCortex API a.k.a Hemingwai'
LONG_DESCRIPTION = "Signup at textcortex.com to get your API key and start " \
                   "generating text content with a single API call, leveraging TextCortex's GPT architecture."

setup(
   name='textcortex',
   version='1.0',
   author='TextCortex AI',
   author_email='dev@textcortex.com',
   packages=find_packages(),
   url='https://textcortex.com/documentation/api',
   license='LICENSE.txt',
   description=DESCRIPTION,
   long_description=LONG_DESCRIPTION,

   keywords=['TextCortex AI', 'gpt-2', 'gpt-3', 'gptNEO', 'generate text',
             'natural language generation', 'NLP', 'hemingwai', 'transformer', 'generate copy text using AI'],
   install_requires=[
    "requests"
   ],
   classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Customer Service",
            "Intended Audience :: Information Technology",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
            "Natural Language :: English",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python :: 3"
        ]
)