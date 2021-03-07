import graphene
from fastapi import FastAPI
from src.customgraphqlapp import CustomGraphQLApp

from src.schema import Query


app = FastAPI()

app.add_route('/graphql', CustomGraphQLApp(schema=graphene.Schema(query=Query)))


@app.get('/')
def ping():
    return {'ping': 'pong'}
