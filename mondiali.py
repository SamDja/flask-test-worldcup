from flask import Flask, render_template, send_from_directory, request
from random import randint
app = Flask(__name__)
teams = [
    ('russia','Russia'),
    ('france','Francia'),
    ('croatia','Croazia'),
    ('mexico','Messico'),
    ('germany','Germania'),
 ]


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', teams=teams)

@app.route('/', methods=['POST'])
def index_form():
    team1 = request.form.get('first_team')
    team2 = request.form.get('second_team')

    winning_team = team1
    if randint(0,1):
        winning_team = team2

    return render_template('index.html', winning_team=str(winning_team))

@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)

@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('assets', path)

@app.route('/fonts/<path:path>')
def serve_fonts(path):
    return send_from_directory('fonts', path)

if __name__=="__main__":
    app.run(host='0.0.0.0', port='80')