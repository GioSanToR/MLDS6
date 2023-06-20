import tensorflow as tf

#Modelo

input = tf.keras.layers.Input((x_new.shape[1],x_new.shape[2]))
#capa LSTM con dimensión latente de 288
capa_LSTM = tf.keras.layers.LSTM(288,return_sequences=True)(input)
#dropout
dropout = tf.keras.layers.Dropout(0.1)(capa_LSTM)
#segunda capa LSTM con dimensión latente de 288
capa_LSTM = tf.keras.layers.LSTM(288)(dropout)
#segunda capa dropout
dropout = tf.keras.layers.Dropout(0.1)(capa_LSTM)
#capa densa con activación relu
dense = tf.keras.layers.Dense(288,activation='relu')(dropout)
#capa densa con activación softmax
output = tf.keras.layers.Dense(len(note2ind),activation='softmax')(dense)
model = tf.keras.models.Model(input, output)
model.summary()

tf.keras.utils.plot_model(model,show_shapes=True)

#Entrenamiento

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.003),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
best_callback = tf.keras.callbacks.ModelCheckpoint(filepath="LSTM.h5",
                                                      monitor="val_loss",
                                                      verbose=True,
                                                      save_best_only=True,
                                                      save_weights_only=True,
                                                      mode="min")
history = model.fit(x_train,y_train, batch_size=128,epochs=100, validation_data=(x_test,y_test))


