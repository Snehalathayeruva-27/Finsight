from datetime import date
import sqlite3

from matplotlib import category

def create_database():

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    # Users table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    # Expenses table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        expense_name TEXT,
        amount INTEGER,
        date TEXT,
        category TEXT,
        payment_mode TEXT,
        description TEXT
    )
    """)

    # Budgets table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS budgets(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        budget_name TEXT,
        amount INTEGER,
        category TEXT,
        start_date TEXT
    )
    """)
    # Income Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS income(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        income_name TEXT,
        amount INTEGER,
        date TEXT
    )
    """)
    # Investments Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS investments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        investment_name TEXT,
        investment_type TEXT,
        invested_amount REAL,
        current_value REAL,
        investment_date TEXT
    )
    """)
    # Goals Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS goals(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        goal_name TEXT,
        target_amount REAL,
        saved_amount REAL,
        target_date TEXT
    )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS download_history(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        report_type TEXT,
        download_date TEXT
    )
    """)
    cursor.execute("""
       CREATE TABLE IF NOT EXISTS savings(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    savings_name TEXT,
    amount REAL,
    category TEXT,
    date TEXT
)
""")
    
    conn.commit()
    conn.close()


create_database()