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
        self.headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        self.host = 'https://api.textcortex.com/hemingwai'
        self.api_key = api_key

    def build_json(self, prompt, category, target_segment, character_count, source_language, creativity):
        json_req = {
            "prompt": prompt,
            "category": category,
            "target_segment": target_segment,
            "character_count": character_count,
            "source_language": source_language,
            # Sets creativity, number between 0 and 1. Default is 0.65
            "creativity": creativity,
            "api_key": self.api_key
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

    def generate(self, prompt, target_segment, character_count, source_language, creativity):
        """
        Generates Text by autocompleting the given prompt using TextCortex Hemingway API

        :param str prompt: Input the your prompt to start generating text based on it.
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated possible text based on the given prompt
        """

        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt, category='Free Text', target_segment=target_segment,
                                                 character_count=character_count,source_language=source_language,
                                                 creativity=creativity))
        return self.pass_results(req=req)

    def generate_blog(self, blog_title, target_segment, character_count, creativity, source_language):
        """
        Generates Blog articles using TextCortex Hemingway API

        :param str blog_title: Input the title of the blog
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated blog articles with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=blog_title, category='Blog Article',
                                                 target_segment=target_segment, character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)

    def generate_ads(self, prompt, target_segment, character_count, creativity, source_language):
        """
        Generates Ad Copy using TextCortex Hemingway API

        :param str prompt: Input the title of the product or basically anything that you want to market
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated ad copies with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=prompt, category='Ads',
                                                 target_segment=target_segment, character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)

    def generate_email_body(self, email_subject, target_segment, character_count, creativity, source_language):
        """
        Generates Email Body text using TextCortex Hemingway API

        :param str email_subject: Input the email subject that you want to generate the email for.
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated email body text with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=email_subject, category='Email Body',
                                                 target_segment=target_segment, character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)

    def generate_email_subject(self, keywords, target_segment, character_count, creativity, source_language):
        """
        Generates Email Subject Line using TextCortex Hemingway API

        :param str keywords: Input the keywords for generating email subject
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated email body text with focus keyword and character length.
        """
        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=keywords, category='Email Subject',
                                                 target_segment=target_segment, character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)

    def generate_product_descriptions(self, product_title, product_category, target_segment, character_count, creativity,
                                      source_language):
        """
        Generates Email Subject Line using TextCortex Hemingway API

        :param str product_title: Input the product title that you want to generate descriptions for.
        :param str product_category: Input the product category that of the product, whole list can be found at:
        https://textcortex.com/documentation/api If you don't know the category, leave empty.
        :param str target_segment: Input your target audience for tone setting
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated email body text with focus keyword and character length.
        """

        if product_category == '':
            product_category = 'Product Description'

        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=product_title, category=product_category,
                                                 target_segment=target_segment, character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)

    def classify_job_headlines(self, job_headline,
                               character_count: int = 192,
                               creativity: float = 0.4,
                               source_language: str = 'en'):
        """

        :param job_headline: Job Headline that needs to be classified as job title. Also can be called as data cleaning.
        :param character_count: Default is 192, if you have unusually long headlines to classify you can pick 384 or more.
        :param creativity: Default is 0.1, higher values might help to classify complex headlines but also more prone to
        making mistakes.
        :param source_language: TextCortex can classify jobs in any language, if the job headline is in english please
        enter 'en' for automatic language sensing, use 'auto'
        :return: Returns the resulting Job Title
        """

        req = requests.post(self.host + '/generate_text', headers=self.headers,
                            json=self.build_json(prompt=job_headline, category='Job Classifier',
                                                 target_segment='', character_count=character_count,
                                                 source_language=source_language, creativity=creativity))
        return self.pass_results(req=req)
