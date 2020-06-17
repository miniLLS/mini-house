import requests
import json

if __name__ == '__main__':
    '''
    破解百度翻译，浏览器通过Ajax请求和服务端异步交互，实现网页部分内容实施刷新。
    '''
    #构造请求参数
    target_word = str(input('Please enter a word:\n'))
    post_url = 'https://fanyi.baidu.com/sug'
    post_data = {
        'kw': target_word
    }
    #进行UA伪装
    post_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    #发起请求
    response = requests.post(url=post_url, data=post_data, headers=post_headers)
    content = response.json()
    #持久化存储
    filename = target_word + '.json'
    #通过json包的dump模块，对json对象进行序列化并存储
    json.dump(content, fp=open(file=filename,mode='w',encoding='utf-8'))
    print('Finished！')