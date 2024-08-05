# Indian Currency Detection 💲

This project leverages the power of the YOLOv10n model to detect and count Indian currency notes. It's designed to be an efficient and accurate solution for recognizing various denominations in real-time.

## Table of Contents 📑
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Details](#model-details)
- 
## Overview 📋

This project focuses on detecting and counting Indian currency notes using the YOLOv10n model, which is known for its efficiency in object detection tasks. The model is trained to recognize different denominations of Indian currency and can be deployed in various applications where automatic currency recognition is required.

## Features ✨
- **Real-time Currency Detection**: Detects and counts Indian currency notes in real-time.
- **Accurate Denomination Recognition**: Capable of distinguishing between various denominations.
- **Optimized for Speed**: Uses the lightweight YOLOv10n model for faster processing.

## Installation 🔧

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/indian-currency-counter.git
   cd indian-currency-counter
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the trained YOLOv10n model and place it in the `models/` directory.

## Usage 🚀

1. Prepare your images or video feed for currency detection.
2. Run the detection script:
   ```bash
   python detect_currency.py --source your-image-or-video --weights models/yolov10n.pt
   ```
3. The script will output the detected denominations along with their count.

## Model Details 🧠

- **Model**: YOLOv10n
- **Framework**: PyTorch
- **Trained on**: Custom dataset of Indian currency notes
- **Performance**: High accuracy with real-time detection capability
