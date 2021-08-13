import streamlit as st
from input_production import webcam_input, video_input_img_sub, video_input_color_mask
from croper import crop, preview_img_subtraction, preview_color_mask
from save_image import save_img
from adjust_color_mask import adjust_color, Render_Color_mask
import time
 # Sleep for 3 seconds


#=================State setup
# c_upload --> edit เพื่อให้สามารถ ทำงานหลาย ๆ ฟังก์ชั่น รวมถึงให้สามารถ อัพวิดีโอใหม่ได้
if 'current_time' not in st.session_state: # status upload or not
    st.session_state.current_time = 0

if 'c_upload' not in st.session_state: # status upload or not
    st.session_state.c_upload = False
    
if 'video_subtrack' not in st.session_state: # record video that skip frame 
    st.session_state.video_subtrack = []
    
if 'video_raw2' not in st.session_state: # record video that skip frame 
    st.session_state.video_raw2 = []
    
if 'img_mask' not in st.session_state: # record video that skip frame 
    st.session_state.img_mask = []
    
if 'video_raw' not in st.session_state: # record video that skip frame 
    st.session_state.video_raw = []
    
if 'no_frame' not in st.session_state: # number of frame in skip video
    st.session_state.no_frame = 0

if 'select_frame_crop' not in st.session_state: # create state name --> cnt
    st.session_state.select_frame_crop = 0
    
if 'select_frame_color_mask' not in st.session_state: # create state name --> cnt
    st.session_state.select_frame_color_mask = 0
#===========================

coordinate = 0
raw = []
lower_color, upper_color = 0, 0
c_upload = False
st.title("Indezy - Adjust Weight program")
st.sidebar.title('Navigation')
mode = st.sidebar.radio('Go To ->', options=['Video', 'Webcam', 'test'])
# st.sidebar.header('Options')
# s

if mode == 'Video':
    
    
    method = st.radio('Method ->', options=['Video Subtraction', 'Color Mask', 'All Methods'])
#     f = st.file_uploader("")
    
    
    # Video sybtraction=====================================================================
    if method == 'Video Subtraction':
        f = st.file_uploader("Video Subtraction")
        # Read Video   
        if st.session_state.c_upload == False:
            video = st.session_state.video_subtrack
            c_upload = st.session_state.c_upload
            video, frame_count, st.session_state.c_upload, no_frame, raw = video_input_img_sub(c_upload, f)

            st.session_state.video_subtrack = video
            st.session_state.no_frame = no_frame
            st.session_state.uploader = f
            st.session_state.video_raw = raw

        # Render Video and Action    
        if f is not None:


            if len(st.session_state.video_subtrack) > 0:
                # slide bar
                values = st.slider( 'Select a range of values',0, int(st.session_state.no_frame) - 1, 1)
                play_button = st.button('Play')

                # Visualize frame
                col1, col2 = st.beta_columns(2)
                stframe1 = col1.empty()
                stframe2 = col2.empty()
                
                # play Frame
                if play_button:
                    fame = 0
                    curr_frame = st.empty()
                    break_button_raw = st.button('STOP')
                    
                    for i in range(len(st.session_state.video_subtrack)):
                        
                        curr_frame.text(fame)
                        stframe1.image(st.session_state.video_subtrack[fame])
                        stframe2.image(st.session_state.video_raw[fame])
                        
                        st.session_state.current_time = fame
                        if break_button_raw:
                            break
                        
                        fame = fame + 1
                        time.sleep(0.05)

                else:
                    # Visualize frame
                    stframe1.image(st.session_state.video_subtrack[values])
                    stframe2.image(st.session_state.video_raw[values])
                
                st.write(st.session_state.current_time)

                # Select frame
                select_button = st.button('Select_subtrack')
                if select_button:
                    st.session_state.select_frame_crop = 1
                    save_img(st.session_state.video_raw[values])
                    

                if st.session_state.select_frame_crop == 1:
                    st.session_state.select_frame_crop, coordinate = crop(st.session_state.select_frame_crop)
                    
                    Preview_button_subtraction = st.button('Preview Subtraction')
                    if Preview_button_subtraction:
                        HIDE_button = st.button('HIDE')
                        preview_img_subtraction(coordinate, 
                                                st.session_state.video_raw, 
                                                st.session_state.video_subtrack, 
                                                HIDE_button, 
                                                method)
                    
                    
                    if st.session_state.select_frame_crop == 1:
                            clear_button = st.button('Clear_subtrack')
                            if clear_button:
                                st.session_state.select_frame_crop = 0
#                                 st.session_state.c_upload = False

    # End Video subtraction
    
    
    # Color Mask ================================================================================
    elif method == 'Color Mask':
        f = st.file_uploader("Color Mask")
        st.write('Color mask')
        # Read Video   
        if st.session_state.c_upload == False:
            video = st.session_state.video_raw2
            c_upload = st.session_state.c_upload
            video, frame_count, st.session_state.c_upload, no_frame = video_input_color_mask(c_upload, f)

            st.session_state.video_raw2 = video
            st.session_state.no_frame = no_frame
            st.session_state.uploader = f


        # Render Video and Action    
        if f is not None:


            if len(st.session_state.video_raw2) > 0:
                # slide bar
                values = st.slider( 'Select a range of values',0, int(st.session_state.no_frame) - 1, 1)
                play_button = st.button('Play')

                # Visualize frame
                stframe1 = st.empty()

                
                # play Frame
                if play_button:

                    fame = 0
                    curr_frame = st.empty()
                    break_button_raw2 = st.button('STOP')
                    for i in range(len(st.session_state.video_raw2)):
                        
                        curr_frame.text(fame)
                        stframe1.image(st.session_state.video_raw2[fame])
                        st.session_state.current_time = fame
                    
                        if break_button_raw2:
                            break
                            
                        fame = fame + 1
                        time.sleep(0.05)
                else:
                    # Visualize frame
                    stframe1.image(st.session_state.video_raw2[values])
                
                st.write(st.session_state.current_time)


                # Adjust Color Mask
                select_button_color_mask = st.button('Adjsut')
                if select_button_color_mask:
                    st.session_state.select_frame_color_mask = 1
                    save_img(st.session_state.video_raw2[values], 'img_adjust_color_mask.jpg')


                if st.session_state.select_frame_color_mask == 1:
                    st.session_state.select_frame_color_mask, lower_color, upper_color, st.session_state.img_mask = adjust_color(st.session_state.select_frame_color_mask)
                    
                    
                    # Play Mask
                    play_button_mask = st.button('Play_Mask')
                    if play_button_mask:
                        break_button_mask = st.button('BREAK')
                        Render_Color_mask(lower_color, upper_color, st.session_state.video_raw2,  break_button_mask)
                    
                    # Select frame
                    select_button = st.button('Select_mask')
                    if select_button:
                        st.session_state.select_frame_crop = 1
                        save_img(st.session_state.video_raw2[values])
#                         save_img(st.session_state.img_mask)



                    if st.session_state.select_frame_crop == 1:
                        st.session_state.select_frame_crop, coordinate = crop(st.session_state.select_frame_crop)
            
                        Preview_button_color_mask = st.button('Preview Mask')
                        if Preview_button_color_mask:
                            HIDE_button = st.button('HIDE')
                            preview_color_mask(coordinate, 
                                    st.session_state.video_raw2, 
                                    lower_color, 
                                    upper_color, 
                                    HIDE_button, 
                                    method)
                        
                        
                        if st.session_state.select_frame_crop == 1:
                            clear_button = st.button('Clear_mask')
                            if clear_button:
                                st.session_state.select_frame_crop = 0
#                                 st.session_state.c_upload = False
#                                 

    
    elif method == 'All Methods':
        st.write('all method')
else:
    webcam_input()