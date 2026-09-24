import pandas as pd

from src.api_client import CustomerAPI


api = CustomerAPI(
    "https://jsonplaceholder.typicode.com/users"
)

customers = api.get_customers()

customer_df = pd.DataFrame(customers)

customer_df = customer_df[
    ["id", "name", "email", "address"]
]

customer_df["city"] = customer_df["address"].apply(
    lambda x: x["city"]
)

customer_df = customer_df[
    ["id", "name", "email", "city"]
]

customer_df = customer_df.rename(
    columns={
        "id": "customer_id",
        "name": "customer_name"
    }
)

print(customer_df)
