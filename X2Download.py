from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pytube import Playlist
import time
import os


playlistURL = input("Cole o link da Playlist:  ")
playlistNome = input("Qual o nome da Playlist:  ")
driver = webdriver.Firefox()
i = 0

def Organizer(playlist):
    os.system('clear')
    print('Preparando para organizar sua playlist')
    dir = playlist
    os.system('clear')
    origem = 'C:/Users/edley/Downloads/'
    print('Buscando músicas em: ' + origem)
    os.makedirs(origem+dir) 
    destino = origem+dir
    os.system('clear')
    print('Suas músicas serão salvas em: '+destino)
    number = 1
    for diretorio, subpastas, arquivos in os.walk(origem):
        for arquivo in arquivos:
            os.system('clear')
            print('Selecionando '+arquivo)
            new = arquivo.replace('X2Download.com - ', f'{number} - ')
            os.rename(origem+arquivo, f'{destino}/{new}')
            os.system('clear')
            print('Renomeando ...')
            os.system('clear')
            print(f'Renomeado para {new} com sucesso!')
            number = number + 1 
        driver.close()
            
            
def Baixar(url_p, i):
    play = Playlist(url_p)            
    for url in play.video_urls:
        print(f'Iniciando rotina de download... |   Musicas Baixadas {i}')
        os.system('clear')
        print(f'Acessando site ...   |   Musicas Baixadas {i}')
        driver.get("https://x2download.com/pt17/download-youtube-to-mp3")
        search = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.XPATH, "//input[@class='search__input']")))
        search = driver.find_element(By.XPATH, "//input[@class='search__input']")
        search.click()
        os.system('clear')
        print(f'Pesquisando música   |   Musicas Baixadas {i}')
        search.send_keys(url)
        btn = driver.find_element(By.XPATH, "//button[@class='btn-red']")
        btn.click()
        getlink = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.XPATH, "//button[@class='btn-blue-small form-control btn-ads']")))
        os.system('clear')
        print(f'Escolhendo MP3 128kbps   |   Musicas Baixadas {i}')
        getlink = driver.find_element(By.XPATH, "//button[@class='btn-blue-small form-control btn-ads']")
        getlink.click()
        baixar = WebDriverWait(driver, 60).until( EC.presence_of_element_located((By.XPATH, "//a[@class='form-control mesg-convert success']")))
        os.system('clear')
        print(f'Baixando...   |   Musicas Baixadas {i}')
        baixar = driver.find_element(By.XPATH, "//a[@class='form-control mesg-convert success']")
        baixar.click()
        time.sleep(5)
        os.system('clear')
        i = i + 1
        print()
        print(f'{i} Musica(s) baixada(s)')
        

    Organizer(playlistNome)

Baixar(playlistURL, i)    
