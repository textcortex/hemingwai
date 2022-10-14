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
        self.url = 'https://api.textcortex.com/hemingwai/generate_text_v3'
        self.api_key = api_key

    @retry(Exception, tries=2, logger=logging, default_value=None)
    def _get_results(self, prompt: dict, token_count: int, source_language: str, temperature: float,
                     template_name: str, n_gen: int, generation_source: str = None) -> List:
        """Connect to the API and retrieve the generated text"""
        headers = {'Content-type': 'application/json',
                   'Accept': 'text/plain', 'user-agent': 'Python-hemingwAI'}
        payload = {
            "template_name": template_name,
            "prompt": prompt,
            "temperature": temperature,
            "token_count": token_count,
            "n_gen": n_gen,
            "source_language": source_language,
            "api_key": self.api_key,
            "generation_source": generation_source
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
            return req.json()['generated_text']
        except APIError:
            return
        except Exception:
            # this will force to retry the connection
            raise

    def generate(self, prompt: str, token_count: int = 100,
                 source_language: str = "en", temperature: float = 0.65, n_gen=1) -> List:
        """
        Generates Text by autocompleting the given prompt using TextCortex Hemingway API

        :param str prompt: Input the your prompt to start generating text based on it.
        :param int token_count: Set the maximum length of the article to be generated.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.65
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated possible text based on the given prompt
        """
        prompt = {"original_sentence": prompt}
        return self._get_results(prompt=prompt, template_name="auto_complete", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)

    def generate_blog(self, blog_title: str, blog_keywords: str, token_count: int = 100,
                      temperature: float = 0.65, source_language: str = "en", n_gen=1) -> List:
        """
        Generates Blog articles using TextCortex Hemingway API

        :param str blog_title: Input the title of the blog
        :param str blog_keywords: Input keywords regarding to the blog category to have more relevant results as
        generated text output.
        :param int token_count: Set the maximum length of the article to be generated in characters.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.65
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated blog articles with focus keyword and character length.
        """
        prompt = {
            "blog_title": blog_title,
            "blog_keywords": blog_keywords
        }

        return self._get_results(prompt=prompt, template_name="blog_body", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)

    def generate_blog_title(self, blog_intro: str, blog_keywords: str, token_count: int = 20,
                            temperature: float = 0.65, source_language: str = "en", n_gen=1) -> List:
        """
        Generates Blog titles using TextCortex Hemingway API

        :param str blog_intro: Intro of the blog article
        :param str blog_keywords: Input keywords regarding to the blog category to have more relevant results as
        generated text output.
        :param int token_count: Set the maximum length of the title to be generated in characters.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.65
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically choosing.
        :param int n_gen: Defines how many different options will be sent according to the result.
        :return: Returns list of generated blog articles with focus keyword and character length.
        """
        prompt = {
            "blog_intro": blog_intro,
            "blog_keywords": blog_keywords
        }

        return self._get_results(prompt=prompt, template_name="blog_title", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)

    def generate_product_descriptions(self, product_name: str, brand: str, product_category: str,
                                      product_features: str, token_count: int = 100,
                                      temperature: float = 0.65, source_language: str = 'en', n_gen=2) -> List:
        """
        Generates Email Subject Line using TextCortex Hemingway API
        :param str product_name: Input the product title that you want to generate descriptions for.
        :param str brand: What is the brand of your product? If not known leave empty, as expected if empty
        this will reduce the quality of the output.
        :param str product_category: Input the product category that of the product, whole list can be found at:
        https://textcortex.com/documentation/api If you don't know the category, leave empty, but this will reduce the
        output quality. Example input: ['Clothing', 'Women', 'Shoes']
        :param str product_features: If you have additional product features pass this as a string
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int token_count: Set the maximum length of the article to be generated in characters.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.65
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns list of generated product descriptions.
        """
        prompt = {
            "product_name": product_name,
            "brand": brand,
            "product_category": product_category,
            "product_features": product_features
        }

        return self._get_results(prompt=prompt, template_name="product_description", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)

    def paraphrase(self, prompt: str, tone: str = "", token_count: int = 50,
                   temperature: float = 1, source_language: str = 'en', n_gen=5) -> List:
        """
        Paraphrases given sentence based on the tonality.
        :param str prompt: Sentence that you would like to paraphrase
        :param str tone: What kind of paraphrasing tone you would like to use?
        :param int n_gen: Defines how many different options will be returned.
        :param int token_count: Set the maximum length of the article to be generated in characters.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns the paraphrased sentences
        """
        prompt = {"original_sentence": prompt, "tone": tone}
        return self._get_results(prompt=prompt, template_name="paraphrase", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)

    def extend(self, prompt: str, token_count: int = 256,
               temperature: float = 0.65, source_language: str = 'en', n_gen=2) -> List:
        """
        Extends a given paragraph with a blog like writing tone using TextCortex Hemingway API
        :param str prompt: Sentence that you would like to paraphrase
        :param int n_gen: Defines how many different options will be sent according to the result.
        :param int token_count: Set the maximum length of the article to be generated in characters.
        :param float temperature: Value between 0-1, 1 is the highest creativity. Default is 0.7
        :param str source_language: Enter the language of the input. 'en' for English, 'auto' for automatically
        sensing the input. If the input language is english and if you choose another language for the source, this will
        change the output language to the set language code.
        :return: Returns the paraphrased sentences
        """
        prompt = {"original_sentence": prompt}
        return self._get_results(prompt=prompt, template_name="auto_complete", token_count=token_count,
                                 source_language=source_language, temperature=temperature, n_gen=n_gen)
