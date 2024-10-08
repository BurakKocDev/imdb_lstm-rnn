from keras.layers import SimpleRNN
from keras.models import Sequential
from keras.layers import Embedding


#örnek rnn
model = Sequential()
model.add(Embedding(1000, 32))
model.add(SimpleRNN(32))
model.summary()
#boyutlandırılmış rnn
model = Sequential()
model.add(Embedding(1000, 32))
model.add(SimpleRNN(32, return_sequences=True))
model.summary()

#ardışık rnn
model = Sequential()
model.add(Embedding(1000, 32))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32, return_sequences=True))
model.add(SimpleRNN(32))
model.summary()

from keras.datasets import imdb
from keras.preprocessing import sequence

num_features = 1000
maxlen = 500
batch_size = 32

print('Load data..')
(input_train, y_train), (input_test, y_test) = imdb.load_data(num_words = num_features)



print(len(input_train), 'Eğitim dizisi', input_train.shape)
print(len(input_test), 'test dizisi', input_test.shape)
print('Pad sequnce (sample x train)')

input_train = sequence.pad_sequences(input_train, maxlen=maxlen)
input_test = sequence.pad_sequences(input_test, maxlen=maxlen)


print(len(input_train), 'Eğitim dizisi', input_train.shape)
print(len(input_test), 'test dizisi', input_test.shape)

from keras.layers import Dense
from keras import layers

#basit rnn ile modelleme
model = Sequential()
model.add(Embedding(num_features, 32))
model.add(SimpleRNN(32))
model.add(Dense(1, activation='sigmoid'))
model.summary()

#basit lstm ile modelleme
model = Sequential()
model.add(layers.Embedding(num_features, 32))
model.add(layers.Bidirectional(layers.LSTM(32)))
model.add(Dense(1, activation='sigmoid'))
model.summary()


#modelin derlenmesi rnn
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history = model.fit(input_train, y_train,
                    epochs = 10,
                    batch_size = 128,
                    validation_split=0.2)



#modelin derlenmesi lstm
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['acc'])

history = model.fit(input_train, y_train,
                    epochs = 10,
                    batch_size = 128,
                    validation_split=0.2)


import matplotlib.pyplot as plt

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)


plt.plot(epochs, acc, 'm*-', label= 'Eğitim Başarımı')
plt.plot(epochs, val_acc, 'g*-', label= 'Doğrulama / Geçerleme Başarımı')
plt.title('Eğitim ve Doğrulama için Başarım')
plt. legend()

plt.figure()

plt.plot(epochs, loss, 'm*-', label= 'Eğitim Kaybı')
plt.plot(epochs, val_loss, 'g*-', label= 'Doğrulama / Geçerleme Kaybı')
plt.title('Eğitim ve Doğrulama için Kayıp')
plt. legend()

plt.show()

print(acc, 'eğitim başarımları')

acc = history.history['acc']
val_acc = history.history['val_acc']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'm*-', label= 'Eğitim Başarımı')
plt.plot(epochs, val_acc, 'g*-', label= 'Doğrulama / Geçerleme Başarımı')
plt.title('Eğitim ve Doğrulama için Başarım')
plt. legend()

plt.figure()

plt.plot(epochs, loss, 'm*-', label= 'Eğitim Kaybı')
plt.plot(epochs, val_loss, 'g*-', label= 'Doğrulama / Geçerleme Kaybı')
plt.title('Eğitim ve Doğrulama için Kayıp')
plt. legend()

plt.show()


