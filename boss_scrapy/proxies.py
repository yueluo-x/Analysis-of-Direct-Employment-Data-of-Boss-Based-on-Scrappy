# -*-coding:utf-8 -*-
# Auothor:yue_luo
import requests
from bs4 import BeautifulSoup
import lxml
from multiprocessing import Process, Queue
import random
import json
import time
import requests
import pymongo
def read_Database():
    client = pymongo.MongoClient('localhost', 27017)
    proxie_url = client['proxies']
    sheet_tab = proxie_url['sheet_tab']
    list =[]
    list_set = set()
    for d in sheet_tab.find({},{'_id':0}):
        if not d['proxy'] in list_set:
            list_set.add(d['proxy'])
            list.append(d['proxy'])
    print(list_set,len(list_set))
    print(list,len(list))
read_Database()
