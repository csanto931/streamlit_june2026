import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice([
    "Hello! Ready to practice some Python today?",
    "Hi there! What would you like to build?",
    "Nice to see you. Let's write some code.",
    "I'm here and ready to help.",
    "That sounds interesting. Tell me more.",
    "Great question!",
    "Let's solve it step by step.",
    "I can help with that.",
    "Want to try a simpler version first?",
    "Let's debug this together.",
    "Can you show me your code?",
    "What output were you expecting?",
    "What output did you actually get?",
    "That error message is a helpful clue.",
    "Let's read the error carefully.",
    "Check your indentation and try again.",
    "You may be missing a colon.",
    "That looks like a syntax issue.",
    "Try printing the variable to inspect it.",
    "Let's test one small part at a time.",
    "Good start!",
    "You're making progress.",
    "Nice job catching that.",
    "That's a smart approach.",
    "Your logic is improving.",
    "You're thinking like a programmer.",
    "Excellent effort.",
    "That was a solid fix.",
    "I like the way you broke that down.",
    "You're getting the hang of it.",
    "Maybe use a list for that.",
    "A dictionary could work well here.",
    "This might be a good place for a loop.",
    "You could use an if statement there.",
    "A function would make that cleaner.",
    "Try storing that in a variable.",
    "This could be a great use for input().",
    "You might want to convert that to an integer.",
    "Consider using len() to check the size.",
    "Maybe sort the data before displaying it.",
    "Let's think about the algorithm.",
    "What are the inputs?",
    "What should the program return?",
    "Can you describe the problem in plain English?",
    "Let's turn the problem into smaller steps.",
    "What happens in the first step?",
    "What should happen next?",
    "Can you repeat that process with a loop?",
    "Is there a pattern in the data?",
    "How would a human solve this manually?",
    "Let's make the chatbot a little friendlier.",
    "That response sounds clear and simple.",
    "Maybe add more variety to the replies.",
    "A random response can make the bot feel more natural.",
    "Keep the responses short and readable.",
    "Try grouping replies by topic.",
    "You could add a fallback response too.",
    "That's a good message for a beginner chatbot.",
    "Maybe make the tone a little more playful.",
    "That would work nicely in a Streamlit app.",
    "Try `random.choice(responses)` here.",
    "Don't forget to import the random module.",
    "Streamlit can display this in a chat-style layout.",
    "You can store chat history in session state.",
    "A button could trigger the bot reply.",
    "A text input box would work well here.",
    "You could show one message at a time.",
    "Try separating user input from bot output.",
    "This would be a fun classroom demo.",
    "Students could customize these responses easily.",
    "Let's improve the user experience.",
    "Can you make that message more specific?",
    "Maybe add encouragement for the user.",
    "Try making the wording more conversational.",
    "That sentence is easy to understand.",
    "Let's rewrite that to sound more natural.",
    "Short messages often work best in chatbots.",
    "Try adding a question at the end.",
    "That reply could guide the user forward.",
    "Maybe make the bot respond with curiosity.",
    "I didn't quite understand that, but I'm still learning.",
    "Can you rephrase that for me?",
    "I'm not sure yet, but let's figure it out together.",
    "Interesting input. Let me think.",
    "I'm still practicing my chatbot skills.",
    "Could you give me a little more detail?",
    "Let's try a different way to ask that.",
    "I'm not certain, but I can still help you explore it.",
    "That one made me think.",
    "I'm a beginner-friendly bot, so simple questions work best.",
    "Let's keep experimenting.",
    "Testing ideas is part of programming.",
    "Every bug teaches us something.",
    "Code, test, revise, repeat.",
    "You're one step closer to a working program.",
    "Small improvements add up quickly.",
    "Practice makes programs better.",
    "Keep going. You're doing well.",
    "Learning to code takes patience.",
    "Let's try one more version."
]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)

st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
