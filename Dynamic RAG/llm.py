from typing import List, Literal, Optional, Mapping, Any, Union
import json
#from lonestar.lonestar_models import infer_chatgpt, infer_embeddings
from langchain.embeddings.base import Embeddings
from pydantic import BaseModel
from langchain.callbacks.manager import CallbackManagerForLLMRun
from langchain.llms.base import LLM
from openai import AzureOpenAI
import httpx
from openai import OpenAI
import httpx
import os

httpx_client = httpx.Client(verify=False)


client = AzureOpenAI(
    api_version="2023-12-01-preview",
    azure_endpoint="",
    api_key="",
    http_client=httpx_client
)

class LangchainDSXLLM(LLM):
    @property
    def _llm_type(self) -> str:
        return "LangchainDSXLLMLLM"

    def _call(self, prompt: str, stop: Optional[List[str]] = None, run_manager: Optional[CallbackManagerForLLMRun] = None) -> str:
        if stop is not None:
            raise ValueError("stop kwargs are not permitted.")

        # Construct the message payload for AzureOpenAI
        messages = [{"role": "user", "content": prompt}]

        # Make the call to Azure OpenAI
        completion = client.chat.completions.create(
            model="gpt-35-turbo",
            messages=messages
        )

        response = completion.choices[0].message.content.strip()
        return response

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {}

