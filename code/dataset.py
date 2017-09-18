#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
from pprint import pprint
import requests
import json
import codecs

#sSENHA DE ACESSO AO FACEBOOK   https://developers.facebook.com/tools/explorer/145634995501895/?method=GET&path={event-id}&version=v2.5
#senha = raw_input('senha da graph api: ')
senha = 'EAACEdEose0cBALCsRirU7BScAWLrlqnRiADS9NshJcYbGYVL5zsLOhM20oKjuZBUalvlCYR6s6ZBoUu4AD0c6uuTP75WmV8CSOPGSe76f3MxncaLV6ZAwRXI1neouWfg81JL6rOJoUG9jhzDKroGjenEXYFkZBC9b2KNgBNGIGdtQX6pJBcFhz7Kn5wrZCAwi25nQKrtKuQZDZD'
id_local = raw_input('id da casa de show: ')
#senha = 'EAACEdEose0cBABMZC0jYrjxBKkbXTSZAdkncNG8ymcQVJIm5BOKD0Fri3DGWDDZAkZAGiCBsEfIhooZCbfeT0zm888kIfjCS2AiUwgQgaqXNdX07cEcCXca8loFX2g2vIhah1EY8IEl2pVLT6FZBOt5zdsPSSUPXmwzoRIjlbwbTqMpZBiEOVDH5IvitKP0xR0gMogsMUG59QZDZD'
#id_local = '190661070997227'
nEventos = raw_input('Digite o numero maximo de eventos: ')
#nPessoas = raw_input('Digite o numero maximo de perfis: ')
#nEventos = '10'
#nPessoas = '1500'
#arq_saida = raw_input('digite o nome para o dataset: ')
arq_saida = id_local
dataset = open("../"+arq_saida, 'a')

e = requests.get("https://graph.facebook.com/v2.10/"+id_local+"?fields=events.limit("+nEventos+"){id}&access_token="+senha)

events = e.text
eventosJson = json.loads(events)
#pprint (eventosJson)
size = len(eventosJson['events']['data'])
count = 0
listaEventos = []
while (count < size):
    listaEventos.append(eventosJson['events']['data'][count]['id'])
    count = count + 1


for idEvento in listaEventos:
    r = requests.get("https://graph.facebook.com/v2.10/"+idEvento+"?fields=start_time,interested.limit(5000){id}&access_token="+senha)
    dados = r.text
    data = json.loads(dados)
    tam = len(data['interested']['data'])
    count2 = 0
    dataset.write(data['id']+","+data['start_time']+",")
    while (count2 < tam):
        dataset.write(data['interested']['data'][count2]['id']+",")
        count2 = count2 +1
    dataset.write('\n')



'''
    count = 0
    while (count < tam):
        dataJ = data['interested']['data'][count]
        dataset.write(data['id']+","+data['start_time']+",")
        count = count +1
        dataA = dataJ['interested']
        dataA = dataA['data']
        tam2 = len(dataA)
        print tam2
        count2 = 0

        while (count2 < tam2):
            dataset.write(dataA[count2]['id']+",")
            count2 = count2 +1
        dataset.write('\n')
'''
