from fastapi import FastAPI, Request
from fastapi.responses import FileResponse , RedirectResponse
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
import os
import random

app = FastAPI(
    title = "HotBeverageAPI",
    description="Gets a HotBeverage from the database. \n This what made by Michael twitter = https://twitter.com/Michaelrbparker ",
    version="0.1.0",
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT",
    },

)

app.mount("/static", StaticFiles(directory="static"), name="static")


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
    x = "static/teacuppics/{}".format(getRandomFile("static/teacuppics"))
    return FileResponse(x)


@app.get('/json/tea')
async def jsontea(request: Request) -> JSONResponse:
    img = "teacuppics/{}".format(getRandomFile("static/teacuppics"))
    img_url = request.url_for('static', path=img)
    return {'img_url': img_url}

@app.get("/coffee")
def coffee():
    x = "static/coffeecups/{}".format(getRandomFile("coffeecups"))
    return FileResponse(x)

@app.get("/json/coffee")
def coffeejson(request: Request) -> JSONResponse:
    img = "coffeecups/{}".format(getRandomFile("static/coffeecups"))
    img_url = request.url_for('static', path=img)
    return {'img_url': img_url}


   
