from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from parser import extract_functions

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):

    if not file.filename.endswith(".py"):
        return HTMLResponse("<h3>Please upload a .py file</h3>")

    content = await file.read()
    code = content.decode("utf-8")

    # STEP 3: Read file contents
    # STEP 4: Parse using AST
    functions = extract_functions(code)

    return templates.TemplateResponse("index.html", {
        "request": request,
        "functions": functions
    })
