import tkinter as tk

def converter_temp():
    try:
        temp = float(entry_temp.get())  # pega o valor digitado
        origem = origem_var.get()       # unidade de origem
        destino = destino_var.get()     # unidade de destino

        # Conversão: primeiro para Celsius
        if origem == "C":
            temp_c = temp
        elif origem == "F":
            temp_c = (temp - 32) * 5/9
        elif origem == "K":
            temp_c = temp - 273.15
        else:
            resultado_label.config(text="Unidade de origem inválida")
            return

        # Depois de Celsius para a unidade destino
        if destino == "C":
            resultado_temp = temp_c
        elif destino == "F":
            resultado_temp = (temp_c * 9/5) + 32
        elif destino == "K":
            resultado_temp = temp_c + 273.15
        else:
            resultado_label.config(text="Unidade de destino inválida")
            return

        resultado_label.config(text=f"{temp:.2f} {origem} = {resultado_temp:.2f} {destino}")

    except ValueError:
        resultado_label.config(text="Digite um valor numérico válido")

# --- Janela ---
janela = tk.Tk()
janela.title("Conversor de Temperatura")
janela.geometry("500x350")
janela.minsize(500, 350)

# Entrada de temperatura
tk.Label(janela, text="Temperatura", font=("Arial", 14)).pack(pady=10)
entry_temp = tk.Entry(janela, font=("Arial", 14))
entry_temp.pack(pady=5)
entry_temp.insert(0, "25")

# Unidade de origem
tk.Label(janela, text="De:", font=("Arial", 14)).pack(pady=5)
origem_var = tk.StringVar()
origem_var.set("C")
tk.OptionMenu(janela, origem_var, "C", "F", "K").pack(pady=5)

# Unidade de destino
tk.Label(janela, text="Para:", font=("Arial", 14)).pack(pady=5)
destino_var = tk.StringVar()
destino_var.set("F")
tk.OptionMenu(janela, destino_var, "C", "F", "K").pack(pady=5)

# Botão
tk.Button(janela, text="Converter", font=("Arial", 14), command=converter_temp).pack(pady=15)

# Resultado
resultado_label = tk.Label(janela, text="", font=("Arial", 14))
resultado_label.pack(pady=10)

janela.mainloop()
