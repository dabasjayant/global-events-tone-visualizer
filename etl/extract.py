import os
import shutil
import zipfile
from etl.download import download_data
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

def load_data():
  if not os.path.isdir('dataset'):
    os.mkdir('dataset')

  name_list = download_data(20200101, 20201231)

  if not os.path.isdir('temp'):
    os.mkdir('temp')

  for item in name_list:
    if not os.path.isfile('temp/'+item.replace('.zip', '')):
      with zipfile.ZipFile('dataset/'+item, 'r') as zip_ref:
        zip_ref.extractall('temp')

  df = spark.read.load('temp/*', format='csv', sep='\t', inferSchema='true', header='false')
  df.show(5)
  



