import os
import requests

class LLMClient:
    def __init__(self):
        self.endpoint = os.getenv("AZURE_LLM_ENDPOINT")
        self.api_key = os.getenv("AZURE_API_KEY")

    def ask(self, prompt):
        payload = {"messages": [{"role": "user", "content": prompt}]}
        headers = {
            "Content-Type": "application/json",
            "api-key": self.api_key
        }
        r = requests.post(self.endpoint, json=payload, headers=headers, verify=True)
        return r.json()
