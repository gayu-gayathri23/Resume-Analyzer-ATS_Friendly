import os
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import google.generativeai as genai

from pdf import extract_text

key=os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

model=genai.GenerativeModel('gemini-2.5-flash-lite')

def analyze_resume(pdf_doc,job_des):
    if pdf_doc is not None:
        pdf_text=extract_text(pdf_doc)
        st.write(F'Text extracted successfully ✅')
    else:
        st.warning('Error !! Drop the file in PDF format 🚨')
    
    ats_score=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des} 
                                    and provide the ATS score
                                    on scale of 0 to 100.pdf_text
                                    
                                    Generate the results in bullet points 
                                    (maximum 5 points)''')
    
    probability=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the probability of getting selected
                                    on scale of 0 to 100.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    good_fit=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the result whether the candidate is a good fit for the job or not
                                    good fit or not good fit.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    skills_match=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the skills match between the resume and 
                                    job description on scale of 0 to 100.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    missing_skills=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the missing skills in the resume as 
                                    per the job description.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    soft_skills=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the soft skills match between the resume and 
                                    job description on scale of 0 to 100.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    linkdin_profile=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the linkdin profile match between the resume and 
                                    job description on scale of 0 to 100.pdf_text
                                    
                                    Generate the results in bullet points
                                    (maximum 5 points)''')
    
    SWOT_analysis=model.generate_content(f'''Compare the given pdf{pdf_text}
                                    and given job description {job_des}
                                    and provide the SWOT analysis of the resume 
                                    as per the job description.pdf_text
                                    
                                    generate the results in bullet points
                                    (maximum 5 points)''')
    
    return st.write(ats_score.text), st.write(probability.text), st.write(good_fit.text), st.write(skills_match.text), st.write(missing_skills.text), st.write(soft_skills.text), st.write(linkdin_profile.text), st.write(SWOT_analysis.text)  
           
            
                
                 
                                           
                    
    

    
    
                                    
    
     
    