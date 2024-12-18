from django.db import connection

class DataLoader:
    @staticmethod
    def execute_query(query: str) -> list[tuple]:
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()