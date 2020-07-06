# 聚焦爬虫：爬取页面中的制定内容。
#     -编码流程：
#         -指定url
#         -发起请求
#         -获取响应数据
#         -数据解析
#         -持久化存储
#
#     -数据解析分类：
#         -正则
#         -BeautifulSoup
#         -Xpath
#
#     -数据解析原理概述：
#        -解析的文本内容会在标签之间或者标签对应的属性中存储
#        -定位标签
#        -提取数据

import requests
import re
from bs4 import BeautifulSoup as BS
from lxml import etree
import os


def regular_expression():
    '''
    利用正则表达式爬取糗事百科中热图板块中的所有图片
    '''
    # 生成新文件夹
    if os.path.exists('./糗图') == False:
        os.mkdir('./糗图')
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    # 构建请求参数
    target_url = 'https://www.qiushibaike.com/imgrank/'
    # 发起请求
    page_text = requests.get(url=target_url, headers=headers).text
    # text(string),content(byte),json(object)
    # 解析提取图片地址
    pattern = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
    image_src_list = re.findall(pattern=pattern, string=page_text, flags=re.S)
    for image_src in image_src_list:
        image_src = 'http:' + image_src
        # 获取图片数据
        image_data = requests.get(url=image_src, headers=headers).content
        image_name = image_src.split('/')[-1]
        # 持久化存储
        file_name = './糗图/' + image_name
        with open(file=file_name, mode='wb') as fp:
            fp.write(image_data)
            fp.close()
            print(image_name + '\tDownloaded successfully')


def bs4():
    '''
    利用beautiful_soup进行html网页解析，需要导入bs4和lxml模块，实例化Beautiful_soup对象
    pip install bs4
    pip install lxml
    '''
    # UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    # 生成新文件夹
    if os.path.exists('./三国演义') == False:
        os.mkdir('./三国演义')
    # response = requests.get(url='https://www.douyu.com/', headers=headers).text
    # soup_obj = BS(response, 'lxml')
    # print(soup_obj)
    # print(soup_obj.img)
    # print(soup_obj.img['src'])
    # print(soup_obj.find('img', class_='DyImg-content is-normal'))
    # print(soup_obj.find_all('img'))
    # print(soup_obj.select('.class > tag1 > tag2'))
    '''
    爬取三国演义章节内容
    '''
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    soup_obj = BS(requests.get(url=url, headers=headers).text, 'lxml')
    for chapter in soup_obj.select('.book-mulu > ul > li > a'):
        chapter_url = chapter['href']
        chapter_name = chapter.string
        chapter_content = requests.get(url='http://www.shicimingju.com%s' % chapter_url, headers=headers).text
        chapter_obj = BS(chapter_content, 'lxml')
        for section in chapter_obj.select('.chapter_content > p'):
            with open(file='./三国演义/%s.txt' % chapter_name, mode='a+', encoding='utf-8') as fp:
                fp.write('\t' + section.text.replace(' ', '').strip() + '\n')
        print('%s Downloaded Successfully' % chapter_name)


def Xpath(selection):
    '''
    利用Xpath进行html网页解析，需要导入lxml模块，实例化etree对象
    pip install lxml
    etree.parse($filepath) or etree.HTML('$page_text')
    /：根节点查找，返回列表
    //：任意节点查找
    //div[@class='***']/p[3]：属性定位、索引定位（从1开始）
    /text()：取文本
    /@attrName：取属性
    '''
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    if selection == 1:
        '''
        爬取58同城的房源信息
        '''
        url = 'https://bj.58.com/ershoufang/'
        etree_obj = etree.HTML(requests.get(url=url, headers=headers).text)
        house_list = etree_obj.xpath('//ul[@class="house-list-wrap"]/li')
        for house_info in house_list:
            print('Name:\t' + house_info.xpath('./div[@class="list-info"]/h2/a/text()')[0].replace('\xa0', ''))
            print('Price:\t' + house_info.xpath('./div[@class="price"]/p[@class="sum"]/b/text()')[0] + 'w')
    elif selection == 2:
        '''
        爬取4K超清图片
        '''
        url = 'http://pic.netbian.com/4kmeinv'
        etree_obj = etree.HTML(requests.get(url=url, headers=headers).text)
        image_list = etree_obj.xpath('//ul[@class="clearfix"]/li')
        if not os.path.exists('./Pics'):
            os.mkdir('./Pics')
        for each_image in image_list:
            image_src = 'http://pic.netbian.com/' + each_image.xpath('.//img/@src')[0]
            image_data = requests.get(url=image_src, headers=headers).content
            image_name = each_image.xpath('.//img/@alt')[0]
            # 单个元素中文显示编解码问题
            image_name = image_name.encode('iso-8859-1').decode('gbk') + '.jpg'
            image_path = 'Pics/%s' % image_name
            with open(file=image_path, mode='wb') as fp:
                fp.write(image_data)
                print(image_name + 'downloaded successfully')
    else:
        print('No matched function')


if __name__ == '__main__':
    # regular_expression()
    # bs4()
    # Xpath(3)
