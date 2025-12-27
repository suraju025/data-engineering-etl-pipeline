import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw")

def extract_data():
    customers = pd.read_csv(DATA_PATH / "customers.csv")
    orders = pd.read_csv(DATA_PATH / "orders.csv")
    products = pd.read_csv(DATA_PATH / "products.csv")

    return customers, orders, products
