
import pandas as pd

from src.data_cleaner import SalesDataCleaner


def test_duplicate_rows_removed():

    df = pd.DataFrame({
        "quantity": [2, 2],
        "price": [100, 100],
        "sale_date": ["2026-01-01", "2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert len(result) == 1


def test_quantity_converted_to_numeric():

    df = pd.DataFrame({
        "quantity": ["2"],
        "price": [100],
        "sale_date": ["2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert result["quantity"].iloc[0] == 2
    assert pd.api.types.is_numeric_dtype(result["quantity"])


def test_price_converted_to_numeric():

    df = pd.DataFrame({
        "quantity": [2],
        "price": ["100"],
        "sale_date": ["2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert result["price"].iloc[0] == 100
    assert pd.api.types.is_numeric_dtype(result["price"])


def test_missing_quantity_replaced_with_one():

    df = pd.DataFrame({
        "quantity": [None],
        "price": [100],
        "sale_date": ["2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert result["quantity"].iloc[0] == 1


def test_missing_price_replaced_with_median():

    df = pd.DataFrame({
        "quantity": [1, 2, 3],
        "price": [100, None, 300],
        "sale_date": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-03"
        ]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    # Median of 100 and 300 = 200
    assert result["price"].iloc[1] == 200


def test_negative_quantity_removed():

    df = pd.DataFrame({
        "quantity": [-2, 2],
        "price": [100, 200],
        "sale_date": [
            "2026-01-01",
            "2026-01-02"
        ]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert len(result) == 1
    assert result["quantity"].iloc[0] == 2


def test_zero_quantity_removed():

    df = pd.DataFrame({
        "quantity": [0, 2],
        "price": [100, 200],
        "sale_date": [
            "2026-01-01",
            "2026-01-02"
        ]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert len(result) == 1
    assert result["quantity"].iloc[0] == 2


def test_sale_date_converted_to_datetime():

    df = pd.DataFrame({
        "quantity": [2],
        "price": [100],
        "sale_date": ["2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert pd.api.types.is_datetime64_any_dtype(
        result["sale_date"]
    )


def test_total_amount_calculated():

    df = pd.DataFrame({
        "quantity": [2],
        "price": [100],
        "sale_date": ["2026-01-01"]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert result["total_amount"].iloc[0] == 200


def test_multiple_records_cleaned_correctly():

    df = pd.DataFrame({
        "quantity": [2, 3, -1],
        "price": [100, 200, 50],
        "sale_date": [
            "2026-01-01",
            "2026-01-02",
            "2026-01-03"
        ]
    })

    cleaner = SalesDataCleaner()

    result = cleaner.clean_data(df)

    assert len(result) == 2

    assert result["total_amount"].tolist() == [
        200,
        600
    ]

