import streamlit as st
from PIL import Image
import numpy as np
import cv2

x = 20
h = 100
y = 40
w = 60

img = cv2.imread('img_dummy.jpg')
im = img[y:y+h, x:x+w]

st.image(img)
st.image(im)