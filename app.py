import os
from flask import Flask, render_template, request, redirect
from waitress import serve
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
        
          return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_file():
    text = "return want you want" # variable for returning
    file = request.files['audio_file']
    file.save(f"static/audio/{file.filename}")
    # process the file here



    # Delete the file after processing
    os.remove(f'static/audio/{file.filename}')
    return text
if __name__ == "__main__":
         
         serve(app, host="0.0.0.0", port=8080)
         app.run(debug=True)