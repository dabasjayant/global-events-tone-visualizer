import os
from keplergl import KeplerGl
import pandas as pd
import json

def load_data():
  df = pd.read_csv('processed_data.csv', delimiter='\t')

  with open('config.json', 'r') as file:
    _config = json.loads(file.readline())

  _map = KeplerGl(height=500, data={"data_1": df}, config=_config)

  _map.save_to_html(file_name='covid_visualizer.html')