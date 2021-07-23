import cv2
import sys
import time
'''
    Execution:
        python3 basic_recognition -i path_image
        python3 basic_recognition -v path_video
        python3 basic_recognition -c camera_id 
'''

#Trained face detector file
face_detector = cv2.CascadeClassifier('detection_models/frontal_face_detection_trained.xml')

#Trained face detector file
eyes_detector = cv2.CascadeClassifier('detection_models/eyes_detection_trained.xml')

'''
    Function that detects eyes in a frame, it returns True if there are 2 or more
    eyes in the crop, in other case it return False and eyes are not drawn
'''
def eyes_detection(frame,x,y,w,h):
    #Detect eyes in crop image
    eyes = eyes_detector.detectMultiScale(frame)
    num_eyes = 0

    #Check if there is 2 o more eyes in the crop
    if len(eyes) >= 2:
        #For each eye
        for xe,ye,we,he in eyes:
            num_eyes += 1
            if num_eyes < 3:
                #Draw a rectangle around the eye
                cv2.rectangle(frame,(xe,ye),(xe+we,ye+he),(255,0,0),2)
        return True
                    
    return False

'''
    Funtion that detects faces in a frame
'''
def facial_detection(frame):
    #Convert image to gray scale 
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #Detection of faces in the image
    faces = face_detector.detectMultiScale(gray, 1.1, 4)

    #Draw a rectangle around the faces
    for x,y,w,h in faces:
        #First frame is cropped in faces
        crop = frame[y:y+h,x:x+w]
        #cv2.imshow(f'Crop {x,y}', crop)
        
        #If there are 2 or more eyes in the crop
        if eyes_detection(crop,x,y,w,h) == True:
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    return frame

'''
    Function for detecting and recognize faces in a image
'''
def image_recognition(file):
    #Open the file
    img = cv2.imread(file, 1)

    #Call to function for detecting faces
    img = facial_detection(img)

    #Render image with detected faces 
    cv2.imshow(f'Detected faces in image <{file}>', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

'''
    Function for detecting and recognize faces in a video
'''
def video_recognition(file):
    try:
        #Load the video
        video = cv2.VideoCapture(file)

        #For each frame of the video
        while True:
            #Read a frame and if it is the end of the video
            ret, frame = video.read()

            if not ret:
                print('[INFO] Exiting video, end of video...')
                break

            #Call to function for detecting faces
            frame = facial_detection(frame)

            #Render the image with the faces detected    
            cv2.imshow(f'Detecting faces on video <{video}>', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('[INFO] Exiting video, q key pushed...')
                break

        video.release()
        cv2.destroyAllWindows()
    except:
        print(f'[ERROR] Cannot load video {file}...')

def camera_recognition(camera_id):
    try:
        #Load camera
        cam = cv2.VideoCapture(int(camera_id))

        while True:
            #Read a frame and if it is the end of the video
            ret, frame = cam.read()

            if not ret:
                print('[INFO] Exiting camera, streaming end...')
                break

            #Call to function for detecting faces
            frame = facial_detection(frame)

            #Render the image with the faces detected
            cv2.imshow(f'Camera <{camera_id}>', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('[INFO] Exiting camera, q key pushed...')
                break
        
        cam.release()
        cv2.destroyAllWindows()
    except:
        print(f'[ERROR] Cannot load camera {camera_id}...')

def main(option,path):
    if option == '-i':
        image_recognition(path)
    if option == '-v':
        video_recognition(path)
    if option == '-c':
        camera_recognition(path)

if __name__ == "__main__":
    print("Argumentos" + str(sys.argv))
    if len(sys.argv) > 2:
        param = sys.argv[-2]
        param2 = sys.argv[-1]

        if param not in ['-i','-v','-c']:
            print("[ERROR] Only -i, -v or -c params are accepted...")
        else:
            if param == '-i':
                img = cv2.imread(param2, 1)
                if img.any() == None:
                    print(f'[ERROR] Cannot load image {param2}...')
                else:
                    print(f'[INFO] IMAGE RECOGNITION -> {param} + {param2}')
                    cv2.destroyAllWindows()
                    main(param,param2)
                    
            if param == '-v':
                main(param,param2)
                '''img = cv2.VideoCapture(param2)
                if img == None:
                    print(f'[ERROR] Cannot load video {param2}...')
                else:
                    print(f'[INFO] VIDEO RECOGNITION -> {param} + {param2}')
                    cv2.destroyAllWindows()
                    main(param,param2)
                '''
            if param == '-c':
                print(f'[INFO] CAMERA RECOGNITION -> {param} + {param2}')
                cv2.destroyAllWindows()
                main(param,param2)
    else:
        print("Execution:\n\tpython3 basic_recognition -i path_image\n\tpython3 basic_recognition -v path_video \n\tpython3 basic_recognition -c camera_id")
