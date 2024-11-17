import streamlit as st
import google.generativeai as genai


genai.configure(api_key="AIzaSyB4tK6azgrb_-VQSgsNT2BW29ABjwaxJII")
llm = genai.GenerativeModel("models/gemini-1.5-flash")  
chatbot = llm.start_chat(history=[])

# Streamlit interface setup
st.title("CodeFixer - AI Code Reviewer")
st.markdown("Submit your Python code below, and I will review it for potential bugs and provide fixes.")

# User input for Python code
code_input = st.text_area("Paste your Python code here:", height=300)

def review_code(code):
    prompt = f"Review the following Python code for bugs, errors, or areas of improvement. Provide suggestions and corrected code:\n\n{code}"

    try:
        response = chatbot.send_message(prompt)
        return response.text.strip()  
    except Exception as e:
        return f"Error: {str(e)}"

reviewed_code = None

if st.button("Submit Code for Review"):
    if code_input:
        st.subheader("AI Code Review:")
        reviewed_code = review_code(code_input)
        st.write(reviewed_code)
    else:
        st.warning("Please paste some Python code above to get a review.")

if reviewed_code:
    st.download_button(
        label="Download Fixed Code",
        data=reviewed_code,
        file_name="reviewed_code.py",
        mime="text/x-python-script"
    )
