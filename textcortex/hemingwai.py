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
        self.host = 'http://localhost:5000/hemingwai/'
        self.api_key = api_key

    def generate_blog(self, blog_title, target_segment, character_length, creativity, source_language):
        """
        :param blog_title: Input the title of the blog
        :param target_segment: Input your target audience for tone setting
        :param character_length: Set the maximum length of the article to be generated
        :param creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :return: Returns list of generated blog articles with focus keyword and character length.
        """
        data = {
            "prompt": blog_title,
            "category": 'Blog Article',
            "target_segment": target_segment,
            "character_count": character_length,
            "source_language": source_language,
            # Sets creativity, number between 0 and 1. Default is 0.65
            "creativity": creativity,
            "api_key": self.api_key
        }
        req = requests.post(self.host + '/generate_text', json=data, headers=self.headers)
        if req.status_code == 403:
            print('API Key is wrong')
            return
        if req.status_code == 402:
            print(
                'Reached API Limits, increase limits by contacting us at dev@textcortex.com or upgrade your account')
            return
        return req.json()['ai_results']
