# src/extract.py
import pandas as pd
import os

class Extract:
    def __init__(self, data_dir="data/raw"):
        self.data_dir = data_dir

    def read_csv(self, filename):
        path = os.path.join(self.data_dir, filename)
        try:
            df = pd.read_csv(path)
            print(f"[INFO] Loaded {filename} - {df.shape[0]} rows, {df.shape[1]} columns")
            return df
        except FileNotFoundError:
            print(f"[ERROR] File not found: {path}")
            return None

    def extract_all(self):
        customers = self.read_csv("customers.csv")
        orders = self.read_csv("orders.csv")
        products = self.read_csv("products.csv")
        return customers, orders, products

if __name__ == "__main__":
    extractor = Extract()
    customers, orders, products = extractor.extract_all()
