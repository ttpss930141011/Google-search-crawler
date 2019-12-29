#!/usr/bin/python
# #-*-coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random
def main():
    
    headerlist = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36 OPR/43.0.2442.991",
           "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36 OPR/42.0.2393.94",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36 OPR/47.0.2631.39",
           "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
           "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0",
           "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko"]
    #隨機選擇headers
    user_agent = random.choice(headerlist)
    headers = {'User-Agent': user_agent}

    key = input('輸入查詢:\n')
    driver = webdriver.Chrome()
    driver.get('https://www.google.com')

    q  = driver.find_element_by_name('q')
    q.send_keys(key+'\n')
    time.sleep(1)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    
    try:                                               #有輔助搜尋
        for ele in soup.find('div', 'i4J0ge'):
            try:                                            #無多餘標籤
                print(ele.text)
            except:
                if ele == 'm'or'n':                         #有多餘標籤則跳過此次迴圈
                    continue
                print(ele.text)
    except:                                            #無輔助搜尋
        aList = []

        for ele in soup.find_all('div','g'):                
            
            try:
                result = ele.find("h3").text + ele.find("a").get("href")
                aList.append(result)                            #將搜尋結果逐條加入陣列
            except:
                pass
        print(random.choice(aList))                         #最後隨機Print一條項目
        
if __name__ == '__main__':
    main()
