# Dependências
import csv
import json


# Função que transforma um arquivo CSV em JSON
# Recebe como parâmetro o endereço do arquivo CSV
def csv2json(csv_filepath):
    # Abre o arquivo CSV
    csv_file = open(csv_filepath, 'r', errors="ignore")
    # Abre um arquivo JSON para escrita
    # Passe dentro do "open" o endereço onde quer que o arquivo seja salvo
    json_file = open(r'resultado.json', 'w')

    # Instancia um leitor de CSV
    # CASO SEU ARQUIVO SEJA DELIMITADOR COM ";", MUDE O DELIMITER
    reader = csv.DictReader(csv_file, delimiter=",")
    # Transforma o arquivo em JSON
    archive = json.dumps([row for row in reader], ensure_ascii=False)
    # Escreve o JSON no arquivo aberto anteriormente
    json_file.write(archive)


# Chama a função passando o endereço do arquivo CSV
csv2json(r'exemplo.csv')
