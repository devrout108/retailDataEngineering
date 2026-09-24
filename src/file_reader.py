import pandas as pd

from data_cleaner import SalesDataCleaner
from database import DatabaseConnection
from data_loader import SalesDataLoader


file_path = "data/input/sales.csv"


# 1. Read CSV
df = pd.read_csv(file_path)

print("CSV file loaded successfully")


# 2. Create cleaner
cleaner = SalesDataCleaner()


# 3. Profile data
cleaner.profile_data(df)


# 4. Clean data
cleaned_df = cleaner.clean_data(df)


print("\nCleaned Data:")
print(cleaned_df)


# 5. Connect to MySQL
db = DatabaseConnection()

connection = db.connect()


# 6. Load data into MySQL
loader = SalesDataLoader(connection)

loader.load_data(cleaned_df)


# 7. Close connection
db.close()