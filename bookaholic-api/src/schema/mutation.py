import strawberry

@strawberry.type
class Mutation:
    @strawberry.mutation
    def register(self):
        pass

    @strawberry.mutation
    def login(self):
        pass