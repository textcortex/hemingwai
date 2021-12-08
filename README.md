# TextCortex - HemingwAI
![alt text](https://github.com/textcortex/hemingwai/raw/main/textcortex_logo.png?raw=true "TextCortex AI API Hemingway Logo")

Generate product descriptions, blogs, ads and more using GPT architecture with a single request to TextCortex API a.k.a 
HemingwAI

## How To Generate Content using TextCortex Hemingwai:
1. Signup at https://textcortex.com
2. Sign-in and click on account on top right.
3. Go to API Key section and copy your key.
4. Install textcortex package:
   `pip install textcortex`
5. Enter your API Key to hemingwai
6. Generate copy text with a single line of code!

### Here is an example request to Hemingwai for generating Product Descriptions:

```python
from textcortex import TextCortex

# Create the hemingwai object and enter your API Key
hemingwai = TextCortex(api_key='YOUR_API_KEY')

# Generate Product Descriptions using Hemingwai
product_description = hemingwai.generate_product_descriptions(
                    product_title='Black Leather Backpack Bag', product_category=['Shoes & Bags', 'Women'],
                    product_brand='Cortexian', product_features=['Color: Black', 'Material: Faux Leather'],
                    source_language='en', character_count=400, creativity=0.7, n_gen=2)
```

#### Response:
```json
[
   {
      "generated_text":" The Cortexians collection of shoes and bags are designed with a focus on comfort, style, quality and function. These products are made for the modern woman who wants to look stylish yet still feel comfortable in their footwear. With fashionable colors and designs that will make any outfit pop, Cortexian is sure to be your favorite shoe brand!",
      "rank":0.9652,
      "text_length":345,
      "word_frequency":[
         
      ],
      "word_count":58
   },
   {
      "generated_text":" The Cortexian is a classic backpack. It features the same style that has been popular for years with its unique design and functionality. This item comes in black color.",
      "rank":0.9176,
      "text_length":170,
      "word_frequency":[
         
      ],
      "word_count":29
   }
]
```

### What kind of texts are possible to generate?

Currently we support the following methods for generating copy text like the following:
```python
# Generate Blog Articles:
hemingwai.generate_blog

# Autocomplete the rest using Hemingwai
hemingwai.generate

# Generate Ad copies using Hemingwai
hemingwai.generate_ads

# Generate Email Body using Hemingwai
hemingwai.generate_email_body

# Generate Email Subject using Hemingwai
hemingwai.generate_email_subject

# Generate Product Descriptions using Hemingwai
hemingwai.generate_product_descriptions

# Classify Complex Job Headlines into understandble Job Titles
hemingwai.classify_job_headlines
```

### Text Generation Variables
There are some variables that you need to send before making a request to Hemingwai.

Here is a brief summary of what those variables:
```
prompt: Prompting the HemingwAI to start writing on a specific subject

creativity: Floating number between 0-1. 0 being the lowest creativity and 1 being the highest. Default is 0.7

character_length: Integer which defines the maximum amount of characters that can be produced by the HemingwAI

source_language: Language code of the source language of the written prompt. for example 'en' for English and 'de' for German.
We support 72 languages. If you don't know the language code you can also use 'auto' for this field to automatically sense the input language.

parameters: Used for setting the tone of the generated copy text. It can be basically anything but please keep it plausible :)

Examples: For example while generating ads, you can add your target segment as an option.
See examples.py for examples.
```

#### Still have questions?
You can have a look at the [HemingwAI's documentation on TextCortex website](https://textcortex.com/documentation/api)

[Or talk to us at the TextCortex Dev Community on slack](https://join.slack.com/t/textcortexaicommunity/shared_invite/zt-rmaw7j10-Lz9vf86aF5I_fYZAS7JafQ)

#### Maintainer/Creator
TextCortex Team (https://textcortex.com)

#### License
MIT
