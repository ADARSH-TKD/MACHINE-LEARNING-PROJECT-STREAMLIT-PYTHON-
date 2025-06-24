import cv2
import streamlit as st 
from PIL import Image
import numpy as np

st.title("IMAGE_FILTERING_TOOLS")
st.write("file you images with color and joy ")
file = st.file_uploader("choose the image ",type = ["jpg","jpeg","png"])
col1, col2 = st.columns(2)
with col1:
    if file is not None:
        image = Image.open(file)
        st.image(image, caption="Uploaded Image")
        filter = st.selectbox("select the filter you want to apply :",["gray","rgb","bgr"])
with col2:
    if file is not None:
        if filter == "gray":
            # Convert PIL Image to numpy array for OpenCV
                image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
                img = cv2.cvtColor(src=image_cv, code=cv2.COLOR_BGR2GRAY)
                st.image(img, caption="gray_image")
        elif filter == "rgb":
            image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            img = cv2.cvtColor(src=image_cv, code=cv2.COLOR_BGR2GRAY)
            st.image(img, caption="gray_image")
        elif filter == "bgr":
            image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
            st.image(image_cv, caption="gray_image")
        
