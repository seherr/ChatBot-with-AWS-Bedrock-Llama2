#1 import streamlit and chatbot file 
import streamlit as streamlit
import chatbot_backend as demo

#2 Title for chatbot 
st.title('Hi, This is Chatbot Seher :sunglasses:')

#3 Langchain memory to the sessipn cache - session State

if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()
    
#4 Add the UI chat history to the session cache 

if 'chat_history' not in st.session_state:  #see if the chat history hasnt't been created yet 
    st.session_state.chat_history =[]  #initialize the chat history 
    
#5 Re-render the chat history (streamlit re-runs the script, so need this to preserve previous chat messages)
for message in st.session_state.chat_history:
    with st.chat_message(message['role']):
        st.markdown(message['text'])
        
#6 Enter the details for chatbot input box 
if input_text:
    with st.chat_message('user'):
        st.markdown(input_text)
    st.sessipn_state.chat_history.append({'role':'user', 'text':input_text})
    

    chat_responce = demo.demo_conversation(input_text=text_input, memory=st.session_state.memory)

    with st.chat_message('assistant'):
        st.markdown(chat_response)
    