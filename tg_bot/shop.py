import sqlite3

conn = sqlite3.connect("shop.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
""")
conn.commit()

cur.execute("INSERT INTO products (name, price) VALUES ('RTX 3050', 25000)")
conn.commit()

cur.execute("SELECT * FROM products")
print(cur.fetchall())