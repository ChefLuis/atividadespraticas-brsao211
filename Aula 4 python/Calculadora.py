import tkinter as tk
import math

def inserir(valor):
    visor.insert(tk.END, valor)

def limpar():
    visor.delete(0, tk.END)

def calcular():
    try:
        expressao = visor.get()
        expressao = expressao.replace("π", str(math.pi))
        resultado = eval(expressao)
        limpar()
        visor.insert(0, resultado)
    except:
        limpar()
        visor.insert(0, "Erro")

def funcao(f):
    try:
        valor = float(visor.get())
        limpar()
        visor.insert(0, f(valor))
    except:
        limpar()
        visor.insert(0, "Erro")

janela = tk.Tk()
janela.title("Calculadora Científica")
janela.geometry("350x450")
janela.resizable(False, False)

visor = tk.Entry(janela, font=("Arial", 20), justify="right")
visor.pack(fill="x", padx=10, pady=10)

botoes = [
    ("7", "8", "9", "/", "C"),
    ("4", "5", "6", "*", "("),
    ("1", "2", "3", "-", ")"),
    ("0", ".", "^", "+", "="),
    ("√", "sen", "cos", "tan", "π"),
    ("log", "ln", "", "", "")
]

frame = tk.Frame(janela)
frame.pack()

for linha in botoes:
    linha_frame = tk.Frame(frame)
    linha_frame.pack()
    for texto in linha:
        if texto == "":
            tk.Label(linha_frame, width=6).pack(side="left")
            continue

        if texto == "C":
            cmd = limpar
        elif texto == "=":
            cmd = calcular
        elif texto == "√":
            cmd = lambda: funcao(math.sqrt)
        elif texto == "sen":
            cmd = lambda: funcao(lambda x: math.sin(math.radians(x)))
        elif texto == "cos":
            cmd = lambda: funcao(lambda x: math.cos(math.radians(x)))
        elif texto == "tan":
            cmd = lambda: funcao(lambda x: math.tan(math.radians(x)))
        elif texto == "log":
            cmd = lambda: funcao(math.log10)
        elif texto == "ln":
            cmd = lambda: funcao(math.log)
        elif texto == "^":
            cmd = lambda: inserir("**")
        else:
            cmd = lambda t=texto: inserir(t)

        tk.Button(
            linha_frame,
            text=texto,
            width=6,
            height=2,
            command=cmd
        ).pack(side="left", padx=2, pady=2)

janela.mainloop()
