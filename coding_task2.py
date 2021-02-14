#!/usr/bin/env python3
import requests

payload = {"tags": "wisdom|happiness", "limit": "5"}
r = requests.get("https://api.quotable.io/quotes", params=payload)
results = r.json()["results"]

for i, r in enumerate(results, start=1):
    print(f"{i}. {r['content']} -- {r['author']}\n")