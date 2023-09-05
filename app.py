import streamlit as st
import pandas as pd
import numpy as np
from tensorflow import keras

def sample():
    return "working"
# defining the function which will make the prediction using 
# the data which the user inputs
def prediction(mean_integrated, sd, ek, skewness, mean_dmsnr_curve, sd_dmsnr_curve, ek_dmsnr_curve, skewness_dmsnr_curve):  
    indgred=[[mean_integrated, sd, ek, skewness, mean_dmsnr_curve, sd_dmsnr_curve, ek_dmsnr_curve, skewness_dmsnr_curve]]
    model = keras.models.load_model('model.hdf5')
    result = model.predict(indgred)
    if (result > 0.5).all():
        a = 'Yes'
    else:
        a = 'No'
    return a

def main():
      # giving the webpage a title
      
    # here we define some of the front end elements of the web page like 
    # the font and background color, the padding and the text to be displayed
    html_temp = """
    <div style ="background-color:yellow;padding:13px">
    <h1 style ="color:black;text-align:center;">Pulsor Star Prediction App </h1>
    </div>
    """
      
    # this line allows us to display the front end aspects we have 
    # defined in the above code
    st.markdown(html_temp, unsafe_allow_html = True)
      
    # the following lines create text boxes in which the user can enter 
    # the data required to make the prediction
    mean_integrated = st.number_input('Mean_Integrated')
    sd = st.number_input('SD')
    ek = st.number_input('EK')
    skewness = st.number_input('Skewness')
    mean_dmsnr_curve = st.number_input('Mean_DMSNR_Curve')
    sd_dmsnr_curve = st.number_input('SD_DMSNR_Curve')
    ek_dmsnr_curve = st.number_input('EK_DMSNR_Curve')
    skewness_dmsnr_curve = st.number_input('Skewness_DMSNR_Curve')
    result=""
    # the below line ensures that when the button called 'Predict' is clicked, 
    # the prediction function defined above is called to make the prediction 
    # and store it in the variable result
   # sample()
    if st.button("Predict"):
        result = prediction(mean_integrated, sd, ek, skewness, mean_dmsnr_curve, sd_dmsnr_curve, ek_dmsnr_curve, skewness_dmsnr_curve)
    st.success('The Prediction is {}'.format(result))
     
if __name__=='__main__':
    main()
