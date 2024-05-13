import csv
import re
import os
import sys
import json
import requests
from pymysql import *
from utils.query import query


def init():
    if not os.path.exists('./tianjinData.csv'):
        with open('./tianjinData.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([
                'title',
                'cover',
                'city',
                'region',
                'address',
                'rooms_desc',
                'area_range',
                'all_ready',
                'price',
                'hourseDecoration',
                'company',
                'hourseType',
                'on_time',
                'open_date',
                'tags',
                'totalPrice_range',
                'sale_status',
                'detail_url'
            ])


def writerRow(row):
    with open('./tianjinData.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(row)


def get_data(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
        'cookie': 'lianjia_uuid=951272e1-5885-4f4a-8534-418c0b77e87c; _smt_uid=652ce757.89c6244; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218b3767af4216-0f2a1fe1f59165-78505770-1327104-18b3767af431146%22%2C%22%24device_id%22%3A%2218b3767af4216-0f2a1fe1f59165-78505770-1327104-18b3767af431146%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fcn.bing.com%2F%22%2C%22%24latest_referrer_host%22%3A%22cn.bing.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; _ga=GA1.2.442743781.1697441626; _ga_TJZVFLS7KV=GS1.2.1704591776.1.0.1704591776.0.0.0; _ga_WLZSQZX7DE=GS1.2.1704591776.1.0.1704591776.0.0.0; _qzja=1.535251590.1704591783276.1704591783276.1704591783276.1704591783276.1704591783276.0.0.0.1.1; _ga_049GGDBYWQ=GS1.2.1704591785.1.0.1704591785.0.0.0; _ga_B3G62E46BE=GS1.2.1704591785.1.0.1704591785.0.0.0; _jzqa=1.4456798814074604000.1697441624.1704591772.1705173561.3; _jzqx=1.1697441624.1705173561.2.jzqsr=cn%2Ebing%2Ecom|jzqct=/.jzqsr=bd%2Efang%2Elianjia%2Ecom|jzqct=/; lianjia_ssid=f260e18a-cc26-48a5-9722-04fd69d86327; GUARANTEE_POPUP_SHOW=true; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYzQzOWQ3YTEyM2NiZDkyNDRmZmM5NTM0MzY2Yjk4ZDk5ZmI0ZjFkZjczMTc0ZGI3ZTA3YjhlZjYwOWM2NDlmY2VjZTExNTM5MDhkMzA5ZjAwOWMxNGY4MGMwNDgxMTMwY2VlODIyYjIyYTU5Yjk2NTgzOTNlMTE1Mzc2NzhjNTY0MmE4NDYyYTM1NzAzZGM2OTBmZWE3OTZkZjJjMzA2ZTdjMTgwMmE2YWI2Y2FiMTFkNjkyZjg3MTc4NzBlMjE0ZGE5MmMxYTRlYzkxMDUwMDgzYzllZGUyYjRmMjhmMjc5ODVjNjQ5NWFhZDk3ODNkM2JiOTQxNDdlNGM1NmUyOFwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI0MTRlMmY5OFwifSIsInIiOiJodHRwczovL3RqLmxpYW5qaWEuY29tL3p1ZmFuZy8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; select_city=130600; _gid=GA1.2.152993007.1705834714',
        'Referer': 'https://bd.fang.lianjia.com/loupan/'
    }
    response = requests.get(url, headers)
    if response.status_code == 200:
        return response.json()['data']['list']
    else:
        return None


def parse_data(hourseDataList, city, url):
    for hourseInfo in hourseDataList:
        try:
            title = hourseInfo['title']
            cover = hourseInfo['cover_pic']
            region = hourseInfo['district']
            address = hourseInfo['address']
            rooms_desc = json.dumps(hourseInfo['frame_rooms_desc'].replace('居', '').split('/'))
            area_range = json.dumps(hourseInfo['resblock_frame_area_range'].replace('㎡', '').split('-'))
            all_ready = hourseInfo['permit_all_ready']
            price = hourseInfo['average_price']
            hourseDecoration = hourseInfo['decoration']
            company = hourseInfo['developer_company'][0]
            hourseType = hourseInfo['house_type']
            on_time = hourseInfo['on_time']
            open_date = hourseInfo['open_date']
            tags = json.dumps(hourseInfo['tags'])
            totalPrice_range = json.dumps(hourseInfo['reference_total_price'].split('-'))
            sale_status = hourseInfo['process_status']


            writerRow([
                title,
                cover,
                city,
                region,
                address,
                rooms_desc,
                area_range,
                all_ready,
                price,
                hourseDecoration,
                company,
                hourseType,
                on_time,
                open_date,
                tags,
                totalPrice_range,
                sale_status,
                url
            ])

        except:
            continue


def save_to_sql():
    with open('./tianjinData.csv', 'r', encoding='utf-8') as reader:
        readerCsv = csv.reader(reader)
        next(readerCsv)
        for h in readerCsv:
            query('''
                insert into hourse_info(title,cover,city,region,address,rooms_desc,area_range,all_ready,price,hourseDecoration,company,hourseType,on_time,open_date,tags,totalPrice_range,sale_status,detail_url)
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                
            ''', [
                h[0], h[1], h[2], h[3], h[4], h[5], h[6], h[7], h[8], h[9], h[10], h[11], h[12], h[13], h[14], h[15],
                h[16], h[17]
            ])


def main():
    init()
    with open('./cityData.csv', 'r', encoding='utf-8') as readerFile:
        reader = csv.reader(readerFile)
        next(reader)
        for city in reader:
                for page in range(1, 10):
                    try:
                        url = 'https:' + re.sub('pg1', 'pg' + str(page), city[1])
                        print('正在爬取 %s 城市的房屋数据在第 %s 页 路径为: %s' % (
                            city[0],
                            page,
                            url

                        ))
                        hourseDetaList = get_data(url)
                        parse_data(hourseDetaList, city[0], url)

                    except:
                        continue


if __name__ == '__main__':
    save_to_sql()
