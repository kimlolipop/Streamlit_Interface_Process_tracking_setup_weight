import streamlit as st
from streamlit_cropper_edit import st_cropper
from PIL import Image
import cv2
import numpy as np
import time

def crop(status):
    if status == 1:
        realtime_update = st.sidebar.checkbox(label="Update in Real Time", value=True)
        box_color = st.sidebar.color_picker(label="Box Color", value='#0000FF')
        aspect_choice = st.sidebar.radio(label="Aspect Ratio", options=["Free","1:1", "16:9", "4:3", "2:3"])
        aspect_dict = {"1:1": (1,1),
                    "16:9": (16,9),
                    "4:3": (4,3),
                    "2:3": (2,3),
                    "Free": None}
        
        
        aspect_ratio = aspect_dict[aspect_choice]
        img = Image.open('img_dummy.jpg')

        if not realtime_update:
            st.write("Double click to save crop")
            
        # Get a cropped image from the frontend
        cropped_img, coordinate, ratio1, ratio2 = st_cropper(img, 
                                                             realtime_update=realtime_update,
                                                             box_color=box_color,
                                                             aspect_ratio=aspect_ratio)
        st.write(coordinate)
        st.write(ratio1, ratio2)


        # Manipulate cropped image at will
        st.write("Preview")
        _ = cropped_img.thumbnail((250,250))
        st.image(cropped_img)

    return status, coordinate




def preview_img_subtraction(coordinate, raw_frame, mask_frame, 
                            HIDE_button, method):
    
    x = round(coordinate[0])
    y = round(coordinate[1])

    w = round(coordinate[2] - coordinate[0])
    h = round(coordinate[3] - coordinate[1]) 


    curr_frame = st.empty()    
    col1, col2, col3, col4 = st.beta_columns(4)
    stframe1 = col1.empty()
    stframe2 = col2.empty()


    for i in range(len(raw_frame)):
        if HIDE_button:
            break
        #pre process
        img = raw_frame[i]
        mask = mask_frame[i]

        img_crop = img[y:y+h, x:x+w]
        mask_crop = mask[y:y+h, x:x+w]


        #visulize
        curr_frame.text(i)
        stframe1.image(img_crop)
        stframe2.image(mask_crop)
        time.sleep(0.05)
        
        
            
def preview_color_mask(coordinate, raw_frame, lower_color, upper_color, 
                       HIDE_button, method):
    

    x = round(coordinate[0])
    y = round(coordinate[1])

    w = round(coordinate[2] - coordinate[0])
    h = round(coordinate[3] - coordinate[1]) 


    curr_frame = st.empty()    
    col1, col2, col3, col4 = st.beta_columns(4)
    stframe1 = col1.empty()
    stframe2 = col2.empty()


    for i in range(len(raw_frame)):
        if HIDE_button:
            break
        #pre process
        HLS = cv2.cvtColor(raw_frame[i], cv2.COLOR_BGR2HLS)
        mask = cv2.inRange(HLS ,lower_color, upper_color)
        
        
        img = raw_frame[i]
        img_crop = img[y:y+h, x:x+w]
        mask_crop = mask[y:y+h, x:x+w]


        #visulize
        curr_frame.text(i)
        stframe1.image(img_crop)
        stframe2.image(mask_crop)
        time.sleep(0.05)

    
    