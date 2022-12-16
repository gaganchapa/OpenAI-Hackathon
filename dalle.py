


import openai
import urllib.request
from PIL import Image
import streamlit as st


openai.api_key = "Enter the API key over here"

def generate_image(image_description):

  img_response = openai.Image.create(
    prompt = image_description,
    n=1,
    size="1024x1024")
  

  img_url = img_response['data'][0]['url']

  urllib.request.urlretrieve(img_url, 'img.png')

  img = Image.open("img.png")
  
  return img

st.set_page_config(layout="wide",page_icon="chart_with_upwards_trend")#to make the page layout wide.


img = Image.open("C:/Users/Tejo Vardhan/Downloads/OpenAI-graphic-removebg-preview.png")
mic = Image.open("C:/Users/Tejo Vardhan/Downloads/mic-circle-outline_1-removebg-preview.png")


col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    st.image(img, width=700)

with col3:
    st.write("")


buff, col, buff2 = st.columns([1,3,1])
col.header('Image Description')

# text input box for image recognition
img_description = col.text_input("")
buff, col, buff2 = st.columns([1.5,2.5,1])#spliting page into columns.

st.text('')
st.text('')
st.text('')

# slider
# first argument takes the title of the slider
# second argument takes the starting of the slider
# last argument takes the end number
buff, col, buff2 = st.columns([1,3,1])
col.subheader("Select the number of images: ")
level = col.slider(" ", 1, 10)
 
# print the number
# format() is used to print value
# of a variable at a specific position
col.text('number of images: {}'.format(level))


if col.button('Generate Image'):
    try:
        for i in range(0,level):
            generated_img = generate_image(img_description)
            col.image(generated_img)
        
    except:
        col.error("InvalidRequestError: Your request was rejected as a result of our safety system. ")
