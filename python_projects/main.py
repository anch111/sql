import sqlite3
//
con = sqlite3.connect('db.sqlite')

cur = con.cursor()

# query_1 = '''
# CREATE TABLE IF NOT EXISTS directors(
#     id INTEGER PRIMARY KEY,
#     full_name TEXT,
#     birth_year INTEGER
# );
# '''

# query_2 = '''
# CREATE TABLE IF NOT EXISTS video_products(
#     id INTEGER PRIMARY KEY,
#     title TEXT,
#     product_type TEXT,
#     release_year INTEGER
# );
# '''

# query = '''
#     INSERT INTO video_products(id, title, product_type, release_year)
#     VALUES (1, 'Весёлые мелодии', 'Мультсериал', 1930);'''
    
# cur.execute(
#     'INSERT INTO video_products VALUES(?, ?, ?, ?);',
#     (2, 'Долгая прогулка', 'Фильм', 2025)
# )

# directors = [
#     (1, 'Текс Эйвери', 1908),
#     (2, 'Роберт Земекис', 1952),
#     (3, 'Джерри Чиникей', 1912)
# ]

# video_products = [
#     (3, 'Злое', 'Фильм', 2021),
#     (4, 'Кто подставил кролика Роджера', 'Фильм', 1988),
#     (5, 'Безумные мелодии Луни Тюнз', 'Мультфильм', 1931),
#     (6, 'Розовая пантера: Контроль за вредителями', 'Мультфильм', 1969),
    
# ]

# cur.executemany('INSERT INTO directors VALUES(?, ?, ?);', directors)
# cur.executemany('INSERT INTO video_products VALUES(?, ?, ?, ?);', video_products)

results = cur.execute('''
    SELECT title,
    release_year
FROM video_products
WHERE (release_year BETWEEN 1930 AND 1970) AND product_type LIKE '%ильм';
''')

for result in results:
    print(result)

con.commit()

con.close()






