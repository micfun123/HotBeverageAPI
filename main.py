import imp
from urllib import response
from fastapi import FastAPI
from fastapi.responses import FileResponse , StreamingResponse
import os
import random

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

def getRandomFile(path):
  """
  Returns a random filename, chosen among the files of the given path.
  """
  files = os.listdir(path)
  index = random.randrange(0, len(files))
  return files[index]



@app.get("/")
async def home():
  return RedirectResponse("/docs")

@app.get("/tea")
def tea():
    x = "teacuppics/{}".format(getRandomFile("teacuppics"))
    return FileResponse(x)

@app.get("/coffee")
def tea():
    x = "coffeecups/{}".format(getRandomFile("coffeecups"))
    return FileResponse(x)


   
