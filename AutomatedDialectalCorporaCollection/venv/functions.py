# encoding: utf-8
from __future__ import unicode_literals
from locations import *
from variables import *
import unicodedata as ud
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import itertools
from nltk import word_tokenize
import os
import pandas as pd
import csv
count_words=0

def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text


def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)

def remove_arabicNumbers(text):
    no = str.maketrans('', '', arabic_numbers)
    return text.translate(no)

def remove_languages(text):
    translationTable = str.maketrans("éàèùâêîôûç", "eaeuaeiouc")
    text = text.translate(translationTable)
    return re.sub(r'[a-zA-Z0-9]+', '', text)

def remove_tatweel(text):
    text = re.sub("ـ", "", text)
    return text

def clean(text):
    # emojis
    text = emoji_pattern.sub(r'', text)
    # mentions
    text = re.sub('@[^\s]+', ' ', text)
    #URLs images and videos
    text = re.sub('http\S+', ' ', text)
    return text
####################NORMALIZATION ######################
def normalizeArabic(text):
    # alef
    text = re.sub("[إأٱآا]", "ا", text)
    # yeh
    text = re.sub("ى", "ي", text)
    # hamza on waw
    text = re.sub("ؤ", "ء", text)
    # hamza on yeh
    text = re.sub("ئ", "ء", text)
    # ta marbota
    text = re.sub("ة", "ه", text)
    # kaf
    text = re.sub("گ", "ك", text)
    # lamalef
    text = re.sub("لإ", "لا", text)
    return(text)

####################STOP WORDS REMOVAL ######################
def StopWordsRemoval(Tweet):
    global count_words
    # remove emoticons from tokens
    emoticons = emoticons_happy.union(emoticons_sad)
    stop_words = set(stopwords.words("arabic"))
    word_tokens = word_tokenize(Tweet)
    filtered_sentence = []
    for w in word_tokens:
        if (w not in stop_words) and (w not in emoticons):
            count_words+=1
            filtered_sentence.append(w)
    return filtered_sentence

####################TOKENIZATION ######################
def Tokenize(Tweet):
    global count_words
    # remove emoticons from tokens
    emoticons = emoticons_happy.union(emoticons_sad)
    word_tokens = word_tokenize(Tweet)
    filtered_sentence = []
    for w in word_tokens:
        if (w not in emoticons):
            count_words+=1
            filtered_sentence.append(w)
    return filtered_sentence

####################PRE-PROCESSING ######################
def preprocess(Tweet):
    Tweet = clean(Tweet)
    Tweet = remove_languages(Tweet)
    Tweet = remove_punctuations(Tweet)
    Tweet = remove_arabicNumbers(Tweet)
    return Tweet

####################LENGTHENING REMOVAL ######################
def remove_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}", re.DOTALL)
    text = pattern.sub(r"\1", text)
    return text

####################NLP PROCESSING ######################
def nlp_tasks(Tweet):
    # diacrities (tashkeel)
    Tweet = remove_diacritics(Tweet)
    # tatweel
    Tweet = remove_tatweel(Tweet)
    # characters lengtheneing
    Tweet = remove_lengthening(Tweet)
    return Tweet

####################WRITING ON A FILE ######################
def generate_output(i, tokens, x, tf):
    tf.write(str(i) + " , " + str(tokens) + " , " + (' '.join(tokens)) + " , " + x + "\n")

####################ALL TASKS ######################
def fun(file_name, flag,file1, file2 ):

    global count_words
    count_words = 0
    emoticons = emoticons_happy.union(emoticons_sad)
    #read CSV file
    file = open(file_name, encoding="utf8")
    colnames = ['Index', 'tweet', 'Dialect']
    df = pd.DataFrame(columns=['id', 'tweet', 'dialect'])
    df = pd.read_csv(file_name, names=colnames)
    tweets = df.tweet.tolist()
    dialect=df.Dialect.tolist()
    dlc=dialect[1]

    txt_file = file1 + dlc + ".csv"
    arff_file = file2 + dlc + ".arff"

    # Emoji patterns
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    #Write file open
    tf = open(txt_file, 'w', encoding='utf-8-sig', newline='')
    tf2 = open(arff_file, 'w', encoding='utf-8', newline='')
    writer = csv.writer(tf)
    writer2 = csv.writer(tf2)
    i=1
    arf="@RELATION "+dlc+"\n" \
                         "@ATTRIBUTE  id numeric \n" \
                         "@ATTRIBUTE tweets string \n" \
                         "@ATTRIBUTE  dialect {"+dlc+"} \n" \
                         "@DATA \n"
    tf2.write(arf)
    writer.writerow(["id", "Tweet"," Tokens","Dialect"])
    iterTweet = iter(tweets)
    next(iterTweet)
    for Tweet in iterTweet:
        # remove retweets

        if ('RT @' not in Tweet):
            Tweet = preprocess(Tweet)
            Tweet = nlp_tasks(Tweet)
            Tweet = normalizeArabic(Tweet)
            if (flag==True):
                final_tweet = StopWordsRemoval(Tweet)
            else:
                final_tweet= Tokenize(Tweet)
            arff_line = str(i) + " , \"" + (' '.join(final_tweet)) + "\" , " + dlc + "\n"
            writer.writerow([str(i), "\""+' '.join(final_tweet)+"\"","\""+str(final_tweet)+"\"", dlc])
            tf2.write(arff_line)
            i+=1

    tf.close()
    print(dlc+" --- lines: "+str(i)+" ,words:"+str(count_words))
    return i

####################UNNECESSARY INDENT ######################
def stream(mystr):

    mystr = mystr.replace('\n', ' ')
    mystr = mystr.replace('\t', ' ')
    mystr = mystr.replace('|', ' ')
    mystr = "\"" + mystr + "\""
    return mystr

####################FILES MERGING ######################
def mergeFiles(filenames, N, status,outfile):
    n=0
    with open(outfile+status+'_merged.arff','w', encoding='utf-8', newline='') as outfile:
        str="@RELATION Dialects\n" \
            "@ATTRIBUTE  id numeric \n" \
            "@ATTRIBUTE tweets string\n" \
            "@ATTRIBUTE  dialect {"
        first =True
        for c in N:
            if first:
                str+=c
                first=False
            else: str+=", "+c
        str+=" }\n" \
        "@DATA \n"
        outfile.write(str)
        for fname in filenames:
            with open(fname,encoding='utf-8') as infile:
                for _ in range(5):
                    next(infile)
                for line in infile:
                        n+=1
                        outfile.write(line)
    return n
