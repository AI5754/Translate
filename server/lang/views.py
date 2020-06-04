from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

import requests
import json

url = "https://google-translate1.p.rapidapi.com/language/translate/v2"
xRapidapiHost = "google-translate1.p.rapidapi.com"
xRapidapiKey = "Your Rapid API key"
acceptEncoding = "application/gzip"
contentType = "application/x-www-form-urlencoded"


def languages(request):
    headers = {
        'x-rapidapi-host': xRapidapiHost,
        'x-rapidapi-key': xRapidapiKey,
        'accept-encoding': acceptEncoding
    }

    response = requests.request("GET", url + "/languages", headers=headers)
    langs = response.json().get('data').get('languages')

    langsFormatted = []
    for lang in langs:
        langsFormatted.append(lang.get('language'))

    return JsonResponse(langsFormatted, safe=False)


def translate(request):
    headers = {
        'x-rapidapi-host': xRapidapiHost,
        'x-rapidapi-key': xRapidapiKey,
        'accept-encoding': acceptEncoding,
        'content-type': contentType
    }

    text = request.GET['text']
    langIn = request.GET['langIn']
    langOut = request.GET['langOut']
    payload = f"source={langIn}&q={text}&target={langOut}"

    response = requests.request("POST", url, data=payload, headers=headers)
    return HttpResponse(response.json().get('data').get('translations')[0].get('translatedText'))


def translateJsonFile(request):
    headers = {
        'x-rapidapi-host': xRapidapiHost,
        'x-rapidapi-key': xRapidapiKey,
        'accept-encoding': acceptEncoding,
        'content-type': contentType
    }

    textJson = json.loads(request.GET['json'])
    langIn = request.GET['langIn']
    langOut = request.GET['langOut']

    textList = []
    jsonToList(textJson, textList)

    payload = f"source={langIn}&target={langOut}"
    for t in textList:
        payload += f"&q={t}"

    response = requests.request("POST", url, data=payload, headers=headers)
    translations = response.json().get('data').get('translations')

    keyValueTranslations = {}
    for ind, t in enumerate(translations):
        keyValueTranslations[textList[ind]] = t['translatedText']

    translateJson(textJson, keyValueTranslations)

    return JsonResponse(textJson, safe=False)


def jsonToList(textJson: dict, textList: []):
    for v in textJson:
        if (type(textJson[v]) is dict):
            jsonToList(textJson[v], textList)
        elif (type(textJson[v]) is str):
            textList.append(textJson[v])
    return


def translateJson(json, translations):
    for v in json:
        if (type(json[v]) is dict):
            translateJson(json[v], translations)
        elif (type(json[v]) is str):
            json[v] = translations[json[v]]
    return
