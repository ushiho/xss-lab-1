#!/usr/bin/python3

from flask import Flask, request, url_for, render_template, redirect
from flask import Blueprint

app = Flask(__name__, template_folder='.', static_url_path='/static')


@app.route('/', methods=['GET'])
def home_xss():
    # query = request.form['query']
    if not request.args.get('query'):
      # Show main search page
      return render_template('./index.html')
    else:
      query = request.args.get('query', '[empty]')
       
      # Our search engine broke, we found no results :-(
      message = "Sorry, no results were found for <b>" + query + "</b>."
      message += " <a href='?'>Try again</a>."

    return render_template("./index.html", message=message)

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=5000)
