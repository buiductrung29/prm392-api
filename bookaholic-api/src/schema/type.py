import strawberry


@strawberry.type
class Book:
    pass


@strawberry.type
class Author:
    id : str
    name : str