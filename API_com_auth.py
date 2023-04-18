# Documentação da API para Python:
# https://developers.google.com/resources/api-libraries/documentation/calendar/v3/python/latest/index.html?hl=pt-br

import requests
import datetime
import os.path

# Bibliotecas do Google Developer para Autenticação
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

token_login = None


# Cria um Token de login. "Permanecer logado".
if os.path.exists('token.json'):
    token_login = Credentials.from_authorized_user_file('token.json')
else:
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    token_login = flow.run_local_server(port=0)

    with open('token.json', 'w') as token:
        token.write(token_login.to_json())

# Identifica o serviço do Google que vai ser acessado pelo programa:
service = build('calendar', 'V3', credentials=token_login)

# Requisitar eventos agendados no Google Calendar:
events = service.events().list(calendarId='primary', maxResults=5, singleEvents = True, orderBy='startTime').execute()

# Requisita apenas os 'items' do evento
events_itens = events.get('items', [])

# Printa os eventos agendados a data e a hora
print('Eventos agendados:\n')
for event in events_itens:
    print("Nome do evento: "+ str(event['summary']) + " || Data e hora: " + str(event['start']['dateTime']))

