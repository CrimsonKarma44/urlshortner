from flask import Flask, render_template, request, redirect, url_for
from utility.jsonMan import jsonDelete, JsonReader, JsonSaver, jsonCopy
from utility.construct import construct
from models.urls import Url

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def displayUrl():
   '''
   Displays the url... Acts like the home page
   '''
   if request.method == 'POST':
      # newData = construct(url=request.form['url'], alias=request.form['alias'])
      newData = Url(url=request.form['url'], alias=request.form['alias']).constructJson()
      JsonSaver(newData=newData)
         
   data = JsonReader()
   return render_template("home.html", context=data)


@app.route("/delete/<alias>")
def deleteUrl(alias):
   ''' Deletes saved url'''
   jsonDelete(alias=alias)
   return redirect(url_for('displayUrl'))

@app.route("/copy/<alias>")
def copyUrl(alias):
   '''Copies url from saved url alias'''
   jsonCopy(alias=alias)
   return redirect(url_for('displayUrl'))

if __name__ == "__main__":
   app.run(debug=True)