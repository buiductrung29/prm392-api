import strawberry
import uvicorn
from strawberry.fastapi import GraphQLRouter
from src.data.data_connection import book_test, select, connection
import nest_asyncio
from pyngrok import ngrok
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.schema.type import Author as AuthorType
from src.data.models import Author
from fastapi.staticfiles import StaticFiles


@strawberry.type
class User:
    name: str
    age: int


@strawberry.type
class Query:
    @strawberry.field
    def user(self) -> User:
        return User(name="Patrick", age=100)

    @strawberry.field
    def author(self) -> AuthorType:
        return Author(id="bd65600d-8669-4903-8a14-af88203add38",name="Trung")
    # @strawberry.field
    # def getBook() -> typing.List[Book]:
    #     return [
    #         Book(id=1, title="Book 1", desc="This is description of book 1", short_desc="Short description 1", published_time="2022-02-02", authors=[1, 2, 3, 4]),
    #     ]
    
    # @strawberry.field
    # def testAlchemy() -> typing.List[Book]:
    #     test = select([book_test.columns.Id, book_test.columns.Title])
    #     return connection.execute(test).fetchall()


schema = strawberry.Schema(query=Query)


app = FastAPI()

# origins = ["http://localhost:8005"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")

# static files provider
app.mount("/static", StaticFiles(directory="static"), name="static")

# set ngrok authtoken
ngrok.set_auth_token("20BzVd4WAfXYNMabTCKMXQNvTXM_2hhJrgpZU4AFbFyYUrDgk")
ngrok_tunnel = ngrok.connect(8005)
print("Public URL: ", ngrok_tunnel.public_url)
nest_asyncio.apply()

# update static path for random ngrok url

#define static folders
# with open("static\\text.txt", "w+") as f:
#     f.write(ngrok_tunnel.public_url)
#     f.close()

uvicorn.run(app, port=8005)