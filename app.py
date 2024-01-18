from flask import Flask, render_template, request, flash, redirect, url_for, session
import sqlite3
from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline

app = Flask(__name__)

tokenizer = AutoTokenizer.from_pretrained("dslim/bert-base-NER")
model = AutoModelForTokenClassification.from_pretrained("dslim/bert-base-NER")
nlp = pipeline("ner", model=model, tokenizer=tokenizer)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    results = ""
    resultsClear = {
        "names": [],
        "places": [],
        "organisations": []
    }
    if request.method == 'POST':
        text = request.form['text']
        results = nlp(text)
        for word in results:
            if word['entity'] in ['B-PER', 'I-PER']:
                resultsClear["names"].append(word['word'])
            elif word['entity'] in ['B-LOC', 'I-LOC']:
                resultsClear["places"].append(word['word'])
            elif word['entity'] in ['B-ORG', 'I-ORG']:
                resultsClear["organisations"].append(word['word'])
    return render_template('index.html', names=resultsClear["names"], places=resultsClear["places"], organisations=resultsClear["organisations"])


if __name__ == "__main__":
    app.run(debug=True)
