import sqlite3

def insert_dialogue(character, dialogue):
    conn = sqlite3.connect('movie_chatbot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO dialogues (character, dialogue)
        VALUES (?, ?)
    ''', (character, dialogue))
    conn.commit()
    conn.close()

def parse_script():
    character = None
    dialogue = ""

    with open('iron_man_script.txt', 'r', encoding='ISO-8859-1') as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.isupper() and ':' in line:
                if character and dialogue:
                    insert_dialogue(character, dialogue.strip())
                character = line.split(':')[0].strip()
                dialogue = line.split(':')[1].strip()
            else:
                dialogue += " " + line

        if character and dialogue:
            insert_dialogue(character, dialogue.strip())

    print("Script parsing and data insertion completed.")

parse_script()
