from pyspark.sql.window import Window
from pyspark.sql.functions import rank, col

from etl.crawler import scrape

def filter_data(df):
  print('Processing data...')
  print('Please be patient ^ ^')
  df = df.selectExpr('_c1 as date', '_c39 as a1_lat', '_c40 as a1_long', '_c46 as a2_lat', '_c47 as a2_long', '_c31 as num_mentions', '_c30 as g_scale', '_c34 as avg_tone', '_c57 as source_url')
  df = df.dropDuplicates(['source_url'])
  df = df.na.drop(how='any')

  terms = ['coronavirus','covid','distancing','epidemic','health','hygiene','immunity','issolation','medical','pandemic','plasma','quarantine','recover','respiratory','restriction','sars','test','treatment','vaccine','virus','who']
  df = df.filter(df.source_url.rlike('|'.join(terms)))

  # # Web scraping to improve performance
  #
  # window = Window.partitionBy(df['date']).orderBy(df['num_mentions'].desc())
  # df = df.select('*', rank().over(window).alias('rank')).filter(col('rank') <= 1000)
  #
  # data = df.rdd.map(lambda x: 
  #   (x['date'],x['a1_lat'],x['a1_long'],x['a2_lat'],x['a2_long'],x['num_mentions'],x['g_scale'],x['avg_tone'],x['source_url'],scrape(x['source_url']))
  # ).toDF()
  # data = data.na.drop(how='any')
  # data = data.filter('_10 != ""')
  # data = data.selectExpr('_1 as date', '_2 as a1_lat', '_3 as a1_long', '_4 as a2_lat', '_5 as a2_long', '_6 as num_mentions', '_7 as g_scale', '_8 as avg_tone', '_9 as source_url', '_10 as source_text')
  
  return df