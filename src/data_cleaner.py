import pandas as pd

from loguru import logger


class SalesDataCleaner:

    def profile_data(self, df):

        print("========== DATA PROFILE ==========")

        print("\nFirst 5 Records:")
        print(df.head())

        print("\nNumber of Rows:")
        print(len(df))

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

        logger.info("Sales data profiling completed successfully")

    def clean_data(self, df):

        print("\n========== DATA CLEANING ==========")

        df = df.drop_duplicates()

        logger.info("Duplicate records removed")

        df["quantity"] = pd.to_numeric(
            df["quantity"],
            errors="coerce"
        )

        df["price"] = pd.to_numeric(
            df["price"],
            errors="coerce"
        )

        df["quantity"] = df["quantity"].fillna(1)

        df["price"] = df["price"].fillna(
            df["price"].median()
        )

        logger.info("Missing quantity and price values handled")

        df["sale_date"] = pd.to_datetime(
            df["sale_date"],
            errors="coerce"
        )

        df = df[df["quantity"] > 0]

        df["total_amount"] = (
            df["quantity"] * df["price"]
        )

        logger.info("Total amount calculated successfully")

        logger.info("Data cleaning completed successfully")

       

        return df