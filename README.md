# upload-de-videos-para-o-youtube-de-forma-automatica
Criei o progama para ajudar quem gosta de upar varios videos ja criados para o youtube de forma automatizada ,so precisa configurar uma vez e ele ja faz automatico, sem precisar postar um por um,podendo agendar a data de postagem

1 Primeiro baixe o arquivo, extraia a pasta caso esteja em rar,

2 Abra a pasta no console que contenha o python instalado.

3 Instale as bibliotecas.
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client

4 


Para ele ir para o seu youtube siga o passo a passp para configurar no seu perfil google

1º Criar um Projeto no Google Cloud Console
1 Acesse o Google Cloud Console.
2 Faça login com sua conta Google.
3 No canto superior esquerdo, clique no menu ≡ e selecione "IAM e administração" > "Criar um projeto".
4 Dê um nome ao projeto (exemplo: "YouTube Video Uploader") e clique em Criar.
5 Aguarde a criação do projeto e selecione-o no topo da página.

2º Ativar a YouTube Data API v3
1 No menu ≡, vá para "APIs e serviços" > "Biblioteca".
2 Na barra de pesquisa, digite "YouTube Data API v3" e clique nela.
3 Clique em "Ativar".

3º Criar Credenciais OAuth 2.0
1 No menu ≡, vá para "APIs e serviços" > "Credenciais".
2 Clique em "Criar credenciais" e selecione "ID do cliente OAuth".
3 Caso apareça um aviso sobre a configuração da tela de consentimento, clique em "Configurar tela de consentimento":
-Escolha "Externo" e clique em "Criar".
-Insira um nome de aplicativo (exemplo: "YouTube Uploader Bot").
-Na seção "Usuários de teste", adicione seu e-mail do Google.
-Clique em Salvar e Continuar até concluir.
4 Volte para "Credenciais" e clique em "Criar credenciais" > "ID do cliente OAuth":
-Tipo de aplicativo: "Aplicativo para computador".
-Nome: "YouTube Uploader App".
-Clique em Criar.
5 Baixe o arquivo JSON das credenciais (client_secrets.json) e coloque-o na pasta do seu script Python, apos baixar precisa renomea-lo para client_secrets.json.

Agora você pode rodar o script para autenticar e começar a fazer uploads no YouTube! 🎥🚀

Adicionar sua conta como testador
1 Acesse o Google Cloud Console.
2 No menu lateral, vá para "APIs e serviços" > "Tela de consentimento OAuth".
3 Role para baixo até a seção "Usuários de teste".
4 Clique em "Adicionar usuários" e digite o e-mail da conta do Google que você usará para fazer login.
5 Clique em Salvar e Continuar.

