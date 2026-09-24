import pandas as pd

from api_client import CustomerAPI
from database import DatabaseConnection
from customer_loader import CustomerDataLoader


# Get data from API
api = CustomerAPI(
    "https://jsonplaceholder.typicode.com/users"
)

customers = api.get_customers()


# Convert API response to DataFrame
customer_df = pd.DataFrame(customers)


# Select required fields
customer_df = customer_df[
    ["id", "name", "email", "address"]
]


# Extract city
customer_df["city"] = customer_df["address"].apply(
    lambda x: x["city"]
)


# Select final columns
customer_df = customer_df[
    ["id", "name", "email", "city"]
]


# Rename columns
customer_df = customer_df.rename(
    columns={
        "id": "customer_id",
        "name": "customer_name"
    }
)


# Convert ID to our format
customer_df["customer_id"] = customer_df[
    "customer_id"
].apply(
    lambda x: f"C{x:03d}"
)


print("\nFinal Customer Data:")
print(customer_df)


# Connect to MySQL
db = DatabaseConnection()

connection = db.connect()


# Load DataFrame into MySQL
loader = CustomerDataLoader(connection)

loader.load_data(customer_df)


# Close connection
db.close()