import sqlite3

conn = sqlite3.connect("attractions.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS attractions (
    city TEXT PRIMARY KEY,
    name TEXT,
    image TEXT,
    maps TEXT
)
""")

data = [

("cumbria",
"Lake District National Park",
"",
"https://www.google.com/maps/search/Lake+District+National+Park"),

("corfe castle",
"Corfe Castle",
"",
"https://www.google.com/maps/search/Corfe+Castle"),

("the cotswolds",
"Bibury Village",
"",
"https://www.google.com/maps/search/Bibury+Cotswolds"),

("cambridge",
"Cambridge Botanic Garden",
"",
"https://www.google.com/maps/search/Cambridge+Botanic+Garden"),

("bristol",
"Clifton Suspension Bridge",
"",
"https://www.google.com/maps/search/Clifton+Suspension+Bridge"),

("oxford",
"Oxford Castle",
"",
"https://www.google.com/maps/search/Oxford+Castle"),

("norwich",
"Norwich Cathedral",
"",
"https://www.google.com/maps/search/Norwich+Cathedral"),

("stonehenge",
"Stonehenge",
"",
"https://www.google.com/maps/search/Stonehenge"),

("watergate bay",
"Watergate Bay Beach",
"",
"https://www.google.com/maps/search/Watergate+Bay"),

("birmingham",
"Birmingham Museum and Art Gallery",
"",
"https://www.google.com/maps/search/Birmingham+Museum+and+Art+Gallery")

]

cursor.executemany("INSERT OR REPLACE INTO attractions VALUES (?,?,?,?)", data)

conn.commit()
conn.close()

print("Database updated (images removed).")