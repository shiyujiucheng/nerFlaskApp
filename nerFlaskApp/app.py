from flask import Flask, request
from utils import load_model
from ast import literal_eval
from flask import request, render_template
import json
app = Flask(__name__)
crf_model = load_model('ckpts/crf.pkl')
def sentencessplit(str):
    # 发送过来字符串预处理
    sentences = []
    sentences.append(list(str))
    return sentences

@app.route('/nerapi', methods=['POST',])
def nerapi():
    if request.method == 'GET':
        return "<h1>error</h1>"
    else:
        sentence = request.form.get('sentences')

        print("sentence:"+sentence)
        lists = sentencessplit(sentence)
        # lists = literal_eval(sentences["sentences"])
        result = crf_model.test(lists)
        return render_template('index.html', result = zip(result[0],list(sentence)))


@app.route('/', methods=['GET',])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
