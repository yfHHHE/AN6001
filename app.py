from flask import Flask
from flask import render_template, request
import textblob
import google.generativeai as gnai

app = Flask("__name__")

@app.route("/",methods=['GET','POST'])
def index():
    return (render_template("index.html"))

@app.route("/main",methods=['GET','POST'])
def main():
    name = request.form.get("q")
    return (render_template("main.html"))

@app.route("/SA",methods=['GET','POST'])
def SA():
    return (render_template("sa.html"))

@app.route("/SA_result",methods=['GET','POST'])
def SA_result():
    q = request.form.get("q")
    r = textblob.TextBlob(q).sentiment
    return (render_template("sa_result.html",r=r))

@app.route("/AI",methods=['GET','POST'])
def AI():
    return (render_template("ai.html"))

@app.route("/AI_result",methods=['GET','POST'])
def AI_result():
    q = request.form.get("q")
    api = 'AIzaSyDMGJl5TE73oqQ7UWOqaE4Z1TPpHNfjjPM'
    gnai.configure(api_key=api)
    model = gnai.GenerativeModel("gemini-1.5-flash")
    r = model.generate_content(q)
    r = r.candidates[0].content.parts[0].text
    return (render_template("ai_result.html",r=r))
if __name__ == '__main__':
    app.run()
