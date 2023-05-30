import io
import socket
import struct
import time
from PIL import Image
import cv2
import numpy
import sys
import mediapipe as mp
from send import send_warning

ip = '10.100.42.109'
port = 8001


server_socket = socket.socket()
server_socket.bind((sys.argv[1], int(sys.argv[2])))  
server_socket.listen(0)
print("Listening")
connection = server_socket.accept()[0].makefile('rb')

face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

start_time = time.time()
eyes_visible = True
eyes_open = True
y_previous = 0  # Initialize y_previous

try:
    img = None
    while True:
        image_len = struct.unpack('<L', connection.read(struct.calcsize('<L')))[0]
        if not image_len:
            break
        image_stream = io.BytesIO()
        image_stream.write(connection.read(image_len))
        image_stream.seek(0)
        image = Image.open(image_stream)
        frame = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)

        rgb_face = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_face)
        landmarks_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        
        if landmarks_points:
            landmarks = landmarks_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                right = [landmarks[374], landmarks[386]]
                for landmark in right:
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0), -1)
                    
                left = [landmarks[145], landmarks[159]]
                for landmark in left:
                    x = int(landmark.x * frame_w)
                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

            start_time = time.time()
            eyes_visible = True
            
            if abs(y - y_previous) < 10:  # Check if y-coordinate of the eye is stable (closed)
                if eyes_open:
                    eyes_open_start_time = time.time()  # Start timer for closed eyes
                    eyes_open = False
                else:
                    elapsed_closed_time = time.time() - eyes_open_start_time  # Calculate elapsed time with eyes closed
                    if elapsed_closed_time >= 2:
                        print("Warning: Eyes closed for over 10 seconds!")
                        send_warning(ip, port)
            else:
                eyes_open = True
                
            y_previous = y
        
        else:
            # Eyes are not visible, check if the time threshold has been reached
            elapsed_time = time.time() - start_time
            if elapsed_time >= 2 and eyes_visible:
                print("Warning: Eyes not visible for 10 seconds!")
                eyes_visible = False
                send_warning(ip, port)
                
        cv2.imshow('Video', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyAllWindows()
finally:
    connection.close()
    server_socket.close()