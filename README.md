Data Engineering ETL Pipeline
A production-ready Python ETL pipeline demonstrating the extraction, transformation, and loading of raw sales data into a structured analytics database.

🚀 Project Overview
This project simulates a real-world e-commerce data workflow. It ingests raw CSV files, cleans and normalizes the data, joins customer and product information, and loads the result into a SQLite database for analytics.

⚙️ Tech Stack
Language: Python 3.x
Data Processing: Pandas
Database: SQLite
Version Control: Git / GitHub
📂 Project Structure
data-engineering-etl-pipeline/├── data/│   ├── raw/               # Input CSV files│   └── analytics.db       # Generated SQLite database (output)├── src/│   ├── extract.py          # Data ingestion logic│   ├── transform.py        # Cleaning & merging logic│   ├── load.py            # Database loading logic│   └── main.py            # Pipeline orchestrator├── requirements.txt└── README.md
🛠️ Workflow
Extract: Read customers.csv, orders.csv, and products.csv from data/raw/.
Transform:
Standardize column names (lowercase, underscores).
Handle data types (dates, floats).
Remove duplicates.
Merge orders with products to calculate total_amount.
Load: Store cleaned dataframes (customers, orders, products, analytics) into data/analytics.db.
📦 Installation
Clone this repository:
bash

git clone https://github.com/suraju025/data-engineering-etl-pipeline.git
cd data-engineering-etl-pipeline
Install dependencies:
bash

pip install -r requirements.txt
▶️ Usage
Run the ETL pipeline:

bash

python src/main.py
Upon successful execution:

You will see console logs indicating progress.
An analytics.db file will be generated in the data/ folder.
🔍 Database Schema
The analytics table joins orders with products and includes:

order_id, customer_id, product_id
quantity, order_date
product_name, category, price
total_amount (calculated field: quantity * price)
👨‍💻 Author
Suraj Upadhyay - GitHub
