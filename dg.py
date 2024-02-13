### Built in Map 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt

st.title('Digimon Dataset')
st.write('This app analyses all the digimons and their details in the database.')
dg = pd.read_csv('digimon.csv')
st.write(dg.head(5))
st.write('Description of each field in the dataset.')
st.write(dg.describe())

st.title('Data Preparation')
st.title('Null Values')
st.write("Displaying the null values in the database.")
st.write(dg.isnull())
st.write("Current number of null values in the database. ", dg.isnull().sum())
dg = dg.dropna()
dg = dg.fillna("NA")
st.write("Null values are now removed.")
st.write(dg.isnull())
st.write("Current number of null values in the database. ", dg.isnull().sum())

st.title('Duplicate Values')
st.write("Displaying the duplicates in the database.")
st.write(dg.duplicated())
st.write("Current number of duplicates in the database. ",dg.duplicated().sum())
dg = dg.drop_duplicates()
st.write("Duplicates are now gone.")
st.write(dg.duplicated())
st.write("Current number of duplicates in the database. ",dg.duplicated().sum())


st.title('Data Visualization')
st.title('Line Chart')
dg_group1 = pd.DataFrame(dg.groupby(['Type']).count()['Number'])
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
st.line_chart (dg_group1)


dg_group2 = dg['Type'].value_counts()
fig2, ax = plt.subplots()
dg_group2.plot(kind='bar', ax=ax)
plt.title('Digimon types')
plt.ylabel('Count')
st.title('Bar Chart')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
st.pyplot(fig2)


st.title('Histogram')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
fig3, ax = plt.subplots()
dg['Lv50 Spd'].plot.hist(bins=50, ax=ax)
plt.xlabel('Lv 50 Spd')
st.pyplot(fig3)


st.title('Pie Chart')
st.write('This graphs shows the total percentage of digimon stages in the whole dataset.')
pie_dg = dg.groupby('Stage')['Number'].sum()
fig, ax = plt.subplots(figsize=(10,10))
ax.pie(pie_dg, labels=pie_dg.index, autopct='%1.0f%%', startangle=60)
st.pyplot(fig)

st.title('SF Trees')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
fig2 = alt.Chart(dg).mark_bar().encode(x = 'Type', y = 'Attribute')
st.altair_chart(fig2)


with st.form('first form'):
    graph_title = st.text_input(label="graph Title")   
    perc_heads = st.number_input(label = "chance of coin landing", min_value=0.0, max_value=1.0, value=.5)
    submit = st.form_submit_button()


#dg = dg.sample(n = 1000)
#st.map(dg)
#st.pydeck_chart(dg)