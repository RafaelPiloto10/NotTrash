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
        res = np.zeros((224, 224))
        res = cv2.resize(frame, (224, 224), fx=0, fy=0, interpolation = cv2.INTER_CUBIC)
        img = img_to_array(res)

        img = img / 255
        img = np.expand_dims(img,axis=0)

        answer = model.predict(img)
        start_point = (frame.shape[1] // 3, frame.shape[0] * 3 // 4)
        end_point = (frame.shape[1] * 2 // 3, frame.shape[0] * 9 // 10)


        c = (255, 0, 0)
        thickness = -1
        category = ""

        if answer[0][0] > 0.85:
            color = (200, 0, 0)
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
        cv2.imshow('Resized', res)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1) & 0xFF == ord('b'):
            _, f = cap.read()
            background = f



    cap.release()
    cv2.destroyAllWindows()

