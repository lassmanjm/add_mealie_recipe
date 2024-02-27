from flask import Flask, render_template, request, jsonify
from PIL import Image
from extract_recipe_text import extract_recipe


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_image():
    if 'image' not in request.files:
        return jsonify({'message': 'No image provided'}), 400

    image_file = request.files['image']
    if image_file.filename == '':
        return jsonify({'message': 'No image selected'}), 400

    try:
        # Process the image using your Python script
        recipe = extract_recipe(image_file)

        # Send the save path in the response
        return jsonify({'message': 'Image processed successfully', 'recipe': recipe})
    except Exception as e:
        return jsonify({'message': 'Error processing image: %s'%(str(e))}, 500)

if __name__ == '__main__':
    app.run(debug=True)
