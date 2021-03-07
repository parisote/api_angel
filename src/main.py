import graphene
from fastapi import FastAPI, Response
from fastapi.responses import RedirectResponse
from src.customgraphqlapp import CustomGraphQLApp
from src.schema import Query
from mimetypes import guess_type
from os.path import isfile
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.add_route('/graphql', CustomGraphQLApp(schema=graphene.Schema(query=Query)))

app.mount("/doc/schema", StaticFiles(directory="doc/schema"), name="doc")


@app.get('/')
def ping():
    return RedirectResponse("/doc/schema/index.html")


@app.get("/doc/schema/{filename}")
async def get_site(filename):
    filename = './doc/schema/' + filename

    if not isfile(filename):
        return Response(status_code=404)

    with open(filename) as f:
        content = f.read()

    content_type, _ = guess_type(filename)
    return Response(content, media_type=content_type)


@app.get("/doc/schema/")
async def get_site_default_filename():
    return await get_site('index.html')
