import sqlite3
from datetime import datetime

# --- Database Setup ---
def init_db():
    """Creates a fresh database and table."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            description TEXT
        )
    """)
    # Clearing the table so running the script multiple times doesn't duplicate data
    cursor.execute("DELETE FROM expenses") 
    conn.commit()
    conn.close()

# --- Core Functions ---
def process_batch_expenses():
    """Loops through hardcoded data and inserts it into the SQLite database."""
    
    # --- HARDCODED INPUTS ---
    transactions = [
        {"category": "Groceries", "amount": 45.50, "description": "Weekly grocery run"},
        {"category": "Transport", "amount": 15.00, "description": "Uber to the office"},
        {"category": "Rent", "amount": 1200.00, "description": "Monthly apartment rent"},
        {"category": "Entertainment", "amount": 60.00, "description": "Video game purchase"},
        {"category": "Utilities", "amount": 95.20, "description": "Electric and Water bill"}
    ]
    
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    # Emojis removed to prevent Jenkins Unicode errors
    print("Processing automated transactions...\n")
    
    for item in transactions:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute(
            "INSERT INTO expenses (date, category, amount, description) VALUES (?, ?, ?, ?)",
            (date, item["category"], item["amount"], item["description"])
        )
        print(f"Logged: {item['category']} - ${item['amount']:.2f}")

    conn.commit()
    conn.close()
    print("\nBatch insertion complete!\n")

def view_expenses():
    """Fetches and displays all expenses from the database."""
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()

    print("--- Database Record ---")
    print(f"{'ID':<5} | {'Date':<19} | {'Category':<15} | {'Amount':<10} | {'Description'}")
    print("-" * 75)
    
    total = 0
    for row in rows:
        total += row[3]
        print(f"{row[0]:<5} | {row[1]:<19} | {row[2]:<15} | ${row[3]:<9.2f} | {row[4]}")
    
    print("-" * 75)
    print(f"Total Expenditure: ${total:.2f}\n")

# --- Main Application Execution ---
def main():
    init_db()                   
    process_batch_expenses()    
    view_expenses()             

if __name__ == "__main__":
    main()
