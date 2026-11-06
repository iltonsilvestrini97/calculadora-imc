import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    try:
        nome = entry_nome.get()
        endereco = entry_endereco.get()
        altura_cm = float(entry_altura.get())
        peso_kg = float(entry_peso.get())

        if altura_cm <= 0 or peso_kg <= 0:
            messagebox.showerror("Erro", "Altura e peso devem ser valores maiores que zero.")
            return

        # Converter altura para metros
        altura_m = altura_cm / 100.0
        imc = peso_kg / (altura_m ** 2)

        # Classificação do IMC baseada na referência padrão
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif imc < 25.0:
            classificacao = "Peso normal (Eutrofia)"
        elif imc < 30.0:
            classificacao = "Sobrepeso"
        elif imc < 35.0:
            classificacao = "Obesidade grau I"
        elif imc < 40.0:
            classificacao = "Obesidade grau II"
        else:
            classificacao = "Obesidade grau III (Mórbida)"

        # Exibir resultado na caixa de texto
        resultado_texto.config(state=tk.NORMAL)
        resultado_texto.delete("1.0", tk.END)
        resultado_texto.insert(
            tk.END,
            f"Paciente: {nome}\n"
            f"Endereço: {endereco}\n\n"
            f"IMC: {imc:.2f}\n"
            f"Classificação: {classificacao}"
        )
        resultado_texto.config(state=tk.DISABLED)

    except ValueError:
        messagebox.showerror("Erro de Entrada", "Por favor, insira valores numéricos válidos para altura e peso.")

def reiniciar():
    entry_nome.delete(0, tk.END)
    entry_endereco.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    resultado_texto.config(state=tk.NORMAL)
    resultado_texto.delete("1.0", tk.END)
    resultado_texto.config(state=tk.DISABLED)

def sair():
    root.destroy()

# Configuração da Janela Principal
root = tk.Tk()
root.title("Cálculo do IMC - Índice de Massa Corporal")
root.geometry("620x330")
root.resizable(False, False)

# Labels e Campos de Entrada
tk.Label(root, text="Nome do Paciente:").place(x=20, y=20)
entry_nome = tk.Entry(root, width=50)
entry_nome.place(x=140, y=20)

tk.Label(root, text="Endereço Completo:").place(x=20, y=60)
entry_endereco = tk.Entry(root, width=50)
entry_endereco.place(x=140, y=60)

tk.Label(root, text="Altura (cm):").place(x=20, y=100)
entry_altura = tk.Entry(root, width=15)
entry_altura.place(x=140, y=100)

tk.Label(root, text="Peso (Kg):").place(x=20, y=140)
entry_peso = tk.Entry(root, width=15)
entry_peso.place(x=140, y=140)

# Caixa de Texto de Resultado
tk.Label(root, text="Resultado").place(x=410, y=95)
resultado_texto = tk.Text(root, width=32, height=9, state=tk.DISABLED)
resultado_texto.place(x=310, y=120)

# Botões Inferiores
btn_calcular = tk.Button(root, text="Calcular", width=12, command=calcular_imc)
btn_calcular.place(x=70, y=260)

btn_reiniciar = tk.Button(root, text="Reiniciar", width=12, command=reiniciar)
btn_reiniciar.place(x=180, y=260)

btn_sair = tk.Button(root, text="Sair", width=12, command=sair)
btn_sair.place(x=470, y=260)

root.mainloop()