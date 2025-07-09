from flask import Flask, render_template, request, send_file
import json
from stock_pred_1 import risk_factor
from swing import risk_factor_swing
from news_analysis import analyze_sentiment
from mutual_web_scrap import web_scrap
from screen_shot import screen_shot
#from download_csv import download_csv

app = Flask(__name__)

# """with open ('config.json', 'r') as c:
#     params = json.load(c)["params"]
#     print(params)
# app.secret_key = 'super-secret-key'"""


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/stock")
def stock():
    return render_template('stock_pred.html')

@app.route("/stock_swing")
def stock_swing():
    return render_template('swing.html')

@app.route("/news_anlysis")
def news_analyis():
    return render_template('news_analysis.html')

@app.route("/web_scrap")
def web_scrap_grow():
    return render_template('web_scrap.html')

@app.route("/screen_shot")
def screen_shot_grow():
    return render_template('screen_shot.html')

@app.route("/stock_pred_page", methods=['POST'])
def stock_pred():
    if request.method == 'POST':
        entry = request.form.get('fname')
        exit = request.form.get('lname')
        
        entry_1,exit_1,quant, target,total_amount, risk = risk_factor(entry,exit)
        
        
    return render_template('charts_pred.html', entry_1=entry_1, exit_1=exit_1,quant=quant,target=target, total_amount=total_amount, risk=risk)


@app.route("/stock_pred_swing", methods=['POST'])
def stock_pred_swing():
    if request.method == 'POST':
        entry = request.form.get('fname')
        exit = request.form.get('lname')
        
        entry_1,exit_1,quant, target,total_amount, risk = risk_factor_swing(entry,exit)
        
        
    return render_template('charts_pred.html', entry_1=entry_1, exit_1=exit_1,quant=quant,target=target, total_amount=total_amount, risk=risk)

@app.route("/news_sentiment", methods=['POST'])
def news_sentiment():
    if request.method == 'POST':
        news = request.form.get('blog_content')
        
        news_analysis= analyze_sentiment(news)
        neg = news_analysis[0]
        neu = news_analysis[1]
        pos = news_analysis[2]
        over_all = news_analysis[3]
        
        
    return render_template('news_chart.html', news = news, neg= neg, neu = neu, pos = pos, over_all = over_all )

@app.route("/web_scarp_mutual", methods=['POST'])
def web_scarp_mutual():
    if request.method == 'POST':
        url = request.form.get('urls')
        output_file_new = url.split('/')[-1]

        output_file = output_file_new.replace('-', ' ')
        output_file = output_file.title()
        df = web_scrap(url)
        excel_file_path = f'output/{output_file_new}.csv'

        df.to_csv(excel_file_path, index=False)
        
        
    return render_template('web_scrap_chart.html', df=df, output_file=output_file,output_file_new=output_file_new)


@app.route("/screen_shot_download", methods=['POST'])
def screen_shot_download():
    if request.method == 'POST':
        name_company = request.form.get('urls')
        print(name_company)
        start = screen_shot(name_company)

        # output_file_new = url.split('/')[-1]

        # output_file = output_file_new.replace('-', ' ')
        # output_file = output_file.title()
        # df = web_scrap(url)
        # excel_file_path = f'output/{output_file_new}.csv'

        # df.to_csv(excel_file_path, index=False)
        
        
    return render_template('screen_shot.html')


@app.route("/download_csv/<filename>", methods=['GET'])
def download_csv(filename):
    
    file_path = f'output/{filename}'
    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)