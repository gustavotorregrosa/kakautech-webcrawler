## Teste KakauTech ##

### Objetivo ###
O presente teste utiliza Python e Selenium para fazer um WebCrawler do site *https://www.scrapethissite.com/pages/simple/*, 
criando um CSV com os países do mundo com
- nome,
- capital,
- populacao,
- area

### Pontos Importantes ###

- Intruções de como montar o ambiente estão abaixo mas, se preferir, rode somente o comando abaixo para gerar o CSV a partir
de uma imagem que colocamos no dockerhub:


*linux/mac*
```bash 
    docker run -v .:/usr/src/app/compartilhado gustavotorregrosa/kakautech:v1
```

*windows*
```bash
    docker run -v .:/usr/src/app/compartilhado gustavotorregrosa/kakautech:v2
```


- Montamos um ambiente em docker, mas também deixamos abaixo as instruções para rodar como virtual env:
```bash
    cd infra
    python -m venv .
    ./Scripts/activate
    cd ../app
    python -m unittest discover (rodar os testes)
    python main.py

```

- Separamos o servico de extração dos dados do serviço de criação do arquivo CSV

- Utilizamos o unittest, nativo do python, para testar o serviço de extração
