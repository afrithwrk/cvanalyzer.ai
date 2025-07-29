import streamlit as st 
from analysis import analyze_resume

st.sidebar.header('Afrith')
st.sidebar.write(':grey[Data Scientist]')
st.sidebar.link_button('LinkedIn🔗',url='https://www.linkedin.com/in/theafrith/')
st.sidebar.image('/Users/afrithh/Downloads/Image/WhatsApp Image 2025-01-07 at 23.30.50.jpeg')

st.title('CV ANALYZER🎯')

st.header('This page helps you to compare your resume with the given job description')

st.sidebar.subheader('Drop your resume here📚')

pdf_doc = st.sidebar.file_uploader('Click here to browse',type = ['pdf'])

st.sidebar.markdown('Designed by Afrith')

job_des = st.text_area('Copy paste the job description here',max_chars = 10000)

submit = st.button('Generate ATS score')

if submit:
    with st.spinner('Getting Results....'):
        analyze_resume(pdf_doc,job_des)