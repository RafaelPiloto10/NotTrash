import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import cv2
import time
from communications import Communications
from database import request, count, update
from threading import Thread

if __name__ == "__main__":

    PORT = "/dev/cu.usbmodem11301"
    BAUDRATE = 9600
    
    model = load_model("./best_weights.hdf5")
    cap = cv2.VideoCapture(0)

    comms = Communications(PORT, BAUDRATE)
    comms.start()

    c = (255, 0, 0)

    while(True):
        ret, frame = cap.read()
        res = cv2.resize(frame, (224, 224), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
        img = img_to_array(res)

        img = img / 255
        img = np.expand_dims(img,axis=0)

        answer = model.predict(img)
        start_point = (frame.shape[1] // 3, frame.shape[0] * 3 // 4)
        end_point = (frame.shape[1] * 2 // 3, frame.shape[0] * 9 // 10)


        thickness = -1
        category = ""

        if answer[0][0] > 0.85:
            c = (200, 0, 0)
            category = "Recycle: {:.2f}% Confident".format(answer[0][0] * 100)
        elif answer[0][0] > 0.25:
            c = (0, 0, 200)
            category = "Landfill: {:.2f}% Confident".format(((answer[0][0] * 100) / 85) * 100)
        else:
            c = (0, 200, 0)
            category = "Organic: {:.2f}% Confident".format(100 - answer[0][0] * 100)

        # setup text
        font = cv2.FONT_HERSHEY_SIMPLEX

        # get boundary of this text
        textsize = cv2.getTextSize(category, font, 1, 2)[0]

        # get coords based on boundary
        textX = (frame.shape[1] - textsize[0]) // 2
        textY = (frame.shape[0] + textsize[1]) * 8 // 10 

        frame = cv2.rectangle(frame, start_point, end_point, c, thickness)
    
        # add text centered on image
        cv2.putText(frame, category, (textX, textY ), font, 1, (255, 255, 255), 2)


        cv2.imshow('Original', frame)

        if cv2.waitKey(30) & 0xFF == ord('q'):
            break
        
        if cv2.waitKey(30) & 0xFF == ord('g'):
            r, C, l = count(request())
            if c == (200, 0, 0):
                comms.writeline("R")
                t = Thread(target = update, args=(r, C, l, "R"))
                t.start()
                print("NEW RECYCLE ITEM ADDED")
            elif c == (0, 0, 200):
                comms.writeline("L")
                t = Thread(target = update, args=(r, C, l, "L"))
                t.start()
                print("NEW LANDFILL ITEM ADDED")
            elif c == (0, 200, 0):
                comms.writeline("O")
                t = Thread(target = update, args=(r, C, l, "O"))
                t.start()
                print("NEW ORGANIC ITEM ADDED")
            else:
                print("COULD NOT PARSE")

    cap.release()
    cv2.destroyAllWindows()

