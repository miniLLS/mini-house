#!/usr/bin/env python
#-*- coding:utf-8 -*-

import requests

target_url = 'http://www.douyu.com'

response = requests.get(url=target_url)
text = response.text
content = response.content

# if __name__ == "__main__":
# print(response)
print(type(response))
# print(text)
print(type(text))
# print(content)
print(type(content))