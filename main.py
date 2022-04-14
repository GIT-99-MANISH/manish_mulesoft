import sqlite3

# Connect to the database (new/existing)
db = sqlite3.connect('mydb.db')
cursor = db.cursor()

movies = [
    {'title': 'ramleela', 'year': 2014, 'director': 'sanjay leela bansali', 'actor': 'ranveer singh', 'actress': 'deepika'},
    {'title': 'sultan', 'year': 2016, 'director': 'ALi abbas zafar', 'actor': 'salman khan', 'actress': 'anushka sharma'},
    {'title': 'bahubali', 'year': 2015, 'director': 'ss rajamouli', 'actor': 'prabhas', 'actress': 'tammanah'},
    {'title': '3 idiots', 'year': 2009, 'director': 'rk hirani', 'actor': 'amir khan', 'actress': 'kareena kapoor'},
    {'title': 'taare zameen par', 'year': 2007, 'director': 'amole gupte', 'actor': 'amir khan', 'actress': 'none'},
    {'title': 'bajrangi bhaijaan', 'year': 2015, 'director': 'kabir khan', 'actor': 'salman khan', 'actress': 'kareena kapoor'},
    {'title': 'newton', 'year': 2017, 'director': 'amit', 'actor': 'rajkumar rao', 'actress': 'anjali patil'}
]

# Creating table 'Movies'
cursor.execute("CREATE TABLE Movies12 (title VARCHAR(60), actor VARCHAR(24), actress VARCHAR(24), year INT(4), director VARCHAR(24));")

# Inserting data into the table
for movie in movies:
    cursor.execute(f"INSERT INTO Movies VALUES (\'{movie['title']}\', \'{movie['actor']}\', \'{movie['actress']}\', {movie['year']}, \'{movie['director']}\');")

# Select all movies
print("\nSelect all movies:")
cursor.execute("SELECT * FROM Movies;")
for i in cursor.fetchall():
    print(i)
print("\n")

# Select all movies with the actor 'amir khan'
print("Select all movies with the actor 'amir khan':")
cursor.execute("SELECT title, year, director FROM Movies WHERE actor='amir khan';")
for i in cursor.fetchall():
    print(i)
print("\n")


# Printing the table in a dataframe
# import pandas as pd
# print(pd.read_sql("SELECT * FROM Movies;", db),end="\n\n")
# print(pd.read_sql("SELECT title, year, director FROM Movies WHERE actor='amir khan';", db))