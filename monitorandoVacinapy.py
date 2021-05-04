import requests as req
from bs4 import BeautifulSoup

import datetime
import time

from playsound import playsound

from configuracoes import busca, horario


horario_busca = datetime.datetime.strptime(horario, "%H:%M") - datetime.timedelta(minutes=15)

link_atual = "https://vacinapira.piracicaba.sp.gov.br/cadastro/blk_inicial/"
link_antigo = "https://web.archive.org/web/20210305165929/https://vacinapira.piracicaba.sp.gov.br/cadastro/blk_inicial/"
link_antigo2 = "https://web.archive.org/web/20210501110705/https://vacinapira.piracicaba.sp.gov.br/cadastro/blk_inicial/"

def monitorar_vacinas(link, str_busca):
    resp = req.get(link).text
    soup = BeautifulSoup(resp, features="html5lib")
    row = soup.find_all("div", {"class": "row"})[0]

    classes = row.find_all("fieldset", {"class": "documentos"})
    classes = list(map(lambda x: x.find_all("p")[1].text, classes))

    if len(classes) == 0:
        print("Nada ainda...")
    else:
        for classe in classes:
            print(classe)
            if str_busca in classe:
                playsound("alerta.mp3")


while True:
    agora = datetime.datetime.now()
    datetime_busca = agora.replace(hour=horario_busca.hour, minute=horario_busca.minute, second=0, microsecond=0)
    if agora >= datetime_busca:
        print()
        print("Acessando o site...")
        try:
            monitorar_vacinas(link_atual, busca)
            time.sleep(60)
        except:
            print("Falhou")

