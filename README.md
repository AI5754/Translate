# Translate

## Server

The server is a django program running on default port (8000).

| API                  |                output                 |                                                                 Parameters |
| -------------------- | :-----------------------------------: | -------------------------------------------------------------------------: |
| translate/languages/ | returns a list of supported languages |                                                                            |
| translate/           |         translates plain text         | text: text to translate, langIn: origin language, langOut: target language |
| translate/json/      |           translates a json           | json: json to translate, langIn: origin language, langOut: target language |

For translations it uses google translate service of rapid api

## Client

The client is a Vue.js program running on default port (8000).

It supports translations of user input as well as file uploads (txt and json).
