import sqlite3
import pandas as pd


def load_to_sqlite(df: pd.DataFrame, table_name: str, db_path="data/analytics.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql(table_name, conn, if_exists="replace", index=False)
    conn.close()
