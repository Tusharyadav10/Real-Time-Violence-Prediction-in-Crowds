# Violence Prediction in Crowds Using DeepFace and Real-Time LED Alert System with Arduino

This project aims to enhance public safety in crowded environments by combining deep learning-based facial emotion recognition with a real-time visual alert system. By detecting aggression-related emotions such as anger, fear, and disgust using the DeepFace framework, the system calculates the probability of violence and provides instant visual feedback using an Arduino-controlled LED alert mechanism.

## 📘 Project Description

Traditional surveillance systems rely heavily on manual monitoring, which is error-prone and delayed. This project introduces a proactive solution that integrates:

- **DeepFace** for facial emotion detection (7-class classification)
- **Mathematical violence prediction model**
- **Arduino UNO + LED system** for real-time alerting
- **FER-2013 & AffectNet datasets** for emotion classification
- **Python, OpenCV, and Arduino C++** for implementation

---

## 📄 Project Report & Research Paper

- 📑 [**Full Project Report (PDF)**](https://github.com/Tusharyadav10/Real-Time-Violence-Prediction-in-Crowds.git/ProjectIIIFinalReport.pdf)
<!-- - 📰 [**Research Paper (PDF)**](https://github.com/Tusharyadav10/Real-Time-Violence-Prediction-in-Crowds.git/ResearchPaper.pdf) -->

---

## 🛠️ Technologies Used

| Component              | Description                                |
|------------------------|--------------------------------------------|
| Deep Learning Library  | TensorFlow / Keras                         |
| Emotion Recognition    | DeepFace                                   |
| Programming Languages  | Python, Arduino C++                        |
| Hardware               | Arduino UNO, LEDs, Breadboard              |
| Computer Vision        | OpenCV                                     |
| Data Communication     | USB Serial Communication                   |
| IDEs                   | VS Code, Arduino IDE                       |

---

## 🚦 System Workflow

1. Capture live video using webcam.
2. Detect faces and classify emotional states using DeepFace.
3. Compute aggregated violence probability using a weighted scoring model.
4. Trigger visual alert via Arduino:
   - 🟥 Red LED → High aggression (potential violence)
   - 🟩 Green LED → Normal conditions

---

## 📊 Model Performance

| Model     | Accuracy (%) |
|-----------|--------------|
| DeepFace  | **96.9**     |
| ResNet50  | 92.8         |
| VGG19     | 91.8         |

---

## 📷 Snapshots

- 📈 Model Accuracy Progression Graphs
- 🔴🟢 Real-Time LED Alert System Hardware
- 🎥 System Workflow Diagrams

*(See `Chapter 4` of the report)*

---

## 🔐 Ethical Considerations

- Facial data processing is performed locally.
- No biometric data is stored.
- Privacy-respecting real-time alerting system.

---

## 🧠 Future Work

- Add multi-modal analysis (audio, posture).
- Enhance detection in low-light environments.
- Expand to cloud-based centralized monitoring.
- Introduce multi-camera and zone-wise analytics.

---

## 👥 Contributors

- Tushar Yadav  
- Ayaj Akhtar Ansari  
- Shubhechha Saha  
- Amar Mishra  
- Almamon Sk  

**Under the guidance of:**
- Dr. Pratima Chatterjee  
- Dr. Sahadeb Shit  
- Dr. Biru Rajak  

---

> 📌 *Submitted as partial fulfillment of B.Tech in CSE (Data Science) at Kazi Nazrul University, 2025*
