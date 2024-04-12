
from flask import Flask, request, jsonify
import threading
from spiders.product_description_spider import scrape
from data_cleaner import clean_text_data
from desc_gen import generate_summary
import subprocess
from werkzeug.serving import make_server
import shutil
import os


app = Flask(__name__)


@app.route('/summarize', methods=['POST'])
def summarize():
    print("hi")
    url = request.form['url']
    scrape(url)
    cw = os.getcwd()
    fd = os.path.join(cw,'scraped_data')
    for file in os.listdir(fd):
        fs = os.path.join(fd,file)
    cleaned_data = clean_text_data(fs)
    # run a shell command: python keyword_model.py
    loc = os.path.join(cw,'keybert_model.pkl')
    if not os.path.exists(loc):
        subprocess.run(['python', 'keyword_model.py'])
    summary = generate_summary(cleaned_data['full_text'])
    if os.path.exists(fd):
        shutil.rmtree(fd)
    return summary


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
