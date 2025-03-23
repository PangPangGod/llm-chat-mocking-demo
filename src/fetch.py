# fetch.py
# Base Instruction for requests
import requests


def fetch_title(url: str) -> str:
    response = requests.get(url)
    return response.text[:20]  # 간단하게 앞 20자만 반환
