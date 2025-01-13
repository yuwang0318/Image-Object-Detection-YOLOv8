# Image Object Detection with YOLOv8

This project demonstrates object detection using the YOLOv8 model within a Flask web application. Users can upload an image, and the application will process it to detect and highlight objects using YOLOv8.

## Features

- Real-time object detection using YOLOv8.
- User-friendly web interface for image uploading and result display.
- Saves annotated images for review.

## Getting Started

1. **Clone the repository:**
2. **Install dependencies:**
   - Install the required libraries:
     !pip flask==2.3.2
     !pip ultralytics==8.0.124
3. **Download the YOLOv8 model weights:**
    - You can download the pre-trained YOLOv8 weights from the official Ultralytics website or use the provided `yolov8n.pt` in the repository.
4. **Run the application:**
5. **Access the web interface:**
   Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Usage

1. Upload an image using the file input.
2. Click the "Detect Objects" button.
3. The application will process the image and display the annotated result.

## Example

**Original Image:**

![Capture](https://github.com/user-attachments/assets/f5b98ac1-7f4e-493b-b215-7d56b8951b38)


**Processed Image:**

![image](https://github.com/user-attachments/assets/b5915b8a-c7a2-4b7e-aad5-eb11b7a22bff)

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [Ultralytics YOLO] for the YOLOv8 model
