# Translate

## Server

The server is a django program running on default port (8000).

| API                  |                output                 |                                                                 Parameters |
| -------------------- | :-----------------------------------: | -------------------------------------------------------------------------: |
| translate/languages/ | returns a list of supported languages |                                                                            |
| translate/           |         translates plain text         | text: text to translate, langIn: origin language, langOut: target language |
| translate/json/      |           translates a json           | json: json to translate, langIn: origin language, langOut: target language |

For translations it uses google translate service of rapid api.

### Deployment

Information about deployment can be found [here](https://docs.djangoproject.com/en/3.0/howto/deployment/).

## Client

The client is a Vue.js program running on default port (8000).

It supports translations of user input as well as file uploads (txt and json).

### Deployment

Information about deployment can be found [here](https://cli.vuejs.org/guide/deployment.html#general-guidelines).
For deployment on a linux server I recommend ubuntu, where it is quite easy to setup secured traffic (https) (e.x. [certbot](https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx)) and routing (e.x. [nginx](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/))
