import nltk
import streamlit as st 
from nltk.chat.util import Chat,reflections
import re


pairs = [
  
    (r"hi|hello|hey", ["Hello! I'm your movie assistant.", "Hi there! Ready to talk about movies?"]),
    (r"what is your name?", ["I'm the MovieBot!", "Call me your Movie Assistant."]),
    (r"how are you?", ["I'm just a bot, but I'm here to help!", "I'm doing great! What about you?"]),

  
    (r"can you recommend a movie?", ["Sure! Try watching 'Inception', 'Interstellar', or 'The Dark Knight'."]),
    (r"what are some good action movies?", ["Some great action movies are 'Mad Max: Fury Road', 'John Wick', and 'Gladiator'."]),
    (r"what are some good comedy movies?", ["You might like 'Superbad', 'Step Brothers', or 'The Hangover'."]),
    (r"what are some good horror movies?", ["Try 'The Conjuring', 'Get Out', or 'Hereditary'."]),
    (r"what are some good sci-fi movies?", ["Check out 'Blade Runner 2049', 'The Matrix', or 'Ex Machina'."]),
    (r"what are some good animated movies?", ["You should watch 'Toy Story', 'Spider-Man: Into the Spider-Verse', or 'Frozen'."]),
    (r"what are some good romantic movies?", ["Try 'The Notebook', 'La La Land', or 'Pride and Prejudice'."]),

  
    (r"what is a (.*) movie?", ["A %1 movie is a film that falls into the %1 genre, featuring typical themes and elements."]),
    (r"tell me about (.*) movies", ["%1 movies are known for their unique style and themes. Would you like some recommendations?"]),

  
    (r"who directed (.*)?", ["I'm not sure, but you can check IMDb for director information."]),
    (r"who starred in (.*)?", ["I can’t look up actors, but IMDb can help you find the cast."]),
    (r"what is the plot of (.*)?", ["I don’t have the plot details, but you can find them on IMDb or Wikipedia."]),
    (r"when was (.*) released?", ["I don’t have the release date, but you can check IMDb for that information."]),

  
    (r"is (.*) a good movie?", ["I don’t rate movies, but you can check reviews on IMDb or Rotten Tomatoes."]),
    (r"what is the rating of (.*)?", ["I don’t have the rating, but you can check IMDb or Rotten Tomatoes for reviews."]),

  
    (r"tell me a movie fact", ["Did you know? The highest-grossing movie of all time is 'Avatar'!", 
                               "Fun fact: 'The Shawshank Redemption' is often considered the best movie of all time!"]),
    (r"what is the best movie ever?", ["That’s subjective, but many people love 'The Godfather', 'The Shawshank Redemption', or 'Inception'."]),

  
    (r"what can you do?", ["I can recommend movies, tell you about genres, and share fun movie facts!"]),
    (r"help", ["I can help you with movie recommendations, genres, and more. Just ask!"]),
    (r"thank you|thanks", ["You're welcome!", "No problem! Happy to help!"]),
    (r"bye|goodbye", ["Goodbye! Enjoy your movies!", "See you later!"]),

  
    (r"(.*)", ["Sorry, I don't have information about that. Try asking about movies!"])
]


chatbot = Chat(pairs,reflections)

st.title('Movie Chatbot')
st.write('Ask me about movies! Type your question below.')

user_input = st.text_input('You:')

if user_input:

    response = chatbot.respond(user_input.lower())
    st.text(f"MovieBot: {response}")

