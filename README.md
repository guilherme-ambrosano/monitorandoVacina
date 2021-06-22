# monitorandoVacina
Programinha em Python pra monitorar o site das vacinas de Piracicaba

Antes de rodar, baixe os pacotes necessários:

```
conda install beautifulsoup4
pip install playsound
pip install Unidecode
pip install html5lib

```

E altere o arquivo ```configuracoes.py``` de acordo com a busca desejada.

## configuracoes.py

Para rodar o programa, você vai precisar criar um arquivo chamado ```configuracoes.py```.
Esse arquivo tem esse formato:

```
# Configurações pro monitoramento do site da vacina

# lista de strings para buscar no site (por exemplo, pessoas com comorbidade)
busca = ["pessoas com comorbidade"] 
horario = "12:00"  # hora que vai abrir (formato %H:%M)
```