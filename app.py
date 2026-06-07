import polars as pl
from src.Load_function import load_data
from src.Clean_data import clean_data   

precios= load_data('data\Bakery price.csv')
ventas= load_data('data\Bakery sales.csv')
print(ventas.schema)
