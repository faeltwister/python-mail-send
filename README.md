# Automatização de Envio de E-mails com Python

Este é um exemplo simples de automação de envio de e-mails usando Python e a biblioteca `smtplib`. O script Python inclui configurações para o servidor SMTP, criação de e-mails MIME com conteúdo HTML e anexação de arquivos, demonstrando uma maneira prática de incorporar essa funcionalidade em seus projetos.

## Configurações

Certifique-se de ter o Python instalado em sua máquina. Mude as configurações abaixo:

```bash
host="smtp.meuservidor.com"
port="587"
login="meuemail@lol.com.br"
senha="minhasenha"
```

Altere o anexo para o caminho onde estão os arquivos para enviar:
```bash
anexo='E:/PDF/arquivo.pdf'
parte_apos_pdf = anexo.split('E:/PDF/', 1)[1]
```
