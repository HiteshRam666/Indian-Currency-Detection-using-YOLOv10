import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLOv10


model = YOLOv10("best.pt")

def predict(image):
  image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  result = model.predict(source = image_rgb, imgsz = 640, conf = 0.25)
  annotated_img = result[0].plot()

  detections = result[0].boxes 

  annotated_img = annotated_img[:, :, :: -1]
  return annotated_img

app = gr.Interface(
    predict, 
    inputs = gr.Image(type = "numpy", label = "Upload an Image"),
    outputs = gr.Image(type = "numpy", label = "Predicted Image"),
    title = "Indian Coin Detections",
    description = "Upload an Image and the YOLOv10 will detect the coin"
)

app.launch()
