'''
UA:User-Agent（请求载体的身份标识）
UA检测（反爬机制）：门户网站的服务器会检测对应请求的载体身份标识，如果检测到请求的载体身份标识为某一款浏览器，
说明是一个正常的请求。但是，如果检测到不是基于浏览器的，则表示该请求为不正常的请求（爬虫），可能被拒绝。

UA伪装：让爬虫的请求载体身份标识伪装成浏览器。
'''

import requests

target_url = 'https://www.sogou.com/web'
key_word = input('enter a word:\n')
param = {'query': key_word}
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}

if __name__ == '__main__':
    '''
    简易网页采集器，爬取指定词条对应的搜索结果页面。
    '''
    response = requests.get(url=target_url,params=param,headers=header)
    content = response.text
    file_name = key_word + '.html'
    with open (file_name,'w',encoding='utf-8') as f:
        f.write(content)
        f.close
    print (file_name + 'saved successfully')