from flask import flask
app = Flask(_name_)

@app.get("/")
def home() :
    return {"message" : "DevOps CI/CD is working!"}
    