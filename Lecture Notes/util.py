import os
from dotenv import load_dotenv, find_dotenv

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

class Model:
    groq_api_key = None
    open_router_api_key = None
    model_name = "openai/gpt-3.5-turbo"
    base_url="https://openrouter.ai/api/v1"

    def __init__(self) -> None:
        _ = load_dotenv(find_dotenv())
        self.groq_api_key = os.environ["GROQ_API_KEY"]
        self.open_router_api_key = os.environ["OPENROUTER_API_KEY"]


    def get_model(self , groq: bool = False) -> "Model":
        if groq:
            model = ChatGroq(model=self.model_name)
        else:
            model = ChatOpenAI(
                model=self.model_name,
                api_key=self.open_router_api_key,
                base_url=self.base_url
            )

        return model
