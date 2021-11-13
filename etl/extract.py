import os
import zipfile
import time

from etl.download import download_data

def get_data(spark):
  
  if not os.path.isdir('dataset'):
    os.mkdir('dataset')

  name_list = download_data(20200101, 20201231)

  if not os.path.isdir('temp'):
    os.mkdir('temp')

  for item in name_list:
    if not os.path.isfile('temp/'+item.replace('.zip', '')):
      with zipfile.ZipFile('dataset/'+item, 'r') as zip_ref:
        zip_ref.extractall('temp')


  start_time = time.time()
  print('Extracting data...')
  df = spark.read.load('temp/2020*', format='csv', sep='\t', inferSchema='true', header='false')
  print('Done!')
  print("--- Took %s seconds ---" % (time.time() - start_time))
  
  return df



