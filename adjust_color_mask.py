import streamlit as st
from PIL import Image
import numpy as np
import cv2
import time

# st.title("Adjust Color Range Mask")
# st.sidebar.title('Navigation')
# method = st.sidebar.radio('Go To ->', options=['Color', 'none'])

def adjust_color(status):
    
    if status == 1:

        opencv_image = cv2.imread('img_adjust_color_mask.jpg')
        im = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2RGB)
        HLS = cv2.cvtColor(opencv_image, cv2.COLOR_BGR2HLS)
        col1, col2 = st.beta_columns(2)

    #     col1.header('Lower')
        l_H = col1.slider( 'lower_Hue',0, 180, 0)
        # st.write('Values:', l_H)
        l_L = col1.slider( 'lower_Luminance',0, 255, 0)
        # st.write('Value:', l_L)
        l_S = col1.slider( 'lower_Saturation',0, 255, 0)
        # st.write('Valus:', l_S)

    #     col2.header('Upper')
        u_H = col2.slider( 'upper_Hue',0, 180, 180)
        # st.write('Values:', l_H)
        u_L = col2.slider( 'upper_Luminance',0, 255, 255)
        # st.write('Value:', l_L)
        u_S = col2.slider( 'upper_Saturation',0, 255, 255)
        # st.write('Valus:', l_S)

        lower_color = np.array([l_H, l_L, l_S])
        upper_color = np.array([u_H, u_L, u_S])
        mask = cv2.inRange(HLS ,lower_color, upper_color)

        col3, col4 = st.beta_columns(2)

        col3.header('Real')
        col3.image(im,channels="RGB")

        col4.header('Color Mask')
        col4.image(mask)
    return status, lower_color, upper_color, mask




def Render_Color_mask(lower_color, upper_color, frame, break_button_mask):
#     st.write(lower_color, upper_color)
#     st.write(frame)


    curr_frame = st.empty()    
    col3, col4 = st.beta_columns(2)
    stframe3 = col3.empty()
    stframe4 = col4.empty()

    
    for i in range(len(frame)):
        
        
        if break_button_mask:
            break
        
        HLS = cv2.cvtColor(frame[i], cv2.COLOR_BGR2HLS)
        mask = cv2.inRange(HLS ,lower_color, upper_color)
        curr_frame.text(i)

        stframe3.image(frame[i])
        stframe4.image(mask)
#         fame = fame + 1
        time.sleep(0.05)
        
    
    
