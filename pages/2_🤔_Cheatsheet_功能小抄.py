import streamlit as st 
st.set_page_config(page_title="Streamlit 功能小抄", page_icon=":question:")
st.title("Streamlit 功能小抄")
col1, col2 = st.columns(2)

with col1:
    with st.expander("用Streamlit 呈現 Plotly"):
        st.write("st.plotly_chart")
        # Display Code
        mycode = """
# Core Pkgs
import streamlit as st 

# Load EDA Pkgs
import pandas as pd 
import numpy as np

# Load Data Vis Pkg
import plotly.express as px

def main():
st.title("用Streamlit 呈現 Plotly")
# Load Dataset
df = pd.read_csv("data/sales_data_sample.csv")
dataframe(df.head())

st.dataframe(df)

# Plotting with Plotly
fig = px.pie(df,values='單價',names='系列',
                title='Pie Chart of 系列usage')
st.plotly_chart(fig)

if __name__ == '__main__':
main()
    """
        st.code(mycode, language = 'python')
        
with col2:
    with st.expander("Streamlit的文字輸入方法"):
        st.write('st.text / st.title / st.write')
        # Display Code
        mycode = """
import streamlit as st 

# Text Input
name = st.text_input("Enter Firstname")

# Text Input Hide Password
password = st.text_input("Enter Password",
                        type='password')
st.title(fname)

# Text Area
message = st.text_area("Enter Message",
                    height=100)
st.write(message)

# Numbers
number = st.number_input("Enter Number",
                        1.0,25.0)
st.write(number)

# Date Input
myappointment = st.date_input("Appointment")

# Time Input
mytime = st.time_input("My Time")
            """
        st.code(mycode, language = 'python')


col3, col4 = st.columns(2)
with col3:
    with st.expander("Streamlit的選擇工具"):
        st.write('st. selectbox / st.multiselect / st.slider / st.select_slider')
        # Display Code
        mycode = """
import streamlit as st 

# Select/Multiple select
my_lang = ["Python","Julia","Go","Rust"]

choice = st.selectbox("Language",my_lang)
st.write("You selected {}".format(choice))

# Multiple Selection
spoken_lang = ("English",
            "French",
            "Spanish",
            "Twi")
my_spoken_lang = st.multiselect(
            "Spoken Lang",
            spoken_lang,
            default="English")

# Slider 
# Numbers (Int/Float/Dates)
age = st.slider("Age",1,100)

# Any Datatype
# Select Slider
color = st.select_slider(
            "Choose Color",
            options=["yellow",
                        "red",
                        "blue",
                        "black",
                        "white"],
            value=("yellow","red"))
            """
        st.code(mycode, language = 'python')
        
with col4:
    with st.expander("Streamlit的文字顯示功能"):
        st.write('st.text / st.header / st.subheader / st.title / st.markdown')
        # Display Code
        mycode = """
import streamlit as st 

## Working with and Displaying Text 
st.text("Hello World this is a text")
name = "Johnny"
st.text("This is so {}".format(name))

## Header
st.header("This is a header")

## Subheader
st.subheader("This is a subheader")

## Title
st.title("This is a title")

## Markdown
st.markdown("## This is markdown")

## Displaying Colored Text/Bootstraps Alert
st.success("Successful")
st.warning("This is danger")
st.info("This is information")
st.error("This is an error")

# Superfunction
st.write("Normal Text")
st.write("## This is a markdown text")
st.write(1+2)

# Help Info
st.help(range)
        """
        st.code(mycode, language = 'python')
        
    
col5, col6 = st.columns(2)

with col5:
    with st.expander("Streamlit的側邊列功能"):
        st.write('st.sidebar.success / st.sidebar.button / st.sidebar.selectbox')
        # Display Code
        mycode = """
# Core Pkgs
import streamlit as st 

# Adding Widgets to Sidebar
# st.sidebar.success("Hello World")
# st.sidebar.button("Hello")

# # Attrib/Method/Widget
# st.write(dir(st.sidebar))

menu = st.sidebar.selectbox("Menu",
                        ["Home","About"])

#   with st.sidebar:
#       st.sidebar.header('側邊標題')
#       st.sidebar.subheader('側邊欄副標題')
#       st.sidebar.write('側邊欄字')

        """
        st.code(mycode, language = 'python')    

        
with col6:
    with st.expander("Streamlit的縮放顯示功能"):
        st.write('st.expander')
        # Display Code
        mycode = """
import streamlit as st 

def main():
st.title("Multi Element Container")
st.text("Multiple elements out of order")

with st.expander("Data Types Summary"):
    st.success("From Inside Container 1")
    st.write("From Inside Container")

with st.expander("Data Types Summary"):
    st.write('f')

st.warning("From Outside Container")

if __name__ == '__main__':
main()
        """
        st.code(mycode, language = 'python')
    

col7, col8 = st.columns(2)

with col7:
    with st.expander("Streamlit的上傳方法"):
        st.write('st.sidebar.file_uploader')
        # Display Code
        mycode = """
import pandas as pd 
import streamlit as st

st.write(‘’‘
# 檔案上傳演練
’‘’)

st.sidebar.header('User Input Features')

uploaded_file = st.sidebar.file_uploader("請上傳您的CSV檔案", type=["csv"])

if uploaded_file is not None:
sales_data = pd.read_csv(uploaded_file)
else:
sales_data = pd.read_csv('data/sales_data_sample.csv')

#### 讀取訂單資料

# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
st.write(sales_data)
# sales_data = pd.read_csv('sales_data.csv')
# sales_data['利潤'] = sales_data['單價'] - sales_data['成本']

# 將訂單時間轉換成datetime形式
# sales_data['訂單時間'] = pd.to_datetime(sales_data['訂單時間'])
    
# Descriptive
        
with st.expander("Data Types Summary"):
    st.dataframe(sales_data.dtypes)

with st.expander("Descriptive Summary"):
    st.dataframe(sales_data.describe())

# with st.expander("廣告代號all Distribution"):
# 	st.dataframe(sales_data['廣告代號all'].value_counts())

# with st.expander("系列 Distribution"):
# 	st.dataframe(sales_data['系列'].value_counts())

else:
st.write('等待新資料上傳，現在使用的是如下的範例資料')
st.dataframe(sales_data)
        """
        st.code(mycode, language = 'python')
    
with col8:
    with st.expander("Streamlit的下載方法"):
        st.write('st.dataframe / st.markdown / csv_downloader')
        # Display Code
        mycode = """
import streamlit.components as stc

import base64 
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
import pandas as pd 
import streamlit as st
import numpy as np
import pickle
import pandas as pd
from io import BytesIO
# pip install pyxlsb
# pip install xlsxwriter

def csv_downloader(data,filename):
csvfile = data.to_csv()
b64 = base64.b64encode(csvfile.encode("UTF-8-sig")).decode()
new_filename = filename+"_{}_.csv".format(timestr)
# 	st.markdown("#### Download File ###")
href = f'<a href="data:file/csv;base64,{b64}" download="{new_filename}">Click Here!!</a>'
st.markdown(href,unsafe_allow_html=True)


def excel_downloader(data, filename):
towrite = BytesIO()
downloaded_file = data.to_excel(towrite, encoding='utf-8', index=False, header=True) # write to BytesIO buffer
towrite.seek(0)  # reset pointer
b64 = base64.b64encode(towrite.read()).decode() 
new_filename = filename+"_{}_.xlsx".format(timestr)
# st.markdown("#### Download File ###")
href= f'<a href="data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{b64}" download="{new_filename}">Download excel file</a>'
st.markdown(href, unsafe_allow_html=True)

# --------------- Display -------------------
vals= ['A','B','C']
df = pd.DataFrame(vals, columns=["Title"])


st.write('''
# 下載方法
''')
st.dataframe(df)

st.markdown("#### Download csv File ###")
csv_downloader(data=df,filename='csv範例資料')

st.markdown("#### Download excel File ###")
excel_downloader(data=df,filename='csv範例資料')

            """
        st.code(mycode, language = 'python')     
