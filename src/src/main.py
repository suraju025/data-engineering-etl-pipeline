# src/main.py
from extract import Extract
from transform import clean_customers, clean_orders, clean_products, create_analytics_table
from load import load_to_sqlite

def main():
    print("--- Starting ETL Pipeline ---")

    # 1. Extract
    extractor = Extract()
    customers, orders, products = extractor.extract_all()

    # Validation check
    if customers is None or orders is None or products is None:
        print("[ERROR] Extraction failed. Please check your data files.")
        return

    # 2. Transform
    print("[INFO] Transforming data...")
    customers_clean = clean_customers(customers)
    orders_clean = clean_orders(orders)
    products_clean = clean_products(products)

    # Create analytics table (join orders + products)
    analytics = create_analytics_table(orders_clean, products_clean)

    print("[INFO] Transformation complete.")

    # 3. Load
    print("[INFO] Loading data into SQLite...")
    load_to_sqlite(customers_clean, "customers")
    load_to_sqlite(orders_clean, "orders")
    load_to_sqlite(products_clean, "products")
    load_to_sqlite(analytics, "analytics")

    print("--- ETL Pipeline Completed Successfully ---")
    print("Database created at: data/analytics.db")

if __name__ == "__main__":
    main()
