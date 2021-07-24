# FACE DETECTION AND RECOGNITION
## Abstract
At first instance it is going to be detected faces and eyes using **OpenCV**, and then using *Machine Learning* technics, it is going to be trained a *Neural Network* with a face dataset. Finally, a small dataset of several people will be introduced into the *NN* for detecting that people and tag them with a idetifier.

## Objetives
1. Detect eyes and faces.
2. Create and train a NN with a big dataset.
3. Introduce a small dataset of several people.
4. Detect that several people.

## Implementation of *face_recognition.py*
The implementation is as the following figure shows:
<img src="https://github.com/alrodsa/face_recognition/blob/main/diagrams/face_recognitionv1.0.png">

There are 3 possible ways to detect and recognize faces:
- Image mode -> ```python3 face_recognition.py -i image_path```
- Video mode -> ```python3 face_recognition.py -v video_path```
- Camera mode -> ```python3 face_recognition.py -c camera_id```

There is an special option for saving the result in a new file; using the option **-s** as it is shown in the following command:
- ```python3 face_recognition.py -s [-i image_path | -v video_path | -c camera_id]```
