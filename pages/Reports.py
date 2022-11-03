import streamlit as st
import urllib,base64
st.set_page_config(layout="wide")
option = st.selectbox(
    'View Some of the Climate Change Impact on Food Reports',
    ('None', 'Report 1', 'Report 2'))

st.write('You selected:', option)
#function to display the PDF of a given file 
report_name = "reports/"+str(option)+".pdf"
if option=="None":
    pass
else:
    with open("reports/climate2030_india.pdf", "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="1190" height="1000" type="application/pdf">'
    st.markdown(pdf_display, unsafe_allow_html=True)
