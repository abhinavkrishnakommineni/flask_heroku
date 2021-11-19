from flask import Flask, request,render_template
from werkzeug.utils import secure_filename
import pandas as pd
from cpsp import codescdv
app = Flask(__name__)
# class col():
#     inputfiletext : 'str'
@app.route('/')
def index():
    return render_template('form.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['inputFile']
    result = codescdv(inputfiletext=file)
    return result
    # file = request.files['inputFile']
    # filename = secure_filename(file.filename)
    # file.save(filename)
    # df = pd.read_csv(filename)
    #return  df
if __name__ == '__main__':
    app.run(debug=True)