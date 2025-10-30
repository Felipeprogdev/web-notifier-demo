# Web Notifier Demo

⚠️ **Atenção:** Este repositório contém apenas uma parte do código do projeto.  
O programa completo está funcionando no vídeo demonstrativo abaixo.

📺 **Assista ao vídeo do projeto completo aqui:** [link do vídeo]

---

## Descrição

Este projeto é um **script de automação para extração de conteúdo e notificação de novidades em sites**. Ele permite acompanhar mudanças em páginas web e receber alertas automaticamente.  

Funcionalidades principais:

- **Raspagem de conteúdo** de sites usando **requests + BeautifulSoup**.  
- **Identificação de novidades**, como artigos, vagas de emprego ou publicações, comparando com o histórico anterior.  
- **Armazenamento local do histórico** em **SQLite**, para comparar o que é novo.  
- **Envio de notificações** por emailquando novas informações são encontradas.  
- **Agendamento automático** para rodar em intervalos definidos usando **schedule**.  

---

## Tecnologias utilizadas

- **Python** – linguagem principal do projeto  
- **requests** e **BeautifulSoup** – raspagem de dados de sites  
- **Selenium** (opcional) – para sites dinâmicos  
- **SQLite** ou **arquivo JSON** – armazenamento local do histórico  
- **smtplib** / **SMTP** – envio de emails
- **schedule** – agendamento automático das verificações  


