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
      decoded = html_decode(query)
      # # Our search engine broke, we found no results :-(
      message = "Sorry, no results were found for <b>" + decoded + "</b>."
      message += " <a href='?'>Try again</a>."

    return render_template("./index.html", message=message)

def html_decode(message):
    """
    Returns the ASCII decoded version of the given HTML string. This does
    NOT remove normal HTML tags like <p>.
    """
    decoded = ""
    htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
        )
    for char in message:
      for code in htmlCodes:
        if char in code:
          char = char.replace(char, code[1])
      decoded += char

    return decoded

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True, port=5000)
