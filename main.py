import os
import sys
import time
import shutil
from pyspark.sql import SparkSession

sys.dont_write_bytecode = True

from etl import extract, transform, load
from etl.autosave import save

if __name__ == '__main__':
  spark = SparkSession.builder.getOrCreate()

  if not os.path.exists('processed_data.csv'):
    # Extract raw data
    raw_data = extract.get_data(spark)
    # Necessary transformations
    data = transform.filter_data(raw_data)

    # Save state
    if os.path.exists('processed_data'):
      shutil.rmtree('processed_data')
    data.repartition(1).write.option('header','true').option('delimiter','\t').csv('processed_data')
    # Save data state
    save()
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

  # Load data
  load.load_data()

  # Simulate
