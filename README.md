# Machine Learning Repository

Welcome to this comprehensive Machine Learning repository! This collection contains a wide variety of machine learning projects, algorithms, and implementations ranging from basic concepts to advanced applications including AI + IoT (AIOT) projects.

## 📚 Table of Contents

- [Machine Learning A-Z Course](#machine-learning-a-z-course)
- [AI + IoT Projects](#ai--iot-projects)
- [Standalone ML Projects](#standalone-ml-projects)
- [Jupyter Notebooks](#jupyter-notebooks)
- [MATLAB Implementations](#matlab-implementations)
- [Computer Vision Projects](#computer-vision-projects)
- [NVIDIA Deep Learning Institute](#nvidia-deep-learning-institute)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Contributing](#contributing)

## 🎓 Machine Learning A-Z Course

The [`Machine Learning A-Z (Codes and Datasets)`](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/) directory contains a complete machine learning course organized into 10 comprehensive parts:

1. **[Part 1 - Data Preprocessing](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%201%20-%20Data%20Preprocessing/)** - Essential data preparation techniques
2. **[Part 2 - Regression](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%202%20-%20Regression/)** - Linear, polynomial, and advanced regression methods
3. **[Part 3 - Classification](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%203%20-%20Classification/)** - Various classification algorithms
4. **[Part 4 - Clustering](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%204%20-%20Clustering/)** - Unsupervised learning techniques
5. **[Part 5 - Association Rule Learning](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%205%20-%20Association%20Rule%20Learning/)** - Market basket analysis and recommendation systems
6. **[Part 6 - Reinforcement Learning](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%206%20-%20Reinforcement%20Learning/)** - Agent-based learning algorithms
7. **[Part 7 - Natural Language Processing](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%207%20-%20Natural%20Language%20Processing/)** - Text analysis and processing
8. **[Part 8 - Deep Learning](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%208%20-%20Deep%20Learning/)** - Neural networks and deep learning
9. **[Part 9 - Dimensionality Reduction](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%209%20-%20Dimensionality%20Reduction/)** - PCA, LDA, and other reduction techniques
10. **[Part 10 - Model Selection and Boosting](./Machine%20Learning%20A-Z%20(Codes%20and%20Datasets)/Part%2010%20-%20Model%20Selection%20and%20Boosting/)** - Advanced model optimization

## 🤖 AI + IoT Projects

The [`AIOT`](./AIOT/) directory contains exciting projects that combine Artificial Intelligence with Internet of Things:

### ESP32 Camera Object Detection
- **[ESP32-Cam-Object-Detection](./AIOT/ESP32-Cam-Object-Detection/)** - Real-time object detection using ESP32-CAM
- **[ESP32CamObjectDetection](./AIOT/ESP32CamObjectDetection/)** - Arduino code and implementation files

### Sensor Projects
- **[Infrared Sensor](./AIOT/infrared/)** - Arduino sketches for infrared sensing
- **[Ultrasonic Sensor](./AIOT/ultrasonic/)** - Distance measurement projects

## 🚀 Standalone ML Projects

### Voice-Enabled Applications
- **[Sentiment Analysis with Voice](./Sentiment%20Analyais%20with%20voice.py)** - Real-time sentiment analysis from speech input

```python
# Example: Voice sentiment analysis
import speech_recognition as sr
from textblob import TextBlob
from gtts import gTTS
```

- **[Virtual Assistant](./Virtual%20Assistant/)** - Complete virtual assistant implementation
- **[Random Choice with Voice](./Random%20Choice%20with%20voice/)** - Voice-controlled random selection tool

### Utility Projects
- **[Sketch Maker](./Sketch%20maker.py)** - Convert images to pencil sketches
- **[Audio Generator](./audio%20generator.py)** - Generate audio files programmatically
- **[Spam Script](./spam.py)** - Automated text generation tool

## 📊 Jupyter Notebooks

Interactive notebooks for hands-on learning:

- **[Logistic Regression](./logistic-regression.ipynb)** - Complete logistic regression implementation
- **[Multiple Linear Regression](./multiple_linear_regression.ipynb)** - Multi-variable regression analysis
- **[Principal Component Analysis (PCA)](./PCA.ipynb)** - Dimensionality reduction techniques
- **[Linear Algebra](./Linear%20Algebra.ipynb)** - Mathematical foundations
- **[Matrix Operations](./Matrix.ipynb)** - Matrix computations and operations
- **[Vectors](./vectors.ipynb)** - Vector mathematics and applications
- **[SMS Classification](./SMS%20Classification.ipynb)** - Text classification for SMS filtering
- **[Air Quality Analysis](./AIR%20Quality.ipynb)** - Environmental data analysis

## 🔢 MATLAB Implementations

The [`Matlab`](./Matlab/) directory contains various algorithm implementations in MATLAB:

### Regression Algorithms
- Linear regression implementations
- Newton's method for optimization
- Ridge regression

### Mathematical Operations
- Eigenvalue computations
- Matrix operations and decompositions
- Statistical distributions

```matlab
% Example: Linear regression in MATLAB
function [theta] = linearRegression(X, y)
    theta = (X' * X) \ (X' * y);
end
```

## 👁️ Computer Vision Projects

The [`opencv haarcascades`](./opencv%20haarcascades/) directory includes:

- **Face Detection** - Multiple Haar cascade classifiers for face detection
- **Eye Detection** - Eye tracking and detection algorithms
- **Full Body Detection** - Complete body recognition systems

### Available Haar Cascades
- Frontal face detection (multiple variants)
- Eye detection (left/right eye specific)
- Smile detection
- Full body and upper/lower body detection

## 🧠 NVIDIA Deep Learning Institute

The [`NVIDIA DLI`](./NVIDIA%20DLI/) directory contains materials from NVIDIA's Deep Learning Institute:

- **[MNIST Classification](./NVIDIA%20DLI/01_mnist.ipynb)** - Handwritten digit recognition
- **[ASL Recognition](./NVIDIA%20DLI/02_asl.ipynb)** - American Sign Language classification
- **[CNN for ASL](./NVIDIA%20DLI/03_asl_cnn.ipynb)** - Convolutional neural networks
- **[Data Augmentation](./NVIDIA%20DLI/04a_asl_augmentation.ipynb)** - Improving model performance
- **[Doggy Door Project](./NVIDIA%20DLI/05a_doggy_door.ipynb)** - Practical computer vision application
- **[Headline Generator](./NVIDIA%20DLI/06_headline_generator.ipynb)** - Natural language generation

## 🚀 Getting Started

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Avishek8136/Machine-Learning.git
   cd Machine-Learning
   ```

2. **Set up your environment:**
   ```bash
   # For Python projects
   pip install -r requirements.txt  # If available
   
   # Common dependencies
   pip install numpy pandas matplotlib scikit-learn tensorflow opencv-python
   ```

3. **For AIOT projects:**
   - Install Arduino IDE for ESP32 projects
   - Set up ESP32 board configuration
   - Install required Arduino libraries

4. **For MATLAB projects:**
   - Ensure MATLAB is installed with required toolboxes
   - Navigate to the [`Matlab`](./Matlab/) directory

## 📋 Requirements

### Python Dependencies
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- TensorFlow/Keras
- OpenCV
- SpeechRecognition
- TextBlob
- PyAutoGUI

### Hardware Requirements (for AIOT projects)
- ESP32-CAM module
- Infrared sensors
- Ultrasonic sensors
- Appropriate connecting cables and breadboards

### Software Requirements
- Python 3.7+
- MATLAB (for MATLAB implementations)
- Arduino IDE (for ESP32 projects)
- Jupyter Notebook/Lab

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Happy Learning!** 🎉 Explore the various projects and feel free to experiment with the code. Each directory contains specific implementations that you can run and modify according to your needs.