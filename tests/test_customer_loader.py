
from unittest.mock import Mock

import pandas as pd

from src.customer_loader import CustomerDataLoader


def test_customer_data_inserted():

    # Mock database connection
    connection = Mock()

    # Mock cursor
    cursor = Mock()

    # When connection.cursor() is called,
    # return our mock cursor
    connection.cursor.return_value = cursor

    # Test data
    df = pd.DataFrame({
        "customer_id": ["C001"],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    # Create loader
    loader = CustomerDataLoader(connection)

    # Run method
    loader.load_data(df)

    # Check INSERT was executed
    cursor.execute.assert_called_once()


def test_correct_customer_values_inserted():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "customer_id": ["C001"],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    loader = CustomerDataLoader(connection)

    loader.load_data(df)

    # Get arguments passed to cursor.execute()
    call_args = cursor.execute.call_args

    # Second argument contains values
    values = call_args[0][1]

    assert values == (
        "C001",
        "John",
        "john@gmail.com",
        "Hyderabad"
    )


def test_commit_called():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "customer_id": ["C001"],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    loader = CustomerDataLoader(connection)

    loader.load_data(df)

    # Check database commit
    connection.commit.assert_called_once()


def test_cursor_closed():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "customer_id": ["C001"],
        "customer_name": ["John"],
        "email": ["john@gmail.com"],
        "city": ["Hyderabad"]
    })

    loader = CustomerDataLoader(connection)

    loader.load_data(df)

    # Check cursor was closed
    cursor.close.assert_called_once()


def test_multiple_customers_inserted():

    connection = Mock()
    cursor = Mock()

    connection.cursor.return_value = cursor

    df = pd.DataFrame({
        "customer_id": ["C001", "C002", "C003"],
        "customer_name": [
            "John",
            "David",
            "Rahul"
        ],
        "email": [
            "john@gmail.com",
            "david@gmail.com",
            "rahul@gmail.com"
        ],
        "city": [
            "Hyderabad",
            "Delhi",
            "Mumbai"
        ]
    })

    loader = CustomerDataLoader(connection)

    loader.load_data(df)

    # Three rows should result in
    # three execute() calls
    assert cursor.execute.call_count == 3
