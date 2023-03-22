import streamlit as st
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pickle
import numpy as np
import tensorflow as tf
#from sklearn.ensemble import IsolationForest


# loading the saved model
loaded_model = pickle.load(
    open('/home/manas/Elite16/SavedModels/IsolationForest.pkl', 'rb'))

st.set_page_config(
    page_title="CODE REVIEW BOT ",
    layout="centered",
    initial_sidebar_state="expanded",
)

bot = ChatBot('MyBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english.greetings')

st.title('Greetings user')
st.write('Enter a message and the bot will respond or Enter a python snippet.')

user_input = st.text_input('User Input')


if user_input:
    bot_response = bot.get_response(user_input)
    st.write('Bot Response: {}'.format(bot_response))
    

def vectorize_program(program):
    # Tokenize and vectorize the program
    tokenizer = tf.keras.preprocessing.text.Tokenizer()
    tokenizer.fit_on_texts([program])
    sequence = tokenizer.texts_to_sequences([program])[0]
    padded_sequence = tf.keras.preprocessing.sequence.pad_sequences([sequence])
    vectorized_program = tf.one_hot(padded_sequence, depth=len(tokenizer.word_index)+1)

    # Reshape the program vector to match the expected shape for the Isolation Forest model
    num_features = 36
    max_len = max(len(sequence), 1)
    num_tokens = min(vectorized_program.shape[1], num_features)
    vectorized_program_2d = np.zeros((1, num_features))
    vectorized_program_2d[0, :num_tokens] = vectorized_program[0, :num_tokens, 0]

    return vectorized_program_2d




# Define the Streamlit app
st.title("Anomaly Detector for Python Code")

# Ask the user to input a Python code snippet
program = st.text_area("Enter a Python code snippet:")

# Vectorize the program
vectorized_program = vectorize_program(program)

# Use the trained model to predict anomalies in the user-input program
predictions = loaded_model.predict(vectorized_program)

# Print the number of anomalies detected
st.write("Number of anomalies detected:", sum(predictions == -1))
    

