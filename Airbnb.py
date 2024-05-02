import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
pd.set_option('display.max_columns', None)
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
from PIL import Image

st.set_page_config(layout= "wide")
st.markdown("""
    <h1 style='text-align: center; color: Black'>AIRBNB DATA ANALYSIS</h1>
    """, unsafe_allow_html=True)
st.write("")

st.markdown(f""" <style>.stApp {{
                        background:url("https://c8.alamy.com/comp/2M6RXCF/airbnb-rotated-logo-white-background-b-2M6RXCF.jpg");
                        background-size: cover}}
                     </style>""", unsafe_allow_html=True)

#Uploading CSV files
df_US= pd.read_csv("/content/US_Airbnb_final.csv")
df_Brazil= pd.read_csv("/content/Brazil_Airbnb_final.csv")
df_Canada= pd.read_csv("/content/Canada_Airbnb_final.csv")
df_Hong= pd.read_csv("/content/Hong_Airbnb_final.csv")
df_Port= pd.read_csv("/content/Portugal_Airbnb_final.csv")
df_Spain= pd.read_csv("/content/Spain_Airbnb_final.csv")
df_Turkey= pd.read_csv("/content/Turkey_Airbnb_final.csv")
df_Aus= pd.read_csv("/content/AUS_Airbnb_final.csv")
df_Air= pd.read_csv("/content/Airbnb_final.csv")


# select= option_menu("Explore", ["Home", "Data Exploration"],orientation="horizontal")
select = option_menu(
    menu_title = None,
    options = ["Home","Explore Data"],
    icons =["house","bar-chart"],orientation="horizontal")
if select == "Home":
  text_content = """
    <h2 style='text-align: center; color: Black;'>Welcome to my Airbnb data analysis project</h2>
    <p style='font-size: 18px; text-align: center; color: Black'>
In our project, we're diving deep into Airbnb's vast collection of listings to find useful information. We use a powerful tool called MongoDB Atlas to help us analyze and understand the data better. Our main goal is to learn how the Airbnb market works. First, we carefully clean and organize the data to make sure it's accurate and reliable. Then, we create interactive maps and graphs to visualize the data in a meaningful way. These visuals help us spot trends, patterns, and differences in things like prices, availability, and what guests prefer. We're not just exploring data; we're discovering insights that can help people make better decisions in the Airbnb world, like how to price their listings or where to focus their efforts. Join us on this journey as we use data and MongoDB Atlas to shed light on the Airbnb phenomenon!</p>
        """

  # Display the text using markdown function
  st.markdown(text_content, unsafe_allow_html=True)

def chats():
  st.write("Data Analysis in",country)
  df_1=a.groupby("property_type").agg({"price":"mean","property_type":"count"}).sort_values("price")
  prop_name=[]

  for group_name,group_data in df_1.iterrows():
    prop_name.append(group_name)
  df_1["property name"]=prop_name

  df_2=a.groupby("host_neighbourhood").agg({"price":"mean","host_neighbourhood":"count"}).sort_values("price")
  Nei_names=[]
  for grp_name,grp_data in df_2.iterrows():
    Nei_names.append(grp_name)
  df_2["Neighbourhood"]=Nei_names

  df3=a.groupby(["city", "property_type"]).size().reset_index(name='number_of_reviews')

  df4=a.groupby("room_type").size().reset_index(name='number_of_reviews')

  col1,col2=st.columns(2)
  with col1:
    fig = px.bar(df_1,x='property name', y='price',color='price',color_discrete_sequence=px.colors.diverging.BrBG,
                  title='Property Type with Average Price'
          )
    st.plotly_chart(fig, use_container_width=True)

  with col2:
    fig = px.bar(df_2,x='Neighbourhood', y='price',color='price',color_discrete_sequence=px.colors.diverging.BrBG,
                  title='Average Price with respect to Neighbourhood'
          )
    st.plotly_chart(fig, use_container_width=True)

  col1,col2=st.columns(2)
  with col1:
    fig = px.sunburst(a, path=['city', 'property_type'], values='number_of_reviews',
                    title='City and its Property Types')
    st.plotly_chart(fig, use_container_width=True)

  with col2:
    fig = px.bar(a, x='room_type', y='number_of_reviews',
             labels={'room_type': 'Room Type', 'number_of_reviews': 'Number of Reviews'},
             title='Room Type with Review')

    st.plotly_chart(fig, use_container_width=True)

if select == "Explore Data":
  country = st.selectbox("Select A Country To Analyse", ["United States", "Turkey", "Portugal", "Canada", "Brazil", "Hong Kong", "Spain", "Australia"])




  if country == "United States":
    a=df_US
    chats()
  elif country == "Brazil":
    a=df_Brazil
    chats()
  elif country == "Canada":
    a=df_Canada
    chats()
  elif country == "Hong Kong":
    a=df_Hong
    chats()
  elif country == "Portugal":
    a=df_Port
    chats()
  elif country == "Spain":
    a=df_Spain
    chats()
  elif country == "Turkey":
    a=df_Turkey
    chats()
  elif country == "Australia":
    a=df_Aus
    chats()



    # fig = px.scatter_mapbox(df_US, lat="Latitudes", lon="Longitudes",
    #                       color=df_US["price"] ,size=df_US["number_of_reviews"],
    #                     color_discrete_sequence=["fuchsia"], zoom=3,width=1200,
    #                     height=900)
    # fig.update_layout(
    #     mapbox_style="open-street-map")
    # fig.update_layout(margin={"r":0,"t":50,"l":0,"b":10})
    # st.plotly_chart(fig, use_container_width=True)

