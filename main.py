import os
import sys
import time
from requests.api import head
from pyspark.sql import SparkSession

sys.dont_write_bytecode = True

from etl import extract, transform, load

if __name__ == '__main__':
  spark = SparkSession.builder.getOrCreate()

  if not os.path.exists('processed_data.csv'):
    # Extract raw data
    raw_data = extract.get_data(spark)
    # Necessary transformations
    data = transform.filter_data(raw_data)

    # Save state
    data.write.option('header',True).option('delimiter','\t').csv('processed_data')
  else:
    # Load saved state
    start_time = time.time()
    print('Found saved data! Now loading...')
    data = spark.read.load('processed_data.csv', format='csv', sep='\t', inferSchema='true', header='true')
    print('Done!')
    print("--- Took %s seconds ---" % (time.time() - start_time))

  # Preview data
  data.show(5)
  print((data.count(), len(data.columns)))

  # Load data in classifier


  # Simulate
