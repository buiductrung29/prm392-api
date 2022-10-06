from click import echo
from sqlalchemy import create_engine, MetaData, Table, select, Column, Integer, String, true
engine = create_engine("sqlite:///Bookaholic.db", echo=True)
# print(engine)
meta = MetaData()
connection = engine.connect()
# worker = Table(
#     "Books",meta,
#     Column("Id", Integer, primary_key=True),
#     Column("Title", String)
# )
# meta.create_all(engine)



book_test = Table("Books", meta, autoload=False)