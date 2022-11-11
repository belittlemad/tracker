import streamlit as st
import streamlit.components.v1 as components
st.header("test html import")

HtmlFile = open("test.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
#st.write(source_code)
data = components.html(source_code)
st.write(data)
