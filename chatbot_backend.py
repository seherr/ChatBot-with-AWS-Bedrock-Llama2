#1 import the os, Bedrock ,conversationChain,conversationBufferMemory Langchain Modules

import os
from langchain.llms.Bedrock import Bedrockfrom 
from langchain.memory import conversationalBufferMemory
from langchain.chains import conversationChain

#2a write a function for invoking model-client connection with bedrock with profile, model_id & Inference params
#add credentials diyerek yapabilirsin 
def demo_chatbot():
    demo_llm=Bedrock(
        credentials_profile_name = 'default',
        model_id = 'meta.lama'
        model_kwargs={
            'temperature': 0.9,
            'top_p':0.5,
            'max_gen_len':512})
    return demo_llm

#2b Test out the LLM with predit method
    #return demo_llm.predict(input_text) 
#response = demo_chatbot('hi, what is your name ')
#print(response)

#3 Create a function for conversationBufferMemory (llm and max token limit)

def demo_memory():
    llm_date=demo_chatbot()
    memory = conversationBufferMemory(llm=llm_date, max_token_limit = 512)
    return memory

#4 create a function for conversation Chain - Input text + memory

def demo_chain(input_text, memory):
    llm_chain_data = demo_chatbot()
    llm_conersation = CeonversationChain(llm=llm_chain_data, memory=memory,verbose=True)
    
#5chat response using predict (prompt template)
chat_reply = llm_conversation.predict(input=input_text)
return chat_reply
