import cv2
import sys
import time
'''
    Execution:
        python3 basic_recognition -i path_image
        python3 basic_recognition -v path_video
        python3 basic_recognition -c camera_id 
'''

def image_recognition(file):
    try:
        img = cv2.imread(file, 1)
        cv2.imshow('Imagen', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print(f'[ERROR] Cannot load image {file}...')

def video_recognition(file):
    try:
        video = cv2.VideoCapture(file)
        while True:
            ret, frame = video.read()
            if not ret:
                print('[INFO] Exiting video, end of video...')
                break
            cv2.imshow('Video', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                print('[INFO] Exiting video, q key pushed...')
                break
        video.release()
        cv2.destroyAllWindows()
    except:
        print(f'[ERROR] Cannot load video {file}...')

def camera_recognition(camera_id):
    try:
        cam = cv2.VideoCapture(int(camera_id))
        while True:
            ret, frame = cam.read()
            if not ret:
                print('[INFO] Exiting camera, streaming end...')
                break
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
