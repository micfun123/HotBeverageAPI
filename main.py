import imp
from urllib import response
from fastapi import FastAPI
from fastapi.responses import FileResponse , StreamingResponse,JSONResponse ,RedirectResponse
import os
import random

app = FastAPI(
    title = "HotBeverageAPI",
    description="Gets a HotBeverage from the database",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)


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
def teajson():
    x = "teacuppics/{}".format(getRandomFile("teacuppics"))
    return FileResponse(x)

@app.get("/json/tea")
def tea():
    return JSONResponse(content={'teacuppics': getRandomFile("teacuppics")})

@app.get("/coffee")
def coffee():
    x = "coffeecups/{}".format(getRandomFile("coffeecups"))
    return FileResponse(x)

@app.get("/json/coffee")
def coffeejson():
    return JSONResponse(content={'coffeecups': getRandomFile("coffeecups")})


   
