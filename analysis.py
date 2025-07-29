import os
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

import google.generativeai as genai

# refer 
from pdf import extractpdf

key = os.getenv('GOOGLE_API_KEY')
genai.configure(api_key=key)

# call the model 

model = genai.GenerativeModel('gemini-1.5-flash')

# create a def function to analyze pdf and jd

def analyze_resume(pdf_doc,job_des):
    if pdf_doc is not None:
        pdf_text = extractpdf(pdf_doc)
        st.write('Extracted Successfuly✅')
        
    else:
        st.warning('Drop file in PDF format')
        
    ats_score = model.generate_content(f'''Compare the resume {pdf_text} with job
                           description {job_des} and get ATS Score rangeC between 0 to 100 as the output''')
    
    good_fit = model.generate_content(f''' Compare the resume {pdf_text} with job description {job_des} and 
                                      say am i a good fit for this job or not .Generate results in bullet Points''')
    
    swot_analysis = model.generate_content(f''' Compare the resume {pdf_text} with job description {job_des} and provide SWOT analysis.
                                           Generative resultd in bullet points''')
    prob = model.generate_content(f''' Compare the resume {pdf_text} with job description {job_des} and give 
                                           the probability to get select for the given job''')
    
    return st.write(ats_score.text),st.write(good_fit.text),st.write(swot_analysis.text)