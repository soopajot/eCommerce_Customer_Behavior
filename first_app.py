import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

st.header('eCommerce Customer Behavior')
st.subheader('This is a subheader')
st.write("Voici un aperçu du dataset")
#st.write(pd.DataFrame({
#    'first column': [1, 2, 3, 4],
#    'second column': [10, 20, 30, 40]
#}))

#DATE_COLUMN = 'date/time'
#DATA_URL = ('https://drive.google.com/file/d/19UDMe-_g-GrIX9Nu6H6o1YapfS2pPwF4/view?usp=sharing')

#url = 'https://drive.google.com/file/d/19UDMe-_g-GrIX9Nu6H6o1YapfS2pPwF4/view?usp=sharing'
#path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
df = pd.read_csv('df.csv')
stats = pd.read_csv('stats.csv')
items = pd.read_csv('items.csv')
top_produits_merged = pd.read_csv('top_produits_merged.csv')

df['date'] = df['timestamp'].apply(lambda x: datetime.fromtimestamp(x/1000))
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day'] = df['date'].dt.day
df['dayofweek'] = df['date'].dt.dayofweek
df['hour'] = df['date'].dt.hour

st.balloons()

st.text('This is some text.')

st.markdown('Streamlit is **_really_ cool**.')

st.write("Voici un aperçu du dataset")
st.write(df)
st.dataframe(df.style.highlight_max(axis=0))

st.write("Voici un aperçu du dataset")
st.write(stats)

st.write("Voici un aperçu du dataset")
st.write(items)

st.write("Voici un aperçu du dataset")
st.write(top_produits_merged)

from PIL import Image
image = Image.open('heatmap.png')
st.image(image, caption='Notre Heatmap')

image1 = Image.open('img-1.png')
st.image(image1, caption='Notre img')

image2 = Image.open('img-2.png')
st.image(image2, caption='Notre img')

image3 = Image.open('img-3.png')
st.image(image3, caption='Notre img')

image4 = Image.open('img-4.png')
st.image(image4, caption='Notre img')

image5 = Image.open('img-5.png')
st.image(image5, caption='Notre img')

image6 = Image.open('img-6.png')
st.image(image6, caption='Notre img')

image7 = Image.open('img-7.png')
st.image(image7, caption='Notre img')

image8 = Image.open('img-8.png')
st.image(image8, caption='Notre img')

                


#chart_data = pd.DataFrame(df,columns=['month'])
#st.line_chart(chart_data)


