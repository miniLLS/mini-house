import requests
import json

if __name__ == '__main__':
    '''
    爬取豆瓣电影排行榜的详情数据
    '''
    target_url = 'https://movie.douban.com/j/search_subjects'
    target_params = {
        'type': 'movie',
        'tag': '热门',
        'sort': 'recommend',
        'page_limit': '100',
        'page_start': '0'
    }
    target_headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    response = requests.get(target_url, params=target_params, headers=target_headers)
    dic_obj = response.json()
    filename = 'movie_list.json'
    fp = open(file=filename, mode='w', encoding='utf-8')
    json.dump(obj=dic_obj, fp=fp, ensure_ascii=False)
    print('Finished!')