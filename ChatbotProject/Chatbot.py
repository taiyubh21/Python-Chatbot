# Mohammad Taiyub Hussain

# Importing the libraries
import nltk
from nltk.chat.util import Chat, reflections

import gradio as gr

# Importing conversation data from separate Python file
from ConversationData import conversationPairs

# Creating a new chatbot using the conversation pairs
chatbot = Chat(conversationPairs, reflections)

# Error handling for user input
# To be used instead of chatbot.converse()
def newChatbot(userInput, conversation=[]):

    # Appending the user input to the conversation array
    conversation.append("You: " + userInput)
    # Getting response based on user input
    response = chatbot.respond(userInput)
    # If the user input doesn't exist in the conversationData then append error message to conversation array
    if response is None:
        conversation.append("Chatbot: I'm sorry, I don't understand. Please try asking a different question such as:\n"
                            "- What does Artificial Intelligence mean?\n- Give some real world applications of AI\n- Describe machine learning\n- Why is ethics a concern with AI?")
    # Else append the chatbot response to the conversation history
    else:
        conversation.append("Chatbot: " + response)

    # Formatting the conversation array so there is space between each input and output    
    conversationAppend = "\n\n".join(conversation)

    # Clear conversation history
    # Able to view single user input and single chatbot output at one time
    conversation.clear()

    return conversationAppend

# Defining the Gradio interface
Interface = gr.Interface(fn=newChatbot, 
                     inputs=gr.Text(label="User input"), 
                     outputs=gr.Text(label="Chatbot output"),
                     title="Chatbot to discuss public trust in AI systems", 
                     description="Welcome to the AI Chatbot! Feel free to ask me questions about machine learning, AI systems and AI ethics."
                     " Examples of questions I am able to answer: \n - What is meant by Artificial Intelligence? \n - What is the purpose of Artificial Intelligence? \n - Name a few real world uses for AI"
                     "\n - What varieties of AI exist? \n - What can AI do now? \n - Why is ethics a concern with AI? \n\nDisclaimer: This chatbot does not use or store any personal data")

# Running the interface
Interface.launch()
