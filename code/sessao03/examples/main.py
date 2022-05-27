from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.get("/blog/{id}")
async def show(id: int):
    # fecth blog with id = {id}
    return {"data": f"Blog N° {id}"}


@app.get("/blog")
async def index(limit: int, published: bool):
    if published:
        return {"data": f"{limit} published on DB"}
    else:
        return {"data": f"{limit} unpublished on DB"}

# here we are testing functions of Method POST() + class Python


@app.post("/blog")
async def createBlog(req: Blog):
    return {"data": f"This blog contain: One {req.title}, One {req.body} and a optional status call {req.published}"}


"""
EXPLICAÇÃO RAPIDA:

a nossa Classe 'Blog' possui os 3 atributos que compõem o nosso objeto 'blog'. 

Sempre que formos adicionar ou alterar um blog, será baseado na estrutura de:

1 - Title
2 - Body
3 - Published

--> A proposito, o código está em inglês pois, o tutorial que peguei era todo em inglês! 
(E deu preguiça na hora de traduzir para PT-BR)
"""
