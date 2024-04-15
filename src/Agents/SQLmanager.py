from langchain_openai import *
from langchain_openai import OpenAI


class SQLmanager():
    def __init__(self, APIKEY = None, llm = None, mode = "SQL"):
        # check if the LLM is provided
        if not llm:
            raise Exception("No LLM provided")
        else:
            self.llm = llm
        
        # check if the APIKEY is provided
        if not APIKEY:
            raise Exception("No APIKEY provided")
        else:
            from os import environ
            from dotenv import load_dotenv, find_dotenv
            load_dotenv(find_dotenv())
            self.APIKEY = environ.get("GPT_API_KEY")
        
        # check if the user provided a db or a API
        """if mode == "SQL":
           from yaml import load, FullLoader            
           with open("src/templates.yaml") as TEMPLATES:
                print(TEMPLATES)
                self.templates = load(TEMPLATES, Loader=FullLoader())["SQL_TEMPLATES"]"""
        
        # check wich LLM is being used so it can initialize the correct chatbot
        match llm:

            case "GPT":
                self.llm = OpenAI(api_key=self.APIKEY)
                print("Using GPT-3")

    def get_response(self, query: str) -> str:
        """
        get the response from the LLM
        """
        return self.llm.invoke(query)

    def get_ctx(self):
        pass

    def setTools(self):
        pass
     