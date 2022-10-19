import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

def carregar_pag():
    link_page = "https://dados.gov.br/dataset/sistema-nacional-de-estatisticas-de-seguranca-publica/resource/03af7ce2-174e-4ebd-b085-384503cfb40f"
    html_page = requests.get(link_page).content
    html_page = bs(html_page,"html.parser")
    url_link = html_page.find("p",{"class":"muted ellipsis"}).find("a").text
    return url_link

def capt_planilha(url):

    load_planilha = requests.get(url).content
    planilha = pd.read_excel(load_planilha)
    print(planilha)
    return planilha


if __name__ == "__main__":
    url = carregar_pag()
    capt_planilha(url)
