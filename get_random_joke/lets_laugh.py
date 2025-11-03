from abc import ABC ,abstractmethod
import requests as req
from bs4 import BeautifulSoup as beso
import re
import random
import string
from huggingface_hub import InferenceClient
import os
from urllib.parse import urlencode


class Joke(ABC):
    @abstractmethod
    def get_random_joke(self):
        pass
    

class EnglishDadJoke(Joke):
    english_dad_jokes_api_url = "https://official-joke-api.appspot.com/random_joke"
    def get_random_joke(self):
        res_json = req.get(self.english_dad_jokes_api_url).json()
        return f"{res_json['setup']}\n{res_json['punchline']}"


class PersianJoke(Joke):
    def get_random_joke_link(self):
        random_page_joke = 'page/%s/'%random.randint(2,200)
        page_link = f"https://farsijokes.com/category/persian-jokes/{random_page_joke}"
        res = req.get(page_link)
        soup = beso(res.text,"html.parser")
        jokes_link = soup.select(".entry-container a")
        random_joke_link = jokes_link[random.randint(0,len(jokes_link)-1)]
        random_joke_link = random_joke_link['href']
        return random_joke_link

    def is_fingilish(self,text):
        for letter in text:
            if letter in string.ascii_letters:
                return True
        return False 


    def get_random_joke(self):
        joke_link = self.get_random_joke_link()
        # print(joke_link)
        res = req.get(joke_link)
        # print(res)
        soup = beso(res.text,'html.parser')
        dirthy_format_joke = str(soup.select("#container .entry-content p"))
        # print(dirthy_format_joke)
        clean_format_joke = re.sub(r"<[^>]+>","",dirthy_format_joke)
        clean_format_joke = re.sub(r"\s+"," ",clean_format_joke).strip()
        joke = clean_format_joke.replace("[","").replace("]","").replace("&amp;#1","")
        return {"joke-text":joke , "is-fingilish":self.is_fingilish(joke)}


    def check_joke_format_with_llm(self,joke_text):
        if self.is_fingilish(joke_text):
            return joke_text
        prompt = f"""
    `    You are an AI that checks the quality of Persian jokes.
        Determine if the following text is:
        1. A complete sentence.
        2. A coherent joke.
        3. Written properly in Persian.

        Respond with one word: 'valid' or 'invalid'.

        Text:
        {joke_text}
        """
        #compelting this part later (after i learn deeply about ai)
        pass

    
class EnglishPlus18Joke(Joke):
    def get_random_joke(self):
        base_url = "https://v2.jokeapi.dev/joke/Dark"
        params = {
            "blacklistFlags": "nsfw",  # Include NSFW by NOT blacklisting
            "type": "single",
            "lang": "en"
        }
        full_url = base_url + "?" + urlencode(params)  # Auto-encodes
        response = req.get(full_url)
        if response.status_code != 200:
            return response.text  # See the error JSON
        else:
            data = response.json()
            return (data["joke"] if not data.get("error") else data["message"])





# testing the classes area

# j = EnglishDadJoke().get_random_joke()
# print(j)

# pj = PersianJoke().get_random_joke()
# print(pj)


# Ep18j = EnglishPlus18Joke().get_random_joke()
# print(Ep18j)






