# TextCortex Python Library

![alt text](https://github.com/textcortex/textcortex-python/raw/main/textcortex_logo.png?raw=true "TextCortex AI API Hemingway Logo")

Python Library for high level access to the TextCortex API. Generate product descriptions, blogs, ads and more using GPT architecture with a single request.

## Installation

Install the package using pip:

```sh
pip install textcortex
```

## Usage

1. Signup at https://textcortex.com
1. Sign-in and click on account on top right.
1. Go to API Key section and copy your key.
1. Set your API Key.


### Example usage

Make sure you have a TextCortex account. If you don't have one, [click here](https://app.textcortex.com/user/signup) to sign up (it just takes a few seconds).

Once you are signed in, you can head off to Account > API Key section. [Click here](https://app.textcortex.com/user/dashboard/settings/api-key) to visit that page.

Copy and paste your API key to the example below. It should return product descriptions based on the given parameters:

```python
from textcortex import TextCortex

API_KEY = 'YOUR_API_KEY' # <---- Paste your API key here

# Create the TextCortex API object and enter your API Key
tc = TextCortex(api_key=API_KEY)

# Generate product descriptions
product_description = tc.generate_product_descriptions(
   product_name='Black Leather Backpack Bag',
   product_category='Shoes & Bags, Women',
   brand='Cortexian',
   product_features='Color: Black, Material: Faux Leather',
   source_language='en',
   token_count=100,
   temperature=0.7,
   n_gen=4,
)
```

#### Response:

```json
[
   {
      "text":"The Cortexian Black Backpack is a stylish and functional bag that can be worn for any occasion. It features a back zipper pocket so you can keep your belongings secure. The black color is ideal for any day and all occasions, from work to school to weekend outings.",
      "id":"2ff2d503-3d6b-405e-a8a5-13196f970160"
   },
   {
      "text":"This cute and stylish black backpack is made for everyday use. The back is padded, fully adjustable and has a removable shoulder strap which can be extended to fit over your shoulder or wear like an arm/back pack. It also comes with two side pockets as well as a main compartment.",
      "id":"87d21b28-48f4-4b7b-90e4-6fab7d7dd0f8"
   },
   {
      "text":"The Cortexian Black Backpack is the perfect travel companion for those who want to keep things simple. This backpack has a padded shoulder straps and an adjustable waist strap, making it comfortable for long periods of use.",
      "id":"20297317-9be6-4457-9481-17d402a988ab"
   }
]
```

## Documentation

Browse the [documentation on TextCortex](https://textcortex.com/documentation/api).

<!-- ### Text Generation Variables

There are some variables that you need to send before making a request to Hemingwai.

Here is a brief summary of what those variables:
```
prompt: Prompting the HemingwAI to start writing on a specific subject

temperature: Floating number between 0-1. 0 being the lowest creativity and 1 being the highest. Default is 0.7

word_count: Integer which defines the maximum amount of words that can be produced by the HemingwAI

source_language: Language code of the source language of the written prompt. for example 'en' for English and 'de' for German.
We support 72 languages. If you don't know the language code you can also use 'auto' for this field to automatically sense the input language.

Examples: For example while generating ads, you can add your target segment as an option.
See examples.py for examples.
``` -->

## Getting help

To get help with using TextCortex Python library, join our [Discord](https://discord.textcortex.com/).