class FinalDataLoader:

    def __init__(self, connection):
        self.connection = connection

    def load_data(self, df):

        cursor = self.connection.cursor()

        query = """
        INSERT INTO final_sales
        (
            sale_id,
            customer_id,
            product_id,
            quantity,
            price,
            sale_date,
            total_amount,
            customer_name,
            email,
            city
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for _, row in df.iterrows():

            values = (
                int(row["sale_id"]),
                row["customer_id"],
                row["product_id"],
                int(row["quantity"]),
                float(row["price"]),
                row["sale_date"].date(),
                float(row["total_amount"]),
                row["customer_name"],
                row["email"],
                row["city"]
            )

            cursor.execute(query, values)

        self.connection.commit()

        cursor.close()

        print("Final data loaded successfully")