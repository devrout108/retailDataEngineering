# check if the final data is inserted into the database correctly

from unittest.mock import Mock

import pandas as pd

from src.final_loader import FinalDataLoader


def test_final_data_inserted():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "sale_id": [1],
        "customer_id": ["C001"],
        "product_id": ["P001"],
        "quantity": [2],
        "price": [100.0],
        "sale_date": [pd.Timestamp("2026-09-25")],
        "total_amount": [200.0],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    loader = FinalDataLoader(connection)

    loader.load_data(df)

    cursor.execute.assert_called_once()

# check if the correct values are inserted into the database

def test_correct_final_sales_values_inserted():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "sale_id": [1],
        "customer_id": ["C001"],
        "product_id": ["P001"],
        "quantity": [2],
        "price": [100.0],
        "sale_date": [pd.Timestamp("2026-09-25")],
        "total_amount": [200.0],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    loader = FinalDataLoader(connection)

    loader.load_data(df)

    call_args = cursor.execute.call_args

    values = call_args[0][1]

    assert values == (
        1,
        "C001",
        "P001",
        2,
        100.0,
        pd.Timestamp("2026-09-25").date(),
        200.0,
        "John",
        "john@gmail.com",
        "Hyderabad"
    )    

def test_multiple_final_sales_inserted():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "sale_id": [1, 2, 3],
        "customer_id": ["C001", "C002", "C003"],
        "product_id": ["P001", "P002", "P003"],
        "quantity": [2, 3, 1],
        "price": [100.0, 200.0, 50.0],
        "sale_date": [
            pd.Timestamp("2026-09-25"),
            pd.Timestamp("2026-09-25"),
            pd.Timestamp("2026-09-25")
        ],
        "total_amount": [200.0, 600.0, 50.0],
        "customer_name": ["John", "David", "Rahul"],
        "email": [
            "john@gmail.com",
            "david@gmail.com",
            "rahul@gmail.com"
        ],
        "city": ["Hyderabad", "Delhi", "Mumbai"]
    })

    loader = FinalDataLoader(connection)

    loader.load_data(df)

    assert cursor.execute.call_count == 3    