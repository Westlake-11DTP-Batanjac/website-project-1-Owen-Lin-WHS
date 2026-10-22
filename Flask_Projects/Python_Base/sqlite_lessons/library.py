import sqlite3

conn=sqlite3.connect("school_library.db")
conn.row_factory=sqlite3.Row
#print("connected")
cursor=conn.cursor()
#print(cursor)

cursor.execute("SELECT * FROM books")
books=cursor.fetchall()
#print(books)

def add_book(conn):
    while True:
        title=input("Title: ")
        if title.strip()!='':
            author=input("Author: ")
            genre=input("Genre: ")
            year = int(input("Year published: ")) 
            pages = int(input("Pages: ")) 
            copies = int(input("Copies: ")) 
            cursor.execute("""INSERT INTO books 
            (title, author, genre, publication_year, pages, available_copies) 
            VALUES (?, ?, ?, ?, ?, ?)""", 
            (title, author, genre, year, pages, copies))
            conn.commit()
            break

#print(books[0][1])

#for title in books:
#    print(title["title"])

#one = cursor.fetchone()
#print(one)
#one = cursor.fetchone()
#print(one)

#for book in books:
#    print(f"{book["title"]} {book["author"]}({str(book["publication_year"])}) - {book["pages"]} pages")

#count=0
#for book in books:
#    if book["available_copies"]==0:
#        count+=1
#print(count)

#print(cursor.fetchall())

#for author in books:
#    print(author["author"])

#count=0
#page=0
#for book in books:
#    page+=book['pages']
#    count+=1
#print(page/count)

#long_page=0
#for book in books:
#    if book['pages']>long_page:
#        long_page=book['pages']
#print(long_page)

#titles=[]
#for book in books:
#    titles.append(book['title'])
#print(titles)

#cursor.execute("SELECT * FROM books WHERE genre = 'fantasy' ORDER BY pages DESC LIMIT 3")



#cursor.execute("""INSERT INTO books 
#    (title, author, genre, publication_year, pages, available_copies) 
#    VALUES (?, ?, ?, ?, ?, ?)""", 
#    ("Aue", "Becky Manawatu", "Fiction", 2019, 344, 2)) 
#print("Added") 
#conn.commit() 
#print(cursor.lastrowid)


add_book(conn)


conn.close()