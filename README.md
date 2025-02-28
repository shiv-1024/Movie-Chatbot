# Movie Chatbot

## Overview
This is a simple movie chatbot built using Python, NLTK, and Streamlit. The chatbot interacts with users and provides movie recommendations, genre explanations, and fun movie facts. It is designed to run on a Streamlit web application.

## Features
- Greets users and introduces itself as a movie assistant
- Provides movie recommendations based on genre
- Shares basic movie facts and information
- Responds to user queries using predefined responses
- Simple and interactive user interface using Streamlit

## Requirements
To run this chatbot, you need to install the following dependencies:

```
pip install nltk streamlit
```

## How to Run
1. Install the required dependencies.
2. Save the chatbot script as `movie_chatbot.py`.
3. Run the chatbot using the command:
   ```
   streamlit run movie_chatbot.py
   ```
4. The chatbot interface will open in your web browser, where you can start interacting with it.

## How It Works
- The chatbot uses `nltk.chat.util.Chat` to process user input based on predefined patterns.
- A set of `pairs` contains different regex-based input patterns and their corresponding responses.
- The chatbot is integrated into a Streamlit app, where user input is taken via a text box and responded to dynamically.

## Example Interaction
```
User: hi
MovieBot: Hello! I'm your movie assistant.

User: can you recommend a movie?
MovieBot: Sure! Try watching 'Inception', 'Interstellar', or 'The Dark Knight'.
```

## Questions Users Can Ask
```
hi
hello
hey
what is your name?
how are you?
can you recommend a movie?
what are some good action movies?
what are some good comedy movies?
what are some good horror movies?
what are some good sci-fi movies?
what are some good animated movies?
what are some good romantic movies?
what is a [genre] movie?
tell me about [genre] movies
who directed [movie name]?
who starred in [movie name]?
what is the plot of [movie name]?
when was [movie name] released?
is [movie name] a good movie?
what is the rating of [movie name]?
tell me a movie fact
what is the best movie ever?
what can you do?
help
thank you
thanks
bye
goodbye
```

## Limitations
- The chatbot relies on predefined responses and does not have a dynamic knowledge base.
- It cannot fetch real-time movie details from external sources like IMDb.

## Future Improvements
- Integrate with an API like IMDb or TMDb to fetch real-time movie information.
- Enhance chatbot responses with NLP models for better user interaction.
- Add more genres and refine recommendations.

## License
This project is for educational purposes and is open-source.

---
Feel free to modify and enhance the chatbot as per your requirements!

