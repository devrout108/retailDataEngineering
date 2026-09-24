import pandas as pd

from database import DatabaseConnection
from data_cleaner import SalesDataCleaner
from final_loader import FinalDataLoader
from loguru import logger
from mysql.connector.errors import IntegrityError


db = None

try:

    # 1. Read sales CSV
    sales_df = pd.read_csv(
        "data/input/sales.csv"
    )

    logger.info("Sales data loaded successfully")


    # 2. Clean sales data
    cleaner = SalesDataCleaner()

    cleaner.profile_data(sales_df)

    sales_df = cleaner.clean_data(sales_df)

    logger.info("Sales data cleaning completed successfully")


    # 3. Connect to MySQL
    db = DatabaseConnection()

    connection = db.connect()

    logger.info("Connected to MySQL successfully")


    # 4. Read customer data from MySQL
    customer_df = pd.read_sql(
        "SELECT * FROM customers",
        connection
    )

    logger.info("Customer data loaded successfully")


    # 5. Merge sales and customer data
    final_df = pd.merge(
        sales_df,
        customer_df,
        on="customer_id",
        how="left"
    )

    logger.info("Sales and customer data merged successfully")


    # 6. Display final data
    print("\n========== FINAL DATA ==========")

    print(final_df)

    print("\nFinal Columns:")
    print(final_df.columns.tolist())

    print("\nMissing Values:")
    print(final_df.isnull().sum())

    logger.info("Final data validation completed successfully")


    # 7. Load final data into MySQL
    loader = FinalDataLoader(connection)

    try:

        loader.load_data(final_df)

        logger.info(
            "Final data loaded into MySQL successfully"
        )

    except IntegrityError as e:

        logger.error(
            "Database integrity error: {}",
            e
            
        )

    except Exception as e:

        logger.exception(
            "Unexpected error while loading final data: {}",
            e
        )


except Exception as e:

    logger.exception(
        "Pipeline failed: {}",
        e
    )


finally:

    if db is not None:
        db.close()

        logger.info(
            "Database connection closed"
        )