import pandas as pd
import glob

def save():
  print('Saving processed data...')

  all_files = glob.glob('processed_data/*.csv')

  li = []

  for filename in all_files:
    df = pd.read_csv(filename, delimiter='\t')
    li.append(df)

  frame = pd.concat(li, axis=0)
  frame = frame.sort_values('date')
  frame.to_csv('processed_data2.csv', sep='\t', index=False, encoding='utf-8')

  print('Done!')