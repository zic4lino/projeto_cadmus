Esta solução foi desenvolvida por Luan Lino em conformidade com a CADMUS para avaliação técnica. 

Este programa fará a varredura de vagas abertas no site https://cadmus.com.br/vagas-tecnologia/, reuní-las em uma planilha nomeada "compilado_vagas.xlsx" e enviar via E-mail.

O programa é composto por 7 arquivos: app.py, chromedriver.exe, email_sender.py,file_constructor.py, readme.md, requirement.txt e selenium-services.py. Para executar este programa, você deve acessar a pasta utilizando o prompt de comando e digitar o comando "python app.py".

Ao início da execução, o programa pedirá para que você insira o endereço e a senha do remetente para fazer login no servidor SMTP do GMAIL. Após este passo, o programa pedirá para digitar o endereço ao qual você deseja enviar o E-mail. 

O fluxo iniciará e se tudo ocorrer bem, a mensagem de "E-mail enviado aparecerá no prompt de comando do programa.

Para executar este programa, você deve configurar sua máquina conforme requisitos dispostos no arquivo requirement.txt. Deixe o navegador chrome em primeiro plano na tela. OBS: A versão do chromedriver.exe que acompanha o pacote pode não ser compatível com o navegador chrome disponivel em seu computador. Caso aconteça, você deve pesquisar qual a versão de seu navegador através do menu->ajuda-acerca do gogole chrome. Após, deve acessar o site https://chromedriver.chromium.org/downloads e fazer o donwload do respectivo chromedriver dentro da pasta do programa.

Para envio do E-mail, favor utilizar um email da Google(Gmail) que contenha a flag de Acesso a apps menos seguros ativada. Caso não esteja ativada no email, acessar o endereço https://www.google.com/settings/security/lesssecureapps e ativar a flag.
