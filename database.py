import sqlite3

conn = sqlite3.connect('movie_chatbot.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS dialogues (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        character TEXT,
        dialogue TEXT
    )
''')
conn.commit()
conn.close()
print("Database and table created successfully.")
