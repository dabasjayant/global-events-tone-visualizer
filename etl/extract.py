import os
from etl.download import download_data

def load_data():
  if not os.path.isdir('dataset'):
    os.mkdir('dataset')

  download_data(20200101, 20201231)
  



