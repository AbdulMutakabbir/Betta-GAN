import cv2
import os


def get_image_list_from_directory(directory):
    return os.listdir(directory)


original_image_path = "Cropped_Betta_V1"
image_list = get_image_list_from_directory(original_image_path)

print(image_list)

for i in range(3):
    print(image_list[i])
    img = cv2.imread(original_image_path + os.sep + image_list[i])
    img = cv2.resize(img,(600,600))
    cv2.imwrite(original_image_path + os.sep + image_list[i] + "___2.jpg",img)
    # cv2.imshow("img",img)


