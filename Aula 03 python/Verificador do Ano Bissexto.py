import tkinter as tk

def listar_datas_comemorativas():
    for widget in frame_resultado.winfo_children():
        widget.destroy()  # limpa resultados anteriores

    try:
        ano = int(entry_ano.get())
        if ano <= 0:
            tk.Label(frame_resultado, text="Digite um ano válido", font=("Arial", 12)).pack()
            return

        # Verifica se o ano é bissexto
        if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
            bissexto_texto = "Bissexto"
        else:
            bissexto_texto = "Não bissexto"

        # Cabeçalho
        tk.Label(frame_resultado, text=f"Ano: {ano} - {bissexto_texto}", font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=(0,10))

        # Lista de datas comemorativas (fixas)
        datas = [
            "01/01 - Confraternização Universal",
            "08/03 - Dia Internacional da Mulher",
            "12/06 - Dia dos Namorados",
            "10/05 - Dia das Mães",
            "09/08 - Dia dos Pais",
            "15/10 - Dia do Professor",
            "24/06 - São João",
            "29/06 - São Pedro",
            "21/04 - Tiradentes",
            "01/05 - Dia do Trabalho",
            "07/09 - Independência do Brasil",
            "12/10 - Nossa Senhora Aparecida",
            "02/11 - Finados",
            "15/11 - Proclamação da República",
            "20/11 - Dia da Consciência Negra",
            "25/12 - Natal"
        ]

        # Divide a lista em duas colunas
        metade = (len(datas) + 1) // 2
        col1 = datas[:metade]
        col2 = datas[metade:]

        # Preenche as colunas
        for i in range(metade):
            tk.Label(frame_resultado, text=col1[i] + f"/{ano}", font=("Arial", 12)).grid(row=i+1, column=0, sticky="w", padx=10, pady=2)
            if i < len(col2):
                tk.Label(frame_resultado, text=col2[i] + f"/{ano}", font=("Arial", 12)).grid(row=i+1, column=1, sticky="w", padx=10, pady=2)

    except ValueError:
        tk.Label(frame_resultado, text="Digite um ano válido", font=("Arial", 12)).pack()

# --- Janela ---
janela = tk.Tk()
janela.title("Verificador de Ano + Datas Comemorativas")
janela.geometry("700x500")
janela.minsize(700, 500)

tk.Label(janela, text="Digite o ano", font=("Arial", 14)).pack(pady=10)
entry_ano = tk.Entry(janela, font=("Arial", 14))
entry_ano.pack(pady=5)
entry_ano.insert(0, "2026")

tk.Button(janela, text="Verificar", font=("Arial", 14), command=listar_datas_comemorativas).pack(pady=15)

# Frame para resultados
frame_resultado = tk.Frame(janela)
frame_resultado.pack(pady=10, fill="both", expand=True)

janela.mainloop()
