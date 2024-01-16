import psycopg2 as psycopg2
from psycopg2 import sql
from config import dbname, user, password, host, port, table_name


class PostgresConnector:
    def __init__(self):
        self.table_name = table_name
        self.connection = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port,
        )
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def get_data_by_id(self, id):
        try:
            query = sql.SQL(f"SELECT * FROM {table_name} WHERE id = %s;").format(sql.Identifier(self.table_name))
            self.cursor.execute(query, (id,))
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            self.close_connection()

    def delete_data_by_id(self, id):
        try:
            query = sql.SQL(f"DELETE FROM {table_name} WHERE id = %s;").format(sql.Identifier(self.table_name))
            self.cursor.execute(query, (id,))
            self.connection.commit()
            print(f"Row with id={id} deleted successfully.")
        except Exception as e:
            self.connection.rollback()
            print(f"Error: {e}")
        finally:
            self.close_connection()