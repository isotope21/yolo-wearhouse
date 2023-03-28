# import torch
# import cv2
# import json
# import easyocr
# import numpy as np
# import PIL
# from PIL import Image

# # image_path = input("Enter the path of the image file: ")

# def predict(image_path):
#     # Ask user for the path of the image


#     # Open the image using Pillow
#     img = Image.open(image_path)

#     # Show the image
#     # img.show()

#     # Model
#     device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#     path = r'D:\msc ai\qZense internship\Projects\ANPR\yolo\yolo_cust\yolo_cust\yolov7\runs\train\yolov7-custom3\weights\best.pt'
#     model = torch.hub.load("WongKinYiu/yolov7", "custom", f"{path}", trust_repo=True)
#     # model = torch.hub.load("WongKinYiu/yolov7","custom")

#     # Image
#     img = img

#     # Inference
#     results = model(img)

#     # r =results.pandas().xyxy[0]

#     # detections = model(img)  # where 'model' is the loaded YOLOv7 model and 'img' is the input image

#     # set confidence threshold
#     conf_thresh = 0.2
#     boxes = results.xyxy[0][results.xyxy[0][:, 4] > conf_thresh, :4]  # get boxes with confidence > conf_thresh

#     # type(results)

#     # detections = np.asarray(results)
#     # print(detections.pandas().xyxy[0])
#     box = tuple(boxes[0].tolist())  # convert NumPy array to tuple
#     cropped_image = img.crop(box)
#     # cropped_image = img.crop((boxes))# cropped_image

#     # Convert the image to a NumPy array
#     image_array = np.asarray(cropped_image)
#     #  Extract text from the cropped image using easyocr library
#     reader = easyocr.Reader(['en'])
#     result = reader.readtext(image_array, detail=0)
#     # print(result)

#     # A dictionary object to store the text
#     text_dict = {'text': result}

#     # Convert the dictionary object to a JSON string
#     json_string = json.dumps(text_dict)

#     # Print the JSON string
#     cropped_image.show()
#     return json_string


# # predict(image_path)
