#create the embedding variable

word_embeddings = tf.get_variable(“word_embeddings”,[vocabulary_size, embedding_size])

# use the tf.nn.embedding_lookup function

embedded_word_ids = tf.nn.embedding_lookup(word_embeddings, word_ids)