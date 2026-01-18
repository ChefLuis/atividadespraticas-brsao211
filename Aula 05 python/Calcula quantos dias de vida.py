import tkinter as tk
from tkinter import messagebox
from datetime import date


# ======================================================
# FUNÇÃO DE CÁLCULO
# ======================================================

def calcular_dias_vivo(data_nascimento: date) -> int:
    """
    Calcula a quantidade de dias que uma pessoa está viva
    com base na data atual.
    """

    # Obtém a data atual do sistema
    data_atual = date.today()

    # Calcula a diferença entre as datas
    diferenca = data_atual - data_nascimento

    # Retorna apenas a quantidade de dias
    return diferenca.days


def executar_calculo():
    """
    Função acionada pelo botão.
    Lê os valores digitados, valida a data e exibe o resultado.
    """

    try:
        # Lê os valores digitados pelo usuário
        dia = int(entrada_dia.get())
        mes = int(entrada_mes.get())
        ano = int(entrada_ano.get())

        # Cria o objeto de data de nascimento
        data_nascimento = date(ano, mes, dia)

        # Verifica se a data é futura
        if data_nascimento > date.today():
            messagebox.showerror(
                "Erro",
                "A data de nascimento não pode ser futura."
            )
            return

        # Calcula os dias vividos
        dias_vivo = calcular_dias_vivo(data_nascimento)

        # Exibe o resultado
        resultado_var.set(f"Dias vividos: {dias_vivo}")

    except ValueError:
        # Captura erros de conversão ou datas inválidas
        messagebox.showerror(
            "Erro",
            "Informe uma data válida."
        )


# ======================================================
# INTERFACE GRÁFICA - TKINTER
# ======================================================

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora de Dias Vividos")
janela.geometry("380x300")
janela.resizable(False, False)

# Título
tk.Label(
    janela,
    text="Exercício 4 - Dias Vividos",
    font=("Arial", 12, "bold")
).pack(pady=10)

# Instrução
tk.Label(
    janela,
    text="Informe sua data de nascimento:"
).pack(pady=5)

# Frame para organizar os campos de data
frame_data = tk.Frame(janela)
frame_data.pack(pady=5)

# Campo Dia
tk.Label(frame_data, text="Dia").grid(row=0, column=0, padx=5)
entrada_dia = tk.Entry(frame_data, width=5)
entrada_dia.grid(row=1, column=0, padx=5)

# Campo Mês
tk.Label(frame_data, text="Mês").grid(row=0, column=1, padx=5)
entrada_mes = tk.Entry(frame_data, width=5)
entrada_mes.grid(row=1, column=1, padx=5)

# Campo Ano
tk.Label(frame_data, text="Ano").grid(row=0, column=2, padx=5)
entrada_ano = tk.Entry(frame_data, width=8)
entrada_ano.grid(row=1, column=2, padx=5)

# Botão de cálculo
tk.Button(
    janela,
    text="Calcular Dias Vividos",
    command=executar_calculo
).pack(pady=15)

# Variável e rótulo para o resultado
resultado_var = tk.StringVar()

tk.Label(
    janela,
    textvariable=resultado_var,
    font=("Arial", 11)
).pack(pady=10)

# Mantém a aplicação em execução
janela.mainloop()
