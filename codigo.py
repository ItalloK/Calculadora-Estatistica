import numpy as np
import tkinter as tk
from tkinter import messagebox

def calcular_media(dados):
    return np.mean(dados)

def calcular_moda(dados):
    modas, counts = np.unique(dados, return_counts=True)
    return modas[counts == np.max(counts)]

def calcular_mediana(dados):
    return np.median(dados)

def calcular_media_harmonica(dados):
    return len(dados) / np.sum(1 / dados)

def calcular_media_geometrica(dados):
    return np.prod(dados) ** (1 / len(dados))

def calcular_media_rms(dados):
    return np.sqrt(np.mean(dados ** 2))

def calcular_variancia(dados):
    return np.var(dados)

def calcular_variancia_amostral(dados):
    return np.var(dados, ddof=1)

def calcular_desvio_padrao(dados):
    return np.std(dados)

def calcular_desvio_padrao_amostral(dados):
    return np.std(dados, ddof=1)

def ler_dados_arquivo():
    try:
        with open("dados.txt", 'r') as arquivo:
            dados = arquivo.read().replace(',', '.').split()
            return np.array(list(map(float, dados)))
    except FileNotFoundError:
        messagebox.showerror("Erro", "Arquivo 'dados.txt' não encontrado.")
        return None

# Função para exibir os resultados
def exibir_resultados(dados):
    media = calcular_media(dados)
    modas = calcular_moda(dados)
    mediana = calcular_mediana(dados)
    media_harmonica = calcular_media_harmonica(dados)
    media_geometrica = calcular_media_geometrica(dados)
    media_rms = calcular_media_rms(dados)
    variancia = calcular_variancia(dados)
    varianciaamostral = calcular_variancia_amostral(dados)
    desvio_padrao = calcular_desvio_padrao(dados)
    desvio_amostral = calcular_desvio_padrao_amostral(dados)

    resultado = "Resultados:\n\n"
    resultado += f"Média: {media:.2f}\n"
    if len(modas) > 1:
        resultado += f"Modas: {modas}\n"
    else:
        resultado += f"Moda: {modas[0]}\n"
    resultado += f"Mediana: {mediana:.2f}\n"
    resultado += f"Média Harmônica: {media_harmonica:.2f}\n"
    resultado += f"Média Geométrica: {media_geometrica:.2f}\n"
    resultado += f"Média RMS: {media_rms:.2f}\n"
    resultado += f"Variância População: {variancia:.2f}\n"
    resultado += f"Variância Amostra: {varianciaamostral:.2f}\n"
    resultado += f"DP População: {desvio_padrao:.2f}\n"
    resultado += f"DP Amostra: {desvio_amostral:.2f}\n" 

    messagebox.showinfo("Resultados", resultado)

dados = ler_dados_arquivo()
if dados is not None:
    exibir_resultados(dados)
