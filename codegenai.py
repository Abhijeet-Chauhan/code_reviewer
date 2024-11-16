import streamlit as st
import google.generativeai as genai

# Configure the API key for Google Gemini
genai.configure(api_key="AIzaSyB4tK6azgrb_-VQSgsNT2BW29ABjwaxJII")
llm = genai.GenerativeModel("models/gemini-1.5-flash")  # Change the model as needed
chatbot = llm.start_chat(history=[])

# Streamlit interface setup
st.title("CodeFixer - AI Code Reviewer")
st.markdown("Submit your Python code below, and I will review it for potential bugs and provide fixes.")

# User input for Python code
code_input = st.text_area("Paste your Python code here:", height=300)

# Function to send code to Google Gemini for review
def review_code(code):
    prompt = f"Review the following Python code for bugs, errors, or areas of improvement. Provide suggestions and corrected code:\n\n{code}"

    try:
        # Send the review request to Google Gemini
        response = chatbot.send_message(prompt)
        return response.text.strip()  # Get and return AI's review
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize reviewed_code as None
reviewed_code = None

# Add a Submit button for code review
if st.button("Submit Code for Review"):
    if code_input:
        st.subheader("AI Code Review:")
        # Review the code and display the result
        reviewed_code = review_code(code_input)
        st.write(reviewed_code)
    else:
        st.warning("Please paste some Python code above to get a review.")

# Optional: Allow users to download the reviewed code, only if reviewed_code is available
if reviewed_code:
    st.download_button(
        label="Download Fixed Code",
        data=reviewed_code,
        file_name="reviewed_code.py",
        mime="text/x-python-script"
    )
