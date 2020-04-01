# -*- coding: utf-8 -*- 
import os, json, glob, sys, numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import keras.backend.tensorflow_backend as K
import tensorflow as tf
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, Flatten, Dropout, Input, Conv1D, MaxPooling1D, GlobalMaxPool1D
from keras.utils import np_utils
from keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.model_selection import train_test_split
from sqlalchemy import create_engine
import pymysql

def Model():
    config = tf.ConfigProto()
    config.gpu_options.allow_growth = True
    session = tf.Session(config=config)
    
    #os.chdir("./data_after_preprocessing_data")
    #data = pd.read_csv('./after_preprocessing_data/after_prepro.csv')
    engine = create_engine('mysql+pymysql://DAN:dudeks7052@localhost/AI',convert_unicode=True)
    conn = engine.connect()

    data = pd.read_sql_table('after_prepro', conn)
    
    df2 = data.sample(frac=1).reset_index(drop=True)
    print(df2.iloc[0:10,1])
    
    print(len(df2.iloc[:, 0]))
    
    X = df2.iloc[:, 0].values
    y = df2.iloc[:, 1].values
    print(y)
    
    print(len(X), len(y))
    
    nb_classes = len(set(y))
    print(nb_classes)
    y = np_utils.to_categorical(y, nb_classes)
    print(y)
    
    
    max_word = 5000
    max_len = 500
    
    tok = Tokenizer(num_words = max_word)
    tok.fit_on_texts(X)
    print(len(tok.word_index))
    
    sequences = tok.texts_to_sequences(X)
    print(len(sequences[0]))
    print(sequences[0])
    print(len(tok.word_index))
    
    sequences_matrix = sequence.pad_sequences(sequences, maxlen=max_len)
    print(sequences_matrix)
    print(sequences_matrix[0])
    print(len(sequences_matrix[0]))
    
    print(len(tok.word_index))
    
    X_train, X_test, y_train, y_test = train_test_split(sequences_matrix, y, test_size=0.2)
    
    print(X_train.shape)
    print(y_train.shape)
    
    with K.tf_ops.device('/device:GPU:0'):
        model = Sequential()
        
        model.add(Embedding(max_word, 64, input_length=max_len))
        model.add(LSTM(60, return_sequences=True))
        model.add(GlobalMaxPool1D())
        model.add(Dropout(0.2))
        model.add(Dense(50, activation='relu'))
        model.add(Dropout(0.5))
        model.add(Dense(nb_classes, activation='softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        model_dir = '/Users/noyeongdan/Downloads/Spring4/AISpring/src/main/webapp/WEB-INF/views/model'
        if not os.path.exists(model_dir):
            os.mkdir(model_dir)
        model_path = model_dir + "/lstm.model"
        checkpoint = ModelCheckpoint(filepath=model_path, monitor="val_loss", verbose=1, save_best_only=True)
        
        early_stopping = EarlyStopping(monitor='val_loss', patience=7)
    
    model.summary()
    
    hist = model.fit(X_train, y_train, batch_size=500, epochs=20, validation_split=0.2, callbacks=[checkpoint, early_stopping])
    
    print("정확도 : %.4f" % (model.evaluate(X_test, y_test)[1]))
    
    evaluate = model.evaluate(X_test, y_test)[1]
    correct = round(evaluate*len(X_test))
    #print(correct,'/',len(X_test))
    print("맞은갯수 : {}/{}".format(int(correct),len(X_test)))
    
    conn = pymysql.connect(host='127.0.0.1', user='DAN', password='dudeks7052', db='AI', charset='utf8')
    curs = conn.cursor()
    conn.commit()
    
    sql = """delete from result"""
    curs.execute(sql)
    
    sql = """insert into result (evaluate,correct,all_data) values (%s, %s,%s)"""
    curs.execute(sql, (evaluate,int(correct),len(X_test)))
    
    conn.commit()
    conn.close()




