	# coding: UTF-8

import os
import requests
import lxml.html as lh
import urllib
import zipfile
import glob
import operator
from time import sleep

def download_data(date_start, date_end):
  print('Verifying data...')
  gdelt_base_url = 'http://data.gdeltproject.org/events/'

  # get the list of all the links on the gdelt file page
  page = requests.get(gdelt_base_url+'index.html')
  doc = lh.fromstring(page.content)
  link_list = doc.xpath('//*/ul/li/a/@href')

  # separate out those links that begin with four digits 
  file_list = [x for x in link_list if str.isdigit(x[0:8]) and int(x[0:8]) >= date_start and int(x[0:8]) <= date_end]

  print('Downloading missing data...')
  loader_count = 1
  for i, item in enumerate(file_list):
    # print status
    if not i == 0 and i%int(len(file_list)/20) == 0:
      print(u'[%-20s] %d%%' % ('█'*loader_count, float(i)/len(file_list)*100))
      loader_count += 1

    # download file
    try_count = 1
    while not os.path.isfile('dataset/'+item) and try_count < 6: 
      urllib.urlretrieve(url=gdelt_base_url+item, filename='dataset/'+item)
      sleep(2**try_count)
      try_count += 1

  print('[%-20s] %d%%' % ('='*20, 100))
  print('Done!')