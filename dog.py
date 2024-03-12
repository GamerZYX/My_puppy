from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api', methods=['POST'])
def my_api():
    data = request.json
    # 处理data
    response = {"message": "Message Received", "yourData": data}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
