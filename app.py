from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def handle_message():
    data = request.json
    message = data['message']
    response = f"{message}"  # Simple echo response
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()