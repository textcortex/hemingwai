"""
This library allows you to quickly and easily use the TextCortex AI Web API via Python.
For more information on this library, see the README on GitHub.
    https://github.com/hemingwai/readme
For more information on the TextCortex AI API, see the docs:
    https://textcortex.com/documentation/api
"""

import requests


class TextCortex:

    def __init__(self, api_key):
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain',
                        'user-agent': 'Python-hemingwAI'}
        self.host = 'https://api.textcortex.com/hemingwai'
        self.api_key = api_key

    def build_json(self, prompt, category, parameters, character_count, source_language, creativity, n_gen):
        json_req = {
            "prompt": prompt,
            "category": category,
            "parameters": parameters,
            "character_count": character_count,
            "source_language": source_language,
            # Sets creativity, number between 0 and 1. Default is 0.65
            "creativity": creativity,
            "api_key": self.api_key,
            "n_gen": n_gen
        }
        return json_req

    def pass_results(self, req):
        if req.status_code == 403:
            print('API Key is invalid. Check out your API key on https://app.textcortex.com/user/account')
            return
        if req.status_code == 402:
            print(
                'Reached API Limits, increase limits by contacting us at dev@textcortex.com or upgrade your account')
            return
        if req.status_code == 500:
            print('An Error occured')
            print(req.json())
            return
        return req.json()['ai_results']

    def generate(self, prompt, parameters, character_count, source_language, creativity, n_gen=1):
        """
        Generates Text by autocompleting the given prompt using TextCortex Hemingway API

        :param str prompt: Input the your prompt to start generating text based on it.
        :param str parameters: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated possible text based on the given prompt
        """

        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt, category='Auto Complete', parameters=parameters,
                                                 character_count=character_count,source_language=source_language,
                                                 creativity=creativity, n_gen=n_gen))
        return self.pass_results(req=req)

    def generate_blog(self, blog_title, character_count, creativity, source_language, n_gen=1, blog_categories=None):
        """
        Generates Blog articles using TextCortex Hemingway API

        :param str blog_title: Input the title of the blog
        :param list blog_categories: Input keywords regarding to the blog category to have more relevant results as
        generated text output.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated blog articles with focus keyword and character length.
        """
        if blog_categories is not None:
            parameters = 'Blog Categories: ' + str(blog_categories)
        else:
            parameters = ''
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=blog_title, category='Blog Body',
                                                 parameters=parameters, character_count=character_count,
                                                 source_language=source_language, creativity=creativity,
                                                 n_gen=n_gen))
        return self.pass_results(req=req)

    def generate_ads(self, prompt, parameters, character_count, creativity, source_language, n_gen=1):
        """
        Generates Ad Copy using TextCortex Hemingway API

        :param str prompt: Input the title of the product or basically anything that you want to market
        :param str parameters: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated ad copies with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=prompt, category='Ads',
                                                 parameters=parameters, character_count=character_count,
                                                 source_language=source_language, creativity=creativity, n_gen=n_gen))
        return self.pass_results(req=req)

    def generate_email_body(self, email_subject, parameters, character_count, creativity, source_language, n_gen=1):
        """
        Generates Email Body text using TextCortex Hemingway API

        :param str email_subject: Input the email subject that you want to generate the email for.
        :param str parameters: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated email body text with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=email_subject, category='Email Body',
                                                 parameters=parameters, character_count=character_count,
                                                 source_language=source_language, creativity=creativity,
                                                 n_gen=n_gen))
        return self.pass_results(req=req)

    def generate_email_subject(self, keywords, parameters, character_count, creativity, source_language, n_gen=1):
        """
        Generates Email Subject Line using TextCortex Hemingway API

        :param str keywords: Input the keywords for generating email subject
        :param str parameters: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated email subject text with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=keywords, category='Email Subject',
                                                 parameters=parameters, character_count=character_count,
                                                 source_language=source_language, creativity=creativity,
                                                 n_gen=n_gen))
        return self.pass_results(req=req)

    def generate_product_descriptions(self, product_title, product_brand='', product_category=[], product_features=[],
                                      character_count=256, creativity=0.65, source_language='en', n_gen=1):
        """
        Generates Email Subject Line using TextCortex Hemingway API
        :param str product_title: Input the product title that you want to generate descriptions for.
        :param str product_brand: What is the brand of your product? If not known leave empty, as expected if empty
        this will reduce the quality of the output.
        :param list product_category: Input the product category that of the product, whole list can be found at:
        https://textcortex.com/documentation/api If you don't know the category, leave empty, but this will reduce the
        output quality. Example input: ['Clothing', 'Women', 'Shoes']
        :param list product_features: If you have additional product features pass this as a python list with strings
        as items in it, for example: ['Color: Red', 'Fit: Slim']
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns list of generated product descriptions.
        """
        parameters = ''
        if product_brand != '':
            parameters = parameters + "Brand: '" + product_brand + "'"
        if len(product_category) != 0:
            if parameters == '':
                parameters = parameters + "Category: " + str(product_category)
            else:
                parameters = parameters + " Category: " + str(product_category)
        if len(product_features) != 0:
            if parameters == '':
                parameters = parameters + "Features: " + str(product_features)
            else:
                parameters = parameters + " Features: " + str(product_features)

        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=product_title, category='Product Description',
                                                 parameters=parameters, character_count=character_count,
                                                 source_language=source_language, creativity=creativity,
                                                 n_gen=n_gen))
        return self.pass_results(req=req)