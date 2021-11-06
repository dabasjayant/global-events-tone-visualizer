import os
import sys
sys.dont_write_bytecode = True

from etl import extract, transform, load

if __name__ == '__main__':
  data = extract.load_data()
