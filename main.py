import cv2
from deepface import DeepFace
from retinaface import RetinaFace
import numpy as np
import pyfirmata2

board = pyfirmata2.Arduino('COM4')

# Setup PWM pins for LED intensity control
red_led = board.get_pin('d:11:p')
green_led = board.get_pin('d:10:p')

def normalize(emotion_dict):
    total = sum(emotion_dict.values())
    return {k: v / total for k, v in emotion_dict.items()}

crowd_emotions = []
violence_weights = {
    'angry': 0.9,
    'fear': 0.6,
    'disgust': 0.7,
    'sad': 0.3,
    'happy': -0.5,
    'surprise': 0.2,
    'neutral': 0.0
}

def violence_score(emotion_probs):
    return sum(emotion_probs[emotion] * violence_weights.get(emotion, 0.0) for emotion in emotion_probs)

# Thresholds
individual_risk_threshold = 0.5  # Above this, individual is considered high risk
crowd_trigger_ratio = 0.3        # If 30% or more of the crowd is high-risk, crowd is violent

def predict():
  if (len(crowd_emotions)>0):
    normalized_crowd = [normalize(person) for person in crowd_emotions]
    individual_scores = [violence_score(person) for person in normalized_crowd]
    high_risk_count = sum(score > individual_risk_threshold for score in individual_scores)
    crowd_risk_ratio = high_risk_count / len(individual_scores)

    crowd_is_violent = crowd_risk_ratio >= crowd_trigger_ratio

    print("Crowd violence probability:", crowd_risk_ratio)
    print("Crowd is violent?" , crowd_is_violent)
    return crowd_is_violent
  return false


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

video_capture = cv2.VideoCapture(0)

while True:
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_roi = frame[y:y+h, x:x+w]
        try:
            # analysis = DeepFace.analyze(face_roi, actions=['age', 'gender', 'emotion'], silent=True)
            analysis = DeepFace.analyze(face_roi, actions=['emotion'], silent=True)
            if analysis:
                # age = analysis[0]['age']
                # gender = analysis[0]['dominant_gender']
                emotion = analysis[0]['dominant_emotion']
                emotion_probabilites = analysis[0]['emotion']

                # text = f"{gender}, {age}, {emotion}"
                crowd_emotions.append(emotion_probabilites)
                text = f"{emotion}"
                cv2.putText(frame, text, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        except ValueError as e:
            print(f"Error analyzing face: {e}")
            continue

    # Set LED colors based on the detected emotion
    crowd_is_violent = predict()
    if crowd_is_violent:
        red_led.write(1)
        green_led.write(0)
    else:
        red_led.write(0)
        green_led.write(1)

    cv2.imshow('Real-time Multiple Face Detection', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()