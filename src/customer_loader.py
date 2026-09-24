class CustomerDataLoader:

    def __init__(self, connection):
        self.connection = connection

    def load_data(self, df):

        cursor = self.connection.cursor()

        query = """
        INSERT INTO customers
        (
            customer_id,
            customer_name,
            email,
            city
        )
        VALUES (%s, %s, %s, %s)
        """

        for _, row in df.iterrows():

            values = (
                row["customer_id"],
                row["customer_name"],
                row["email"],
                row["city"]
            )

            cursor.execute(query, values)

        self.connection.commit()

        cursor.close()

        print("Customer data loaded successfully")