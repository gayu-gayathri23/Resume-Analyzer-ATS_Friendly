import streamlit as st
from analysis import analyze_resume 
st.set_page_config('Resume Analyzer',page_icon='🛠️')
st.title('RESUME ANALYZER USING AI 🤖🧠🇦🇮👾')

st.header(':blue[AI powered Resume Analyzer with given Job Description using AI 🚀]')

st.subheader('''This page helps you to compare the resume and the given job description and provides ATS score, probability of selection, good fit or not good fit, skills match, missing skills, soft skills match, linkdin profile match and SWOT analysis of the resume as per the job description 🧐''')

st.sidebar.header(':blue[Upload your Resume 📜]')  

pdf_doc=st.sidebar.file_uploader('Click here 👇 ',type=['pdf'])

st.sidebar.markdown('Designed by Gayathri Subramanian 😎')
st.sidebar.markdown('Git hub: https://github.com/gayu-gayathri23/Resume-Analyzer-ATS_Friendly.git')

job_des=st.text_area('Copy and paste the job description here 🕹️ ',max_chars=50000)

submit=st.button('Get Results 🔥🔥🔥')



if submit:
    with st.spinner('Loading.....🌀⌛'):
        analyze_resume(pdf_doc,job_des)
        