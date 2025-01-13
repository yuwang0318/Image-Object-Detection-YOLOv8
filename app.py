from flask import Flask, render_template, request, jsonify
import os
from ultralytics import YOLO

app = Flask(__name__)
# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  
# Define the upload folder
UPLOAD_FOLDER = os.path.join(app.static_folder, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            return jsonify({'error': 'No image provided'}), 400

        image_file = request.files['image']
        image_path = os.path.join(UPLOAD_FOLDER, image_file.filename)
        image_file.save(image_path)
        print(f"Image saved at: {image_path}")  # Debug: Print image save path
        
        # Run object detection with error handling
        try:
            # Generate a new filename for the annotated image
            new_filename = 'annotated_' + image_file.filename

            # Run object detection and save with the new filename
            results = model(image_path, save=True, project=UPLOAD_FOLDER, name='annotated', exist_ok=True)
            
            # Get the path of the original annotated image
            # original_annotated_path = os.path.join(UPLOAD_FOLDER, image_file.filename)

            # Generate the path for the renamed annotated image
            new_annotated_path = os.path.join(UPLOAD_FOLDER, 'annotated', image_file.filename)
            rename_annotated_path = os.path.join(UPLOAD_FOLDER, 'annotated', new_filename)
            
            # Rename the annotated image
            os.rename(new_annotated_path, rename_annotated_path)
            print("Before saving annotated image")  # Debug: Print before saving            
            print("Before saving annotated image")
            
            # Check if the file actually exists after saving            
            if os.path.exists(new_annotated_path):
                print(f"Annotated image saved at: {new_annotated_path}")
            else:
                print(f"Error: Annotated image not found at: {new_annotated_path}")
            
            image_url = f'/static/uploads/annotated/{new_filename}'  # URL of annotated image

            return jsonify({'imageUrl': image_url})
        except Exception as e:
            # Log the error for debugging
            print(f"Error during object detection: {e}") 
            # Return a more specific error to the front-end
            return jsonify({'error': f'Error detecting objects: {str(e)}'}), 500  
       
    return render_template('index.html')  # Serve the HTML template

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app in debug mode