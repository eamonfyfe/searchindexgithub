import requests
from flask import *

from flask import Flask, render_template

# -*- coding: utf-8 -*-
# encoding=utf8

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/returnSearch', methods=['POST'])
def get_search():
    search_input = request.form['input']
    endpoint = 'https://eamonssearch.search.windows.net/'
    api_version = '?api-version=2019-05-06'
    headers = {'Content-Type': 'application/json',
               'api-key': '244AD3FC6219953972BC79F560D14C47'}
    searchquery = "&search="

    url = endpoint + "indexes/cosmosdb-index/docs" + api_version + searchquery + search_input
    response = requests.get(url, headers=headers)
    response.headers.setdefault('Content-Type', 'application/json')
    response.headers.setdefault('Access-Control-Allow-Origin', '*')
    foundInSearch = response.json()

    urlads = endpoint + "indexes/cosmosdbadverts-index/docs" + api_version + searchquery + search_input
    responseads = requests.get(urlads, headers=headers)
    responseads.headers.setdefault('Content-Type', 'application/json')
    responseads.headers.setdefault('Access-Control-Allow-Origin', '*')
    foundInSearchAds = responseads.json()
    search_result = []
    for value in foundInSearch['value']:
        print foundInSearch['value']
        search_result.append("author: {}".format(value['author']))
        search_result.append("text: {}".format(value['text'].encode("utf-8")))

    searchad_result = []
    for value in foundInSearchAds['value']:
        searchad_result.append("advert: {}".format(value['advert']))

    return jsonify("Here are your Results! ", search_result, searchad_result)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
