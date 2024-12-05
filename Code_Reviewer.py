# Code Reviewer
import streamlit as st
import google.generativeai as genai
genai.configure(api_key='AIzaSyCs60qWMnNF0e6NNgqEyQ8bT_4F8ACxSH4')
system_propmt='You are the Helpfull AI Assitant, to rectify the mistakes in the progamming. you are expected to reply in an much correct as possible. In case if a student ask any questions outside the programming scope, politely decline and ask them to ask the questions related to programming.'
model=genai.GenerativeModel(model_name="gemini-1.5-flash",
                            system_instruction=system_propmt)
st.title('AI CODE REVIEWER')
st.write("I'm here, to review you Code")
user_prompt=st.text_area('Enter the Query:',
              placeholder='type the query',
              height=250)
button_click=st.button("generate responce")
if button_click==True:
    response=model.generate_content(user_prompt)
    st.write(response.text)
    
 