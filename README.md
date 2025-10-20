# 💖 Lembre-se, Outubro Rosa 🎀

Um projeto em Python que envia **mensagens de conscientização sobre o câncer de mama**, com foco em **saúde, autocuidado e amor próprio**.
Criei este projeto para **praticar meus conhecimentos em Python**, ao mesmo tempo **vincular a um dos objetivos da ONU (Organização das Nações Unidas): 3 - Saúde e Bem-Estar. 🌸** 

## 🌷 Sobre o projeto

### O objetivo é simples e delicado: 

* Lembrar mulheres da importância de cuidar da própria saúde
* Incentivar o amor próprio através de pequenas mensagens diárias.
* Criar uma automação leve que funcione de forma prática e segura.
* O projeto envia um e-mail por dia contendo uma mensagem aleatória do CSV, seguindo um fluxo simples:

![Fluxo da automação](https://github.com/SamarahCosta/lembre-se-outubro-rosa/blob/main/data/fluxo.png)


## 📂 Estrutura dos arquivos

`mensagens.csv`
Contém todas as mensagens que serão enviadas. Cada linha é uma mensagem única.

`utilitario.py`
Responsável por ler o CSV e transformar as mensagens em uma lista para envio.

`envio.py`
Contém a função enviar_email(), que envia os e-mails pelo Gmail ou Outlook.

`agendador.py`
Configura o agendamento diário, usando a biblioteca schedule.
* Permite definir horário fixo para envio,
* Verifica a data limite (por exemplo, até 31/10/2025) para encerrar a campanha automaticamente.

`main.py`
Integra todos os módulos e mantém o script rodando.

_Algumas anotações explicam como configurar a senha de app e o remetente para quem for clonar o projeto._

## ⚙️ Como usar

* Clone o repositório
* Edite o **arquivo envio.py**
  * Altere a configuração do servidor para Gmail ou Outlook
* Edite o arquivo **agendador.py**
  * Atualize suas credenciais: email, senha (comentários no código de como deve ser realizado)
* Execute o script:
  * `python main.py`
  * Certifique-se de estar na pasta **src** no terminal 

A automação enviará uma mensagem todos os dias as 10 horas (O script deve estar rodando contínuamente).

## 💌 Final

Este projeto nasceu apenas para praticar Python e, ao mesmo tempo, lembrar da importância da saúde e do amor próprio.
Que cada mensagem enviada inspire cuidado, carinho e atenção consigo mesma, porque a prevenção é um gesto de amor. 🌸
