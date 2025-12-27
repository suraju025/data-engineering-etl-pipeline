# src/transform.py
import pandas as pd

def clean_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    if 'signup_date' in df.columns:
        df['signup_date'] = pd.to_datetime(df['signup_date'])
    return df

def clean_orders(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    if 'order_date' in df.columns:
        df['order_date'] = pd.to_datetime(df['order_date'])
    return df

def clean_products(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower()
    df = df.drop_duplicates()
    if 'price' in df.columns:
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
    return df

def create_analytics_table(orders_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    merged = orders_df.merge(products_df, on='product_id', how='left')
    merged['total_amount'] = merged['quantity'] * merged['price']
    analytics = merged[['order_id', 'customer_id', 'product_id', 'quantity', 'order_date',
                       'product_name', 'category', 'price', 'total_amount']]
    return analytics
