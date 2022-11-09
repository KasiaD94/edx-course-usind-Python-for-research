# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:38:05 2020

@author: Kasia
"""
#import os
import pandas as pd
#import numpy as np
from collections import Counter

def count_words_fast(text):
    """Seperates characters in text"""
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """Read the text from path"""
    text   = pd.read_csv(title_path, sep = "\n", engine='python', encoding="utf8")
    text = text.to_string(index = False)
    return text

def word_stats(word_counts):
    """Take text and returns number all words appered in text and list of number of times
    each word appeared in text"""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

hamlets = pd.read_csv("hamlets.csv", index_col=0)
#print(hamlets)
#language, text = hamlets.iloc[0]
#print(language)

def summarize_text(language, text):
    """Takes language and text and creates Dataframe ith language, frequency, mean length
    of word and number of words in appropriate category"""
    counted_text = count_words_fast(text)
    list_keys = list(counted_text.keys())
    list_values = list(counted_text.values())
    data = pd.DataFrame({"word": list_keys, "count": list_values})
    #print(data.loc[data['word'] == 'hamlet'])
    
    data['length'] = data['word'].str.len()
    
    def check_frequency(row):
        if row['count'] > 10:
            frequency = "frequent"
        elif (row['count'] > 1) and (row['count'] <= 10):
            frequency = "infrequent"
        elif row['count'] == 1:
            frequency = "unique"
        return frequency
    
    data['frequency'] = data.apply(check_frequency, axis=1)
    #print(data[data['frequency'] == "unique"].count())
    #data.groupby('frequency').count()
    mean_word_length = data.groupby('frequency')['length'].mean()
    num_words = data.groupby('frequency')['word'].count()
    sub_data = pd.DataFrame({"language": language, 
                             "frequency": ["frequent", "infrequent", "unique"],
                             "mean_word_length": mean_word_length,
                             "num_words": num_words})
    return(sub_data)

language = []
text = []
text_ind = 1
lang_ind = 0
for i in range(3):
    language.append(hamlets.iloc[i][lang_ind])
    text.append(hamlets.iloc[i][text_ind])
columns = ["language", "frequency", "mean_word_length", "num_words"]
grouped_data = pd.DataFrame(columns=columns)

for i in range(3):
    sub_data = summarize_text(language[i], text[i])
    grouped_data = grouped_data.append(sub_data)
   
#print(grouped_data)

colors = {"Portuguese": "green", "English": "blue", "German": "red"}
markers = {"frequent": "o","infrequent": "s", "unique": "^"}
import matplotlib.pyplot as plt
for i in range(grouped_data.shape[0]):
    row = grouped_data.iloc[i]
    plt.plot(row.mean_word_length, row.num_words,
        marker=markers[row.frequency],
        color = colors[row.language],
        markersize = 10
    )

color_legend = []
marker_legend = []
for color in colors:
    color_legend.append(
        plt.plot([], [],
        color=colors[color],
        marker="o",
        label = color, markersize = 10, linestyle="None")
    )
for marker in markers:
    marker_legend.append(
        plt.plot([], [],
        color="k",
        marker=markers[marker],
        label = marker, markersize = 10, linestyle="None")
    )
plt.legend(numpoints=1, loc = "upper left")

plt.xlabel("Mean Word Length")
plt.ylabel("Number of Words")
plt.show();