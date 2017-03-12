# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 09:44:33 2017

@author: Jerry
"""
'''
from google.cloud import datastore

client = datastore.Client()
key = client.key('Person')

entity = datastore.Entity(key=key)
entity['name'] = 'Your name'
entity['age'] = 25
client.put(entity)

from oauth2client.client import GoogleCredentials
credentials = GoogleCredentials.get_application_default()
'''

# Imports the Google Cloud client library
from google.cloud import language
import time
# Instantiates a client
language_client = language.Client()
#credentials = GoogleCredentials.get_application_default()
# The text to analyze
#text = 'Hello, world! We Chinses save the world in Oculus. Computer Science is great.'
filepath = 'D:/Jerry/1-Study/6-GirlHackthon/'
savepath = 'D:/Jerry/1-Study/6-GirlHackthon'#'newResult/'
savename = 'name.txt'
f1 = open(filepath + 'Customer Success.txt','rb')

#lines=f1.readlines();
#lines=f1.readlines();

#document = language_client.document_from_text(lines[10].strip('\r\n'))
document = language_client.document_from_text("Ning Ning is a handsome and smart boy. He can do a lot of things")

# Detects the sentiment of the text
#sentiment = document.analyze_sentiment().sentiment
entities = document.analyze_entities().entities
#print document.analyze_syntax()
#print('Text: {}'.format(text))
#print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
time.sleep(0.8)
for entity in entities:
        print('=' * 20)
        print('{:<16}: {}'.format('name', entity.name))
        print('{:<16}: {}'.format('type', entity.entity_type))
        print('{:<16}: {}'.format('metadata', entity.metadata))
        print('{:<16}: {}'.format('salience', entity.salience))
        print('{:<16}: {}'.format('wikipedia_url',
              entity.metadata.get('wikipedia_url', '-')))


# Detects syntax in the document. You can also analyze HTML with:
#   document.doc_type == language.Document.HTML
time.sleep(0.8)
tokens2 = document.analyze_syntax().tokens

for token in tokens2:
    print('{}: {}'.format(token.part_of_speech, token.text_content))