import json

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse

app = FastAPI()

@app.get("/image/{image_description}")
async def get_image(image_description: str):
  img = "![Yellow Circle](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAxMDAgMTAwIiB3aWR0aD0iMTAwIiBoZWlnaHQ9IjEwMCI+PHRpdGxlPlllbGxvdyBDaXJjbGU8L3RpdGxlPjxjaXJjbGUgY3g9IjUwIiBjeT0iNTAiIHI9IjUwIiBmaWxsPSJ5ZWxsb3ciIC8+PC9zdmc+)"
  return JSONResponse(content=img, status_code=200)
  

@app.get("/logo.png")
async def plugin_logo():
  return FileResponse('logo.png')

@app.get("/.well-known/ai-plugin.json")
async def plugin_manifest(request: Request):
  host = request.headers['host']
  with open("ai-plugin.json") as f:
    text = f.read().replace("PLUGIN_HOSTNAME", f"https://{host}")
  return JSONResponse(content=json.loads(text))

if __name__ == "__main__":
  import uvicorn
  uvicorn.run(app, host="0.0.0.0", port=5002)