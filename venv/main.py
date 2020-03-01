from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def send_js():
    return app.send_static_file('home.html')

@app.route('/bootstrap.css')
def send_css():
    return app.send_static_file('bootstrap.css')

@app.route('/handle_data',methods=['POST'])
def my_form_post(s):
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

if __name__ == "__main__":
    app.run(port=9876)