import cv2

def save_img(img, name = 'img_dummy.jpg'):
    img_dummy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    cv2.imwrite(name, img_dummy)