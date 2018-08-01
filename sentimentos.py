#importando as bibliotecas
from textblob import TextBlob as tb
import tweepy
import numpy as np

#variáveis para armazenar nossas informações de autenticação
consumer_key = 'SUA CONSUMER KEY'
consumer_secret = 'SUA CONSUMER SECRET'
access_token = 'SEU ACCESS TOKEN'
access_token_secret = 'SEU ACCESS TOKEN SECRET'

#variáveis que irão realizar o login na API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Variável que irá armazenar todos os Tweets com a palavra escolhida na função search da API
public_tweets = api.search('eleição') #escolhi a palavra eleição

#Variável que irá armazenar as polaridades 
analysis = None

tweets = [] # Lista vazia para armazenar scores

# imprime todos os tweets e, em seguida, a polaridade
for tweet in public_tweets:
    print(tweet.text)
    analysis = tb(tweet.text)
    polarity = analysis.sentiment.polarity 
    tweets.append(polarity)
    print(polarity)
	#A função sentiment.polarity retornará um número entre -1 e 1, onde quanto maior esse número, menos chateada a pessoa estará.
	
print('Média dos sentimentos analisados: ' + str(np.mean(tweets)))