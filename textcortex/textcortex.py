"""
This library allows you to quickly and easily use the TextCortex AI Web API via Python.
For more information on this library, see the README on GitHub.
    https://github.com/hemingwai/readme
For more information on the TextCortex AI API, see the docs:
    https://textcortex.com/documentation/api
"""

import logging
import time
from functools import wraps
from typing import List

import requests


def retry(ExceptionToCheck, tries=4, delay=3, backoff=2, logger=None, default_value=None):
    """Retry calling the decorated function using an exponential backoff.
    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry
    :param ExceptionToCheck: the exception to check. may be a tuple of
        exceptions to check
    :type ExceptionToCheck: Exception or tuple
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param logger: logger to use. If None, print
    :type logger: logging.Logger instance
    """
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return f(*args, **kwargs)
                except ExceptionToCheck as e:
                    msg = "%s, Retrying in %d seconds..." % (str(e), mdelay)
                    if logger:
                        logger.warning(msg)
                    else:
                        print(msg)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= backoff
            return default_value
        return f_retry  # true decorator
    return deco_retry


class APIError(Exception):
    def __init__(self, msg=''):
        self.msg = msg
        logging.error(msg)

    def __str__(self):
        return self.msg


class TextCortex:

    def __init__(self, api_key: str):
        self.url = 'https://api.textcortex.com/hemingwai/generate_text'
        self.api_key = api_key

    @retry(Exception, tries=4, logger=logging, default_value=None)
    def _get_results(self, prompt: str, parameters, character_count: int, source_language: str, creativity: float,
                     category: str, n_gen: int) -> List:
        """Connect to the API and retrieve the generated text"""
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain', 'user-agent': 'Python-hemingwAI'}

        payload = {
            "prompt": prompt,
            "category": category,
            "parameters": parameters,
            "character_count": character_count,
            "source_language": source_language,
            "creativity": creativity,  # Sets creativity, number between 0 and 1. Default is 0.65
            "api_key": self.api_key,
            "n_gen": n_gen
        }

        try:
            req = requests.post(self.url, headers=headers, json=payload)
            if req.status_code == 403:
                raise APIError(
                    'API Key is invalid. Check out your API key on https://app.textcortex.com/user/account')
            if req.status_code == 402:
                raise APIError(
                    'Reached API Limits, increase limits by contacting us at dev@textcortex.com or upgrade your account')
            if req.status_code == 500:
                raise APIError('Ops, error {}'.format(str(req.json())))
            return req.json()['ai_results']
        except APIError:
            return
        except Exception:
            # this will force to retry the connection
            raise

    def generate(self, prompt: str, parameters: str = "", character_count: int = "256", source_language: str = "en",
                 creativity: float = 0.65, n_gen=1) -> List:
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

        return self._get_results(prompt, parameters, character_count, source_language, creativity, 'Auto Complete', n_gen)

    def generate_blog(self, blog_title: str, character_count: int = "256", creativity: float = 0.65,
                      source_language: str = "en", n_gen=1, blog_categories: List[str] = []) -> List:
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
        parameters = ""
        if blog_categories is not None:
            parameters = "Blog Categories: " + str(blog_categories)

        return self._get_results(blog_title, parameters, character_count, source_language, creativity, 'Blog Body', n_gen)

    def generate_blog_title(self, character_count: int = "100", creativity: float = 0.65,
                            source_language: str = "en", n_gen=4, blog_categories: List[str] = []) -> List:
        """
        Generates Blog articles using TextCortex Hemingway API

        :param list blog_categories: Input keywords regarding to the blog category to have more relevant results as
        generated title output.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated blog titles with focus keyword and character length.
        """

        return self._get_results(prompt=str(blog_categories), parameters='', character_count=character_count,
                                 source_language=source_language, creativity=creativity, category='Blog Title',
                                 n_gen=n_gen)

    def generate_meta_description(self, page_title: str, page_keywords: str, character_count: int = "256",
                                  creativity: float = 0.65, source_language: str = "en", n_gen=1) -> List:
        """
        Generates Meta Descriptions using TextCortex Hemingway API

        :param str page_title: Input the title of the web page.
        :param str page_keywords: Input keywords regarding to the web page so that AI can generate more relevant results
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated meta descriptions with focus keyword and character length.
        """

        return self._get_results(page_title, page_keywords, character_count, source_language, creativity,
                                 'Meta Description', n_gen)

    def generate_ads(self, prompt: str, parameters: str, character_count: int = "256", creativity: float = 0.65,
                     source_language: str = "en", n_gen=1) -> List:
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
        return self._get_results(prompt, parameters, character_count, source_language, creativity, 'Ads',
                                 n_gen)

    def generate_email_body(self, email_subject: str, parameters: str, character_count: int = "256",
                            creativity: float = 0.65, source_language: str = "en", n_gen=1) -> List:
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
        return self._get_results(email_subject, parameters, character_count, source_language, creativity, 'Email Body', n_gen)

    def generate_email_subject(self, keywords: str, parameters: str, character_count: int = "256",
                               creativity: float = 0.65,
                               source_language: str = "en", n_gen=1) -> List:
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
        return self._get_results(keywords, parameters, character_count, source_language, creativity, 'Email Subject', n_gen)

    def generate_product_descriptions(self, product_title: str, product_brand: str, product_category: List = [],
                                      product_features: List = [], character_count: int = 256,
                                      creativity: float = 0.65, source_language: str = 'en', n_gen=1) -> List:
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
        parameters = ""
        if product_brand is not None:
            parameters += " Brand: '{}'".format(product_brand)

        if len(product_category) > 0:
            parameters += " Category: ".format(str(product_category))

        if len(product_features) > 0:
            parameters = parameters + \
                " Features: {}".format(str(product_features))

        parameters = parameters.strip().replace("  ", " ")

        return self._get_results(product_title, parameters, character_count, source_language, creativity,
                                 'Product Description', n_gen)

    def generate_instagram_caption(self, product: str, audience: str, character_count: int = 256,
                                   creativity: float = 0.65, source_language: str = 'en', n_gen=1) -> List:
        """
        Generates Email Subject Line using TextCortex Hemingway API
        :param str product: What is the product that you are promoting in instagram?
        :param str audience: Who is your target group that you are trying to communicate with?
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns list of generated product descriptions.
        """
        return self._get_results(product, audience, character_count, source_language, creativity,
                                 'Instagram Caption', n_gen)

    def paraphrase(self, prompt: str, tone: str = "", character_count: int = 128,
                   creativity: float = 0.65, source_language: str = 'en', n_gen=5) -> List:
        """
        Generates Email Subject Line using TextCortex Hemingway API
        :param str prompt: Sentence that you would like to paraphrase
        :param str tone: What kind of paraphrasing tone you would like to use?
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns the paraphrased sentences
        """
        return self._get_results(prompt, tone, character_count, source_language, creativity,
                                 'Paraphrase', n_gen)

    def extend(self, prompt: str, parameters: str = "", character_count: int = 256,
               creativity: float = 0.65, source_language: str = 'en', n_gen=2) -> List:
        """
        Extends a given paragraph with a blog like writing tone using TextCortex Hemingway API
        :param str prompt: Sentence that you would like to paraphrase
        :param str parameters: Not used, leave empty.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int character_count: Set the maximum length of the article to be generated in characters.
        :param float creativity: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns the paraphrased sentences
        """
        return self._get_results(prompt, parameters, character_count, source_language, creativity,
                                 'Extend', n_gen)
