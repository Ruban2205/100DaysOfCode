# Implement a recurrent neural network (RNN) for text generation.
print("\nRuban Gino Singh - Day75 of #100DaysOfCode\n")

print("Python program to implement recurrent neural network (RNN) for text generation.\n")

import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

text = open('your_text_data.txt', 'r').read()
vocab = sorted(set(text))
char_to_index = {char: index for index, char in enumerate(vocab)}
index_to_char = {index: char for index, char in enumerate(vocab)}
text_as_int = np.array([char_to_index[char] for char in text])

seq_length = 100
examples_per_epoch = len(text) // (seq_length + 1)
char_dataset = tf.data.Dataset.from_tensor_slices(text_as_int)

sequences = char_dataset.batch(seq_length + 1, drop_remainder=True)

def split_input_target(chunk):
    input_text = chunk[:-1]
    target_text = chunk[1:]
    return input_text, target_text

dataset = sequences.map(split_input_target)

BATCH_SIZE = 64
BUFFER_SIZE = 10000
dataset = dataset.shuffle(BUFFER_SIZE).batch(BATCH_SIZE, drop_remainder=True)

vocab_size = len(vocab)
embedding_dim = 256
rnn_units = 1024

model = Sequential([
    Embedding(vocab_size, embedding_dim, batch_input_shape=[BATCH_SIZE, None]),
    LSTM(rnn_units, return_sequences=True, stateful=True, recurrent_initializer='glorot_uniform'),
    Dense(vocab_size)
])

model.compile(optimizer='adam', loss=tf.losses.SparseCategoricalCrossentropy(from_logits=True))

EPOCHS = 10
history = model.fit(dataset, epochs=EPOCHS)

def generate_text(model, start_string, num_generate=1000, temperature=1.0):
    input_eval = [char_to_index[s] for s in start_string]
    input_eval = tf.expand_dims(input_eval, 0)

    text_generated = []

    model.reset_states()
    for i in range(num_generate):
        predictions = model(input_eval)
        predictions = tf.squeeze(predictions, 0) / temperature
        predicted_id = tf.random.categorical(predictions, num_samples=1)[-1,0].numpy()

        input_eval = tf.expand_dims([predicted_id], 0)

        text_generated.append(index_to_char[predicted_id])

    return (start_string + ''.join(text_generated))

generated_text = generate_text(model, start_string='The ', num_generate=500, temperature=0.8)
print(generated_text)

# --------------------------------------------------------- #