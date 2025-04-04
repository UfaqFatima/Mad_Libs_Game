import streamlit as st
import random 

# Streamlit app title
st.title("Fun Mad Libs Game!")

# Sidebar for user input
st.sidebar.header("Fill in the blanks")

# Taking user input
adjective = st.sidebar.text_input("Enter an adjective")
verbs1 = st.sidebar.text_input("Enter a verb")
verbs2 = st.sidebar.text_input("Enter another verb", "innovate")
famous_person = st.sidebar.text_input("Enter a famous person")

# Fun Sentences
madlib_template = [
    f"Python is so {adjective}! Day by day it makes me confident to create more apps compared to other languages, to {verbs1}, stay connected, and {verbs2} like your idol {famous_person}.",
    f"Coding is very {adjective}! It helps to {verbs2} apps more easily like {famous_person}.",
    f"Success is {adjective}. If you want to be like {famous_person}, you must {verbs1} every day and never forget to {verbs2}!"
]

# Button to Generate Mad Libs
if st.button("Generate Mad Lib"):
    selected_madlib = random.choice(madlib_template)
    st.subheader("Here's Your Mad Lib:")
    st.write(selected_madlib)

# Footer
st.markdown("**Made with love by Ufaq Fatima**")