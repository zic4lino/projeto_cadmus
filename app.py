from selenium.webdriver.common import by
from selenium_services import Selenium_services
import file_constructor as FC
import email_sender
import time
import os
import urllib3
urllib3.disable_warnings()

def substituir_apresentacao(descricao_vaga):
    texto_finalização = "\n\n\nDê um play em sua carreira! #VemSerCadmus."
    texto_apresentacao = "Somos uma das melhores empresas para trabalhar pelo GPTW,"\
                        " por isso, buscamos os melhores talentos porque acreditamos"\
                        " que só com pessoas incríveis entregamos resultados incríveis."
    descricao_vaga = descricao_vaga.replace(texto_finalização,"")
    return descricao_vaga.replace(texto_apresentacao+"\n\n","")



selenium = Selenium_services()
print("--------------Iniciando processo-------------")
time.sleep(4)
email_remetente = input("Insira o email do remetente(gmail):")
senha_remetente = input("insira a senha do remetente:")
email_destinatario = input("insira o destinatário:")



url = "https://cadmus.com.br/vagas-tecnologia/"

selenium.open_driver(url)
time.sleep(20)
contador_scroll = 0
obj_vagas = [["nome","local","descricao"]]

while True:
    vagas = selenium.extract_elements(selenium.by.XPATH,"//*[@id='pfolio']/div/div[@class='box']")
    selenium.scroll_page()
    contador_scroll += 1
    if not vagas[0].text == None or not vagas[0].text == "":
        break

time.sleep(3)
vagas = selenium.extract_elements(selenium.by.XPATH,"//*[@id='pfolio']/div/div[@class='box']")
for posicao_box in range(len(vagas)):
    info_vaga = selenium.extract_elements(selenium.by.XPATH,"//*[@id='pfolio']/div/div[@class='box']")[posicao_box].text
    campos_info_vaga = info_vaga.split("\n")
    selenium.click_scroll(selenium.by.XPATH,"//*[@id='pfolio']/div["+str(posicao_box+1)+"]/div/p[2]")
    time.sleep(5)
    descricao_vaga = selenium.extract_value(selenium.by.XPATH,"//*[@id='boxVaga']/p")
    if descricao_vaga == None:
        descricao_vaga = "Descrição indisponível"
    descricao_vaga_formatada = substituir_apresentacao(descricao_vaga)
    obj_vagas.append([campos_info_vaga[0],campos_info_vaga[1],descricao_vaga_formatada])
    selenium.backpage()
    time.sleep(5)

selenium.close_driver()
anexo = FC.create_excel(obj_vagas)
if anexo != None:
    email_sender.envio_email(email_remetente,email_destinatario,
                            senha_remetente, anexo)