from flask import Flask, render_template, request
import qrcode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/makeQR', methods=['POST', 'GET'])
def make():
    output = request.form.to_dict()
    toMake = output['data']
    qr = qrcode.make(toMake)
    qr.save('static/somename.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)