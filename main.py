from sqlite3 import connect, Connection, Cursor
from services.auth_service import register, login
from services.admin_service import adminMenu
from database.db_setup import ensureSchema


def main() -> None:
    """App entry: opens DB, ensures schema, shows menu."""
    conn: Connection = connect(".database.db")
    cursor: Cursor = conn.cursor()
    ensureSchema(conn, cursor)

    while True:
        print()
        print("1. Register")
        print("2. Login")
        print("3. Admin")
        print("4. Exit")

        try:
            choice: str = input("Enter your choice: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if choice == "1":
            register(conn, cursor)
        elif choice == "2":
            login(conn, cursor)
        elif choice == "3":
            adminMenu(conn, cursor)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()


if __name__ == "__main__":
    main()
