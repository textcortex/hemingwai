# TextCortex - HemingwAI
![alt text](https://textcortex.com/static/media/logo-dark.466b1e13.png "TextCortex AI API Hemingway Logo")

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
                    product_title='Black Backpack', product_category='Shoes & Bags', target_segment='',
                    source_language='en', character_count=300, creativity=0.7)
print(product_description)
```

####Response:
```json
    "ai_results": [
        {
            "generated_text": " This blue cotton duvet set will make your bedroom set, comfortable and stylish. The duvet cover set is made from soft polyester fabric with detailed embroidery. The duvet cover set has blue and silver floral embroidery details. The decorative pillows are decorated with black and silver embroidery. The duvet cover set is completed with coordinated Two shams, one in the same design. The duvet cover set is",
            "rank": 0.9533,
            "text_length": 407,
            "word_frequency": [
                {
                    "word": "cover",
                    "frequency": 4
                },
                {
                    "word": "embroidery",
                    "frequency": 3
                },
                {
                    "word": "duvet",
                    "frequency": 5
                },
                {
                    "word": "with",
                    "frequency": 3
                }
            ],
            "word_count": 67
        }...
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
```

### Parameters
There are some parameters that you need to send before making a request to Hemingwai.

Here is a brief summary of what those parameters:

`prompt: Prompting the HemingwAI to start writing on a specific subject`

`creativity: Floating number between 0-1. 0 being the lowest creativity and 1 being the highest. Default is 0.7`

`character_length: Integer which defines the maximum amount of characters that can be produced by the HemingwAI`

`source_language: Language code of the source language of the written prompt. for example 'en' for English and 'de' for German.
We support 72 languages. If you don't know the language code you can also use 'auto' for this field to automatically sense the input language.`

`target_segment: Used for setting the tone of the generated copy text. It can be basically anything but please keep it plausible :)
Examples: Young people, middle aged people, young men, women, etc..`

#### Still have questions?
You can have a look at the [HemingwAI's documentation on TextCortex website](https://textcortex.com/documentation/api)

[Or talk to us at the TextCortex Dev Community on slack](https://join.slack.com/t/textcortexaicommunity/shared_invite/zt-rmaw7j10-Lz9vf86aF5I_fYZAS7JafQ)

