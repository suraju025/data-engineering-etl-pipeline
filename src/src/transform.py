import pandas as pd


def transform_customers(customers: pd.DataFrame) -> pd.DataFrame:
    customers.columns = customers.columns.str.lower()
    customers = customers.drop_duplicates()
    customers["signup_date"] = pd.to_datetime(customers["signup_date"])
    return customers


def transform_products(products: pd.DataFrame) -> pd.DataFrame:
    products.columns = products.columns.str.lower()
    products = products.drop_duplicates()
    products["price"] = products["price"].astype(float)
    return products


def transform_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders.columns = orders.columns.str.lower()
    orders = orders.drop_duplicates()

    if "order_date" in orders.columns:
        orders["order_date"] = pd.to_datetime(orders["order_date"])

    return orders
