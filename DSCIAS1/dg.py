### Built in Map 
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
st.set_page_config(layout='wide')

st.title('Digimon Dataset')
st.write('This app analyses all the digimons and their details in the database.')
dg = pd.read_csv('digimon.csv')
st.write(dg.head(5))
st.write('Description of each field in the dataset.')
st.write(dg.describe())

import streamlit as st


Max_Digimon = st.sidebar.slider('Select Digimon index range:', min_value=0, max_value=254, value=(0, 254))
No_Digimon = dg[(dg['Number'] >= Max_Digimon[0]) & (dg['Number'] <= Max_Digimon[1])]
st.header('Filtered Digimon Data')
st.write('This shows the filtered Digimon data based on the selected index range.')
st.write(No_Digimon)

st.title('Data Preparation')


st.header('Null Values')
st.write("Displaying the null values in the database.")
st.write(dg.isnull())
st.write("Current number of null values in the database. ", dg.isnull().sum())
dg = dg.dropna()
dg = dg.fillna("NA")
st.write("Null values are now removed.")
st.write(dg.isnull())
st.write("Current number of null values in the database. ", dg.isnull().sum())


st.header('Duplicate Values')
st.write("Displaying the duplicates in the database.")
st.write(dg.duplicated())
st.write("Current number of duplicates in the database. ",dg.duplicated().sum())
dg = dg.drop_duplicates()
st.write("Duplicates are now gone.")
st.write(dg.duplicated())
st.write("Current number of duplicates in the database. ",dg.duplicated().sum())


st.title('Data Visualization')
col1, col2 = st.columns(2)

with col1:
    st.header('Line Chart')
    dg_group1 = pd.DataFrame(No_Digimon.groupby(['Type']).count()['Number'])
    st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
    st.line_chart (dg_group1)

with col2:
    dg_group2 = No_Digimon['Attribute'].value_counts()
    fig2, ax = plt.subplots()
    dg_group2.plot(kind='bar', ax=ax)
    plt.title('Digimon types')
    plt.ylabel('Count')
    st.header('Bar Chart')
    st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
    st.pyplot(fig2)

with col2:
    st.header('Altair Chart')
    st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
    fig2 = alt.Chart(No_Digimon).mark_bar().encode(x = 'Type', y = 'Lv 50 HP')
    st.altair_chart(fig2)

with col1:
    st.header('Scatter Plot')
    st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(No_Digimon['Memory'], No_Digimon['Equip Slots'])
    ax.set_xlabel('Memory')
    ax.set_ylabel('Equip SLots')
    ax.set_title('Digimon Memory & Equip Slots')
    st.pyplot(fig)


st.header('Histogram')
st.write('This app analyses trees in San Francisco using a dataset kindly provided by SF DPW')
fig3, ax = plt.subplots()
speed = st.slider('Select speed range:', min_value=0, max_value=200, value=(0, 200))
filter_speed = No_Digimon[(No_Digimon['Lv50 Spd'] >= speed[0]) & (No_Digimon['Lv50 Spd'] <= speed[1])]
filter_speed['Lv50 Spd'].plot.hist(bins=50, ax=ax)
plt.xlabel('Lv 50 Spd')
st.pyplot(fig3)


st.header('Pie Chart')
st.write('This graphs shows the total percentage of digimon stages in the whole dataset.')
filter_type = st.selectbox('Select Type:', No_Digimon['Type'].unique())
filtered_dg = No_Digimon[No_Digimon['Type'] == filter_type]
pie_dg = filtered_dg.groupby('Stage')['Number'].sum()
fig, ax = plt.subplots(figsize=(10,10))
ax.set_title('Distribution of Digimon Stages')
ax.pie(pie_dg, labels=pie_dg.index, autopct='%1.0f%%', startangle=60)
st.pyplot(fig)

st.header('Area Chart')
st.write('This graph shows an area chart.')
fig, ax = plt.subplots(figsize=(8, 6))
ax.fill_between(No_Digimon['Stage'], No_Digimon['Lv 50 HP'], color='skyblue', alpha=0.4)
ax.plot(No_Digimon['Stage'], No_Digimon['Lv 50 HP'], color='Slateblue', alpha=0.6, linewidth=2)

ax.set_xlabel('Stage')
ax.set_ylabel('Lv 50 HP')
ax.set_title('Area Chart')
st.pyplot(fig)

with st.form('first form'):
    graph_title = st.text_input(label="graph Title")   
    perc_heads = st.number_input(label = "chance of coin landing", min_value=0.0, max_value=1.0, value=.5)
    submit = st.form_submit_button()


#dg = dg.sample(n = 1000)
#st.map(dg)
#st.pydeck_chart(dg)