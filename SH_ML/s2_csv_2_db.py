import sqlite3
import csv

# Database setup
db_name = 'elements.db'
table_name = 'element_attributes'

# Connect to SQLite database (this will create the database if it doesn't exist)
conn = sqlite3.connect(db_name)
c = conn.cursor()

# Create table with an added 'element' column
c.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
            element TEXT,
            tag TEXT,
            id TEXT,
            type TEXT,
            class TEXT,
            name TEXT,
            aria_autocomplete TEXT,
            title TEXT,
            href TEXT,
            text TEXT,
            value TEXT,
            aria_label TEXT
            )''')

# Function to insert data from CSV to the database
def insert_data_from_csv(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        # Ensure 'element' is included in the fieldnames if not already present
        fieldnames = ['element'] + [name.replace('-', '_') for name in reader.fieldnames if name != 'element']
        for row in reader:
            # Map original row to a new one with modified keys, including 'element'
            row_with_underscores = {key.replace('-', '_'): value for key, value in row.items()}
            # Use the new row for the SQL query
            c.execute(f'''INSERT INTO {table_name} (element, tag, id, type, class, name, aria_autocomplete, title, href, text, value, aria_label)
                          VALUES (:element, :tag, :id, :type, :class, :name, :aria_autocomplete, :title, :href, :text, :value, :aria_label)''', row_with_underscores)
    conn.commit()

# Example usage
csv_file_path = 'elements.csv'  # The path to your CSV file. Adjust as needed.
insert_data_from_csv(csv_file_path)

# Close connection
conn.close()
