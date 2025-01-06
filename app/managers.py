import sqlite3
from models import Actor


class ActorManager:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("cinema.sqlite")
        self.table_name = "actors"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def create(
            self,
            first_name: str,
            last_name: str) -> None:
        self.connection.execute(
            f"INSERT INTO {self.table_name}(first_name, last_name) "
            f"VALUES (?, ?)",
            (first_name, last_name,)
        )
        self.connection.commit()

    def all(self) -> list[Actor]:
        actors_data_cursor = self.connection.execute(
            f"SELECT * from {self.table_name}"
        )
        return [Actor(*row) for row in actors_data_cursor]

    def update(
            self,
            id_to_update: int,
            new_first_name: str,
            new_last_name: str) -> None:
        self.connection.execute(
            f"UPDATE {self.table_name} "
            f"SET first_name = ?, "
            f"last_name = ? "
            f"WHERE id = ? ",
            (
                new_first_name,
                new_last_name,
                id_to_update
            )
        )
        self.connection.commit()

    def delete(self, id_to_delete: int) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
            f"WHERE id = ? ",
            (id_to_delete, )
        )
        self.connection.commit()

    def delete_all(self) -> None:
        self.connection.execute(
            f"DELETE FROM {self.table_name} "
        )
        self.connection.commit()
