import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import cv2
import time

if __name__ == "__main__":
    
    model = load_model("./best_weights.hdf5")
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        res = cv2.resize(frame, (224, 224), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
        img = img_to_array(res)

        img = img / 255
        img = np.expand_dims(img,axis=0)

        answer = model.predict(img)
        print(answer)
        start_point = (0, 0)
        end_point = (100, 100)
        c = (255, 0, 0)
        thickness = -1

        if answer[0][0] > 0.85:
            print("The image belongs to Recycle waste category")
            color = (200, 0, 0)
        elif answer[0][0] > 0.25:
            print("The image belongs to Trash waste category")
            c = (0, 0, 200)
        else:
            print("The image belongs to Organic waste category ")
            c = (0, 200, 0)

        
        frame = cv2.rectangle(frame, start_point, end_point, c, thickness)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()

