from extract import load_csv
from transform import clean_customers, clean_orders, clean_products
from load import load_to_sqlite


def main():
    customers = load_csv("data/raw/customers.csv")
    orders = load_csv("data/raw/orders.csv")
    products = load_csv("data/raw/products.csv")

    customers_clean = clean_customers(customers)
    orders_clean = clean_orders(orders)
    products_clean = clean_products(products)

    load_to_sqlite(customers_clean, "customers")
    load_to_sqlite(orders_clean, "orders")
    load_to_sqlite(products_clean, "products")

    print("✅ ETL Pipeline executed successfully!")


if __name__ == "__main__":
    main()
