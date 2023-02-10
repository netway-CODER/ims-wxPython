""" Unfinished file of nwxp.db.
    Use for an abstract class of all model classes.
    """

import sqlite3


class Manager:
    def __init__(self):
        self.file_name = "db.sqlite3"
        self.table_name = ""

    def fetch_query(self, query):
        conn = sqlite3.connect(self.file_name)
        try:
            with conn:
                result = conn.execute(query)
                return result.fetchall()
        except Exception as e:
            print("Error: {}".format(e))
        conn.close()

    def execute_query(self, query):
        conn = sqlite3.connect(self.file_name)
        try:
            with conn:
                conn.execute(query)
        except Exception as e:
            print("".format(e))
        conn.close()

    def all(self):
        query = "SELECT * FROM {}".format(self.table_name)
        return self.fetch_query(query)

    def count(self):
        all_records = self.all()
        return len(all_records)

    def get(self, columns):
        query = "SELECT {} FROM {}".format(columns, self.table_name)
        return self.fetch_query(query)

    def add(self, **kwargs):
        query = "INSERT INTO {} ({}) VALUES({})".format(self.table_name, kwargs.keys(), kwargs.values())
        self.execute_query(query)