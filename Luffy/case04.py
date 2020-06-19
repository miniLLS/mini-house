import requests
import json
import time

if __name__ == '__main__':
    '''
    爬取国家药品监督管理总局中基于中华人民共和国化妆品生产许可证相关数据
    http://125.35.6.84:81/xk/
    -动态加载数据
    -首页中对应的企业信息数据是通过ajax动态请求的
    '''
    # 进行UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    #构建请求参数
    target_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsList'
    id_list = []
    for page in range (1, 3):
        page = str(page)
        post_data = {
            'on': 'true',
            'page': page,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        #发起请求
        response_1 = requests.post(url=target_url, data=post_data, headers=headers)
        info_dic = response_1.json()
        for each in info_dic['list']:
            id_list.append(each['ID'])

    #获取单个企业的id
    for each_list in id_list:
        id_data = {
            'id': each_list
        }
        cr_code_url = 'http://125.35.6.84:81/xk/itownet/portalAction.do?method=getXkzsById'
        # 获取单个企业的社会信用代码
        response_2 = requests.post(url=cr_code_url, data=id_data, headers=headers)
        single_company_info = response_2.json()
        cr_code_info = {
            'company_name': single_company_info['epsName'],
            'cr_code': single_company_info['businessLicenseNumber']
        }
        print(cr_code_info)
        #避免服务端对请求间隔的限制
        time.sleep(3)

    # #持久化存储
    # filename = 'permission_info.json'
    # json.dump(obj=info_dic, fp=open(file=filename, mode='w', encoding='utf-8'), ensure_ascii=False)