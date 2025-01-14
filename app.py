import streamlit as st
from groq import Groq


client = Groq(
    api_key="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"
)



def get_chat_completion(user_message):
    """
    Generate a chat completion using the Groq API.
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_message,
            }
        ],
        model="mixtral-8x7b-32768",
    )
    return chat_completion.choices[0].message.content

# Streamlit app layout with CSS styles
st.markdown(
    """
    <style>
        .stApp {
            width: 100vw;
            height: 100vh;
            position: absolute;
            left: -20%;
            top: -10%;
            background-image:url(" https://wallpapers.com/images/featured/dark-sky-r6up6saosci2pwnu.jpg");
            background-repeat: no-repeat;
            background-size: cover;
            background-position: right;
            color: white;
        }
        .stTextInput, .stButton {
            width: auto;
            margin-right: 10px;
            margin-bottom: 10px;
        }
        .stTitle {
            text-align: left;
        }
    </style>
    """,
    unsafe_allow_html=True
)



# Streamlit app layout
st.title("Hey! Aditya here ")

# User input for message
user_message = st.text_input("How can I help you : ")

# Submit button
if st.button("Send"):
    # Generate chat completion
    response = get_chat_completion(user_message)
    
    # Display the response outside the text area
    st.write("Chatbot: ", response)




