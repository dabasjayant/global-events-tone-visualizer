
from etl.crawler import scrape

def filter_data(df):
  print('Processing data...')
  print('Please be patient ^ ^')
  df = df.selectExpr('_c1 as date', '_c39 as a1_lat', '_c40 as a1_long', '_c46 as a2_lat', '_c47 as a2_long', '_c31 as num_mentions', '_c30 as g_scale', '_c34 as avg_tone', '_c57 as source_url')
  df = df.na.drop(how='any')
  data = df.rdd.map(lambda x: 
    (x['date'],x['a1_lat'],x['a1_long'],x['a2_lat'],x['a2_long'],x['num_mentions'],x['g_scale'],x['avg_tone'], scrape(x['source_url']))
  ).toDF()
  print('Done!')
  return data