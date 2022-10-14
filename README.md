# TextCortex - HemingwAI
![alt text](https://github.com/textcortex/hemingwai/raw/main/textcortex_logo.png?raw=true "TextCortex AI API Hemingway Logo")

Generate product descriptions, blogs, ads and more using GPT architecture with a single request to TextCortex API a.k.a 
HemingwAI

## How To Generate Content using TextCortex Hemingwai:
1. [Signup to TextCortex to get your free API Key](https://app.textcortex.com/user/signup?registration_source)
2. Go to API Key section and copy your key.
3. Install textcortex package:
   `pip install textcortex`
4. Enter your API Key to hemingwai
5. Generate relevant text, content or code with a single line of code!

### Here is an example request to Hemingwai for generating Product Descriptions:

```python
from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='YOUR_API_KEY')

# Generate Product Descriptions using Hemingwai
product_description = hemingwai.generate_product_descriptions(
                    product_name='Black Leather Backpack Bag', product_category='Shoes & Bags, Women',
                    brand='Cortexian', product_features='Color: Black, Material: Faux Leather',
                    source_language='en', word_count=100, temperature=0.7, n_gen=4)
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

### What kind of texts are possible to generate?

Currently we support the following methods for generating copy text like the following:
```python
# Generate Blog Articles:
hemingwai.generate_blog

# Generate Blog Titles:
hemingwai.generate_blog_titles

# Autocomplete the rest using Hemingwai
hemingwai.generate

# Extend paragraphs with a blog writing tone using Hemingwai
hemingwai.extend

# Generate Product Descriptions using Hemingwai
hemingwai.generate_product_descriptions

# Paraphrase a given sentence with a tone change or without.
hemingwai.paraphrase
```

### Text Generation Variables
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
```

#### Still have questions?
You can have a look at the [HemingwAI's documentation on TextCortex website](https://textcortex.com/text-generation-api)

[Or talk to us at the TextCortex Dev Community on slack](https://discord.textcortex.com)

#### Maintainer/Creator
TextCortex Team (https://textcortex.com)

#### License
MIT
