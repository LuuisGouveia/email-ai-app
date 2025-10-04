Características Gerais:
A Aplicação Email-ai-Process foi construída com Back-end em Python utilizando o framework FastAPI e no seu Front-end foi utilizado HTML, CSS e JS puros.

Foi utilizado a biblioteca Nltk do Python para o NLP das mensagens enviadas.

O modelo de IA utilizado para categorização de emails e sugestão de respostas automáticas foi a Hugging Face Distilbert, elá foi treinada com 400 exemplos de emails sendo 200 de cada categoria.

Foi implementado no serviço de IA uma estrutura para isolar o modelo e ser chamado apenas quando for necessário, diminuindo o peso dos dados do modelo no deploy devido ao uso da versão gratuita do Render.

As respostas automáticas seguem templates pré definidos que poderiam ser aumentados para melhor variação de respostas. 

É possivel também fazer envio de arquivos de emails em .txt e .pdf, os arquivos são processados e transformados em texto puro que depois é avaliado pelo modelo de IA.

Instruções para run local:

A aplicação é simples e é necessário apenas o python instalado previamente, todas as dependências utilizadas estão devidamente listadas no arquivo requirements.txt na raíz do projeto para instalação, porém o modelo de IA devido a seu grande tamanho não foi carregado no repositorio remoto do Github, para ter o modelo é necessário rodar o script python train_model.py, no diretório training que já está configurado corretamente, no mesmo diretório constam os arquivos emails.csv e emails_test.csv que usados para o treino do modelo.

Deploy:

O deploy foi realizado porém houve complicações devido ao tamanho do modelo de IA do hugging face que ultrapassa o limite permitido pelo Render no plano gratuito, o deploy é feito e fica no ar porém não consegue processar as requisções quando aciona o modelo de IA.
Link do deploy Back-end:https://ai-email-process.onrender.com
Link do deploy Front-end:https://luuisgouveia.github.io/email-ai-app/
