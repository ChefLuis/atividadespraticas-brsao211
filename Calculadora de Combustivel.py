import tkinter as tk

# Dados fixos
distancia = 300
combustivel = 25
consumo = distancia / combustivel

# Janela
janela = tk.Tk()
janela.title("Consumo de Combustível")
janela.geometry("300x200")

# Conteúdo
tk.Label(janela, text="Calculadora de Consumo", font=("Arial", 12, "bold")).pack(pady=10)

tk.Label(janela, text=f"Distância percorrida: {distancia} km").pack()
tk.Label(janela, text=f"Combustível gasto: {combustivel} litros").pack()

tk.Label(
    janela,
    text=f"Consumo médio: {consumo:.2f} km/l",
    font=("Arial", 11),
    fg="green"
).pack(pady=10)

janela.mainloop()
