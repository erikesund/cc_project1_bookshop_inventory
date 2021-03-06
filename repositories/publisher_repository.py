from db.run_sql import run_sql
from models.publisher import Publisher
from models.book import Book

def save(publisher):
  sql = "INSERT INTO publishers(name, address, phone_number) VALUES ( %s, %s, %s) RETURNING id"
  values = [publisher.name, publisher.address, publisher.phone_number]
  results = run_sql(sql, values)
  id = results[0]['id']
  publisher.id = id
  return publisher

def select_all():
  publishers = []
  sql = "SELECT * FROM publishers"
  results = run_sql(sql)
  for row in results:
    publisher = Publisher(row["name"], row["address"], row["phone_number"], row["id"])
    publishers.append(publisher)
  return publishers

def select(id):
  publisher = None
  sql = "SELECT * FROM publishers WHERE id = %s"
  values = [id]
  result = run_sql(sql, values)[0]  
  
  if result is not None:
    publisher = Publisher(result["name"], result["address"], result["phone_number"], result["id"])
  return publisher

def update(publisher):
  sql = "UPDATE publishers SET (name, address, phone_number) = (%s, %s, %s ) WHERE id = %s"
  values = [publisher.name, publisher.address, publisher.phone_number, publisher.id]
  run_sql(sql, values)


def delete(id):
  sql = "DELETE FROM publishers WHERE id = %s"
  values = [id]
  run_sql(sql, values)

def books_by_publisher(id):
  books = []
  sql = "SELECT books.* FROM books WHERE publisher_id = %s"
  values = [id]
  publisher = id
  results = run_sql(sql, values)
  for row in results:
    book = Book(row["title"], row["author"], row["genre"], row["quantity"], row["buy_price"], row["sell_price"], publisher, row["isbn"], row["book_format"], row["id"])
    books.append(book)
  return books

def delete_all():
  sql = "DELETE FROM publishers"
  run_sql(sql)
