import pandas as pd

def salvarCsv(df: pd.DataFrame, nome_arquivo: str, separador: str, decimal: str):
    """
    Salva um DataFrame do Pandas em um arquivo CSV com configurações personalizadas.

    Parâmetros:
    df (pd.DataFrame): O DataFrame a ser salvo.
    nome_arquivo (str): Nome do arquivo de destino (ex: "dados.csv").
    separador (str): Caractere utilizado para separar as colunas (ex: "," ou ";").
    decimal (str): Caractere usado para representar casas decimais (ex: "." ou ",").

    Retorno:
    None: A função apenas salva o arquivo e não retorna nenhum valor.
    """
    df.to_csv(nome_arquivo, sep=separador, decimal=decimal)
    return
