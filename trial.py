from fastapi import FastAPI, File, Form, UploadFile,status,Response

app = FastAPI()

name_json={"name":"Rishabh","city":"noida","state":"UP"}


@app.get("/name_data")
def func():
    return name_json