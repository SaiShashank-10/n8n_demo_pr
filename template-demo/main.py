from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Initialize Jinja2 templates
templates = Jinja2Templates(directory="templates")

@app.get("/messesges", response_class=HTMLResponse)
async def read_root(request: Request):
    # Context data passed to the template
    context = {"message": "Hello, World!"}
    return templates.TemplateResponse("index.html", {"request": request, **context})

@app.get("/messeges1/v1/", response_class=HTMLResponse)
async def read_root(request: Request):
    # Context data passed to the template
    context = {"message": "Hello, World!"}
    return templates.TemplateResponse("index.html", {"request": request, **context})

if __name__ == "__main__":
    print("Hello World")
