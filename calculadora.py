import tkinter as tk
from tkinter import messagebox

#Função utilizando eval para saber oq ele irá executar
def click(button_text):
    if button_text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Operação Inválida")
    elif button_text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, button_text)


# Iniciar o Tk
janela = tk.Tk()
janela.title("Calculadora JL")
janela.geometry("300x350")

# Campo de entrada
entry = tk.Entry(janela, width=20, font=("Arial", 24), bd=5, insertwidth=4, justify='right')
entry.place(x=10, y=10, width=280, height=50)

# Botões de operações
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

# Lugar dos botões
button_width = 60
button_height = 60
spacing = 10
start_x = 10
start_y = 70

# Configuração dos botões
for i, row in enumerate(buttons):
    for j, button_text in enumerate(row):
        
        if button_text == "C":
            button = tk.Button(janela, text=button_text, font=("Arial", 18), bg="red",
                               command=lambda bt=button_text: click(bt))
        else:
            button = tk.Button(janela, text=button_text, font=("Arial", 18),
                               command=lambda bt=button_text: click(bt))
        
        # Definindo a posição dos botões
        button.place(x=start_x + j * (button_width + spacing),
                     y=start_y + i * (button_height + spacing),
                     width=button_width, height=button_height)


# Lembrar de colocar o Mainloop para manter a janela aberta
janela.mainloop()
