#fastapi
from fastapi import FastAPI
#langserve
import uvicorn 

from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser 

from langserve import add_routes


#essay_prompt 

e_prompt = ChatPromptTemplate.from_messages(
    [
        ("system","listen to user carefully"),
        ("user","write an essay of exact 100 words on topic{topic}")
    ]
)

#poem 
p_prompt = ChatPromptTemplate.from_template(
    """
    write a poem of exact 50 words
    on topic{topic}
    """
)

model = Ollama(model="llama2")

app = FastAPI(server="langserver",version=1.0)

add_routes(
    app,
    e_prompt|model,
    path="/essay"
)

add_routes(
    app,
    p_prompt|model,
    path="/poem"
)


uvicorn.run(app,host="localhost",port=8000)