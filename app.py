from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# Route untuk menyajikan index.html dari lokasi root
@app.route('/')
def home():
    return send_from_directory('.', 'index.html')

# Route untuk menghitung ekspresi
@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Ambil ekspresi dari request
        data = request.get_json()
        expression = data.get('expression', '')

        # Evaluasi ekspresi
        result = eval(expression)

        # Cek apakah hasil genap atau ganjil
        if result % 2 == 0:
            message = "I LOVE U"
        else:
            message = "I MISS U"

        return jsonify({'result': message})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
