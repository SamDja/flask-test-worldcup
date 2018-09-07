from flask import Flask, render_template, send_from_directory, request
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
    select = request.form.get('first_team')
    return str(select)

@app.route('/css/<path:path>')
def serve_css(path):
    return send_from_directory('css', path)

@app.route('/assets/<path:path>')
def serve_assets(path):
    return send_from_directory('assets', path)

# if __name__=="__main__":
#     app.run(host='0.0.0.0', port='80')