### 生物學案例 - 鳶尾花預測 ###
#%% (III) API 與 App 設計
import pandas as pd
import numpy as np
from iris_API import *
import streamlit as st

@st.cache
def backend(df):
    
    X, y, X_scaled, y_encoded = set_vars(df)
    clustering = modeling(X_scaled)
    X = get_prediction(X, clustering)
    
    return X, y, y_encoded

def upload():
    
    data_file = st.file_uploader("請上傳鳶尾花案例資料：IRIS.csv", type=["csv"])
    
    if data_file is not None:
        return pd.read_csv(data_file, encoding="utf=8-sig")

def show_img():
    
    from PIL import Image
    image = Image.open('christina-brinza-TXmV4YYrzxg-unsplash.jpg')
    img_caption = "Photo by Christina Brinza on Unsplash"
    
    return st.image(image, caption=img_caption)
    
def main_page():
        
    # Text
    st.markdown("""
                # 生物學案例 - 鳶尾花預測
                ### (IV) Streamlit App 製作
                """, unsafe_allow_html=True)
    st.write("""
             **IRIS 資料集**是資料科學界中非常知名的資料集。常作為**分類問題**的招牌示範資料。
             在1936 年，英國統計學家和生物學家 Ronald Fisher 在論文中曾引入此多變量資料集。
             此資料是埃德加安德森收集三種鳶尾花種的不同特徵，因此有時作安德森鳶尾花資料集。
             該資料集包含 **三種鳶尾花（山鳶尾、變色鳶尾和維吉尼亞鳶尾）** 各 50 個樣本。
             從每個樣本中測量四種特徵：**萼片和花瓣的長度和寬度**，以厘米為單位。
             """, unsafe_allow_html=True)
    st.text("")
    
    # col
    col1, col2 = st.columns([3,2])
    
    with col1:
        st.write("""**分析目標: 從萼片與花瓣長寬度預測花種**""")
        df = upload()
        
    with col2:
        show_img()

    if df is not None:
        
        st.markdown("### 資料樣貌")
        with st.expander("前五筆資料"):  
            st.dataframe(data=df.head())
        
        # backend
        X, y, y_encoded = backend(df)
        
        predict_fig = plot_reseult(X,y, y_encoded, predict=True)
        actual_fig = plot_reseult(X,y, y_encoded, predict=False)
        
        st.plotly_chart(predict_fig, use_container_width = True)
        st.plotly_chart(actual_fig, use_container_width = True)
    
    # st.write("""<br><br><br><br><br><br><br><br><br><br>
    #          此App為台灣行銷研究有限公司版權所有之課程用教材 2022
    #          """, unsafe_allow_html=True)

if __name__ == "__main__":
    main_page()
    