from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Function to generate folder name based on user input
def create_folder_name(answers):
    # Replace empty answers with 'XXX' and format the folder name
    answers = [answer if answer else "XXX" for answer in answers]
    folder_name = "_".join(answers).upper().replace(' ','')
    return folder_name

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Collect form data
        answers = [
            request.form.get('Modelo'),
            request.form.get('Litragem'),
            request.form.get('Potencia'),
            request.form.get('Ano'),
            request.form.get('Transmissao'),
            request.form.get('Placa'),
            request.form.get('Cliente')
        ]
        # Generate the folder name
        folder_name = create_folder_name(answers)
        return jsonify({'folder_name': folder_name})

    # Render the HTML template for GET requests
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
