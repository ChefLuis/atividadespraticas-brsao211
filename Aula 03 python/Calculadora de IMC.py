import tkinter as tk

def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())
        if peso <= 0 or altura <= 0:
            resultado.config(text="Peso e altura devem ser maiores que zero")
            return
        imc = peso / (altura ** 2)
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25:
            classificacao = "Peso normal"
        elif imc < 30:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obeso"
        resultado.config(
            text=f"Peso: {peso} kg\nAltura: {altura} m\nIMC: {imc:.2f}\nClassificação: {classificacao}"
        )
    except ValueError:
        resultado.config(text="Preencha os campos corretamente")

# Janela
janela = tk.Tk()
janela.title("Calculadora de IMC")
janela.geometry("450x350")
janela.minsize(450, 350)

# Peso
tk.Label(janela, text="Peso (kg)", font=("Arial", 12)).pack(pady=8)
entry_peso = tk.Entry(janela, font=("Arial", 12))
entry_peso.pack(pady=5)
entry_peso.insert(0, "70")

# Altura
tk.Label(janela, text="Altura (m)", font=("Arial", 12)).pack(pady=8)
entry_altura = tk.Entry(janela, font=("Arial", 12))
entry_altura.pack(pady=5)
entry_altura.insert(0, "1.75")

# Botão
tk.Button(janela, text="Calcular IMC", font=("Arial", 12), command=calcular_imc).pack(pady=15)

# Resultado
resultado = tk.Label(janela, text="", justify="left", font=("Arial", 12))
resultado.pack(pady=10)

janela.mainloop()
