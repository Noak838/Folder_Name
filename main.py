import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to generate folder name based on user input
def create_folder_name(answers):
    answers = [answer if answer != "" else "XXX" for answer in answers]
    folder_name = "_".join(answers).upper().replace(' ','')
    return folder_name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        answers = [
            request.form.get('Modelo'),
            request.form.get('Litragem'),
            request.form.get('Potencia'),
            request.form.get('Ano'),
            request.form.get('Transmissão'),
            request.form.get('Placa'),
            request.form.get('Cliente')
        ]
        folder_name = create_folder_name(answers)
        return jsonify({'folder_name': folder_name})

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Use the PORT provided by Heroku or default to 8080
    app.run(host='0.0.0.0', port=port, debug=True)
