import tkinter as tk
from tkinter import ttk

def criar_aba_2(notebook, responder_pergunta):
  tab2 = ttk.Frame(notebook)
  notebook.add(tab2, text='Responder pergunta')

  #linha 0
  tk.Label(
    tab2, 
    text='Escreva aqui a sua pergunta'
  ).grid(row=0, column=0, sticky='W', padx=5, pady=0)

  #linha 1
  pergunta_text = tk.Text(tab2)
  pergunta_text.configure(height=20)
  pergunta_text.grid(
    row=1, column=0, sticky='WEN', padx=5, pady=0
  )

  #linha 2
  tk.Label(
    tab2, 
    text='Eis a resposta do ChatGPT:'
  ).grid(row=2, column=0, sticky='W', padx=5, pady=0)

  #linha 3
  resposta_text = tk.Text(tab2)
  resposta_text.configure(height=20)
  resposta_text.grid(row=3, column=0, sticky='WEN', padx=5, pady=0)

  #linha 4
  def executar():
    resposta = responder_pergunta(
      pergunta_text.get('1.0', 'end')
    )
    resposta_text.delete('1.0', 'end')
    resposta_text.insert('1.0', resposta)
  tk.Button(
    tab2,
    text='Ok',
    command=executar
  ).grid(row=4, column=0, sticky='WE', padx=5, pady=5)

  for i in range(5):
    tab2.grid_rowconfigure(i, weight=1)
  
  tab2.grid_columnconfigure(0, weight=1)

def criar_aba1(notebook, criar_pergunta):
  tab1 = ttk.Frame(notebook)
  notebook.add(tab1, text='Gerar pergunta')

  #linha 0
  tk.Label(tab1, text='Assunto').grid(row=0, column=0, sticky='W', padx=5, pady=5)
  assunto_entry = tk.Entry(tab1)
  assunto_entry.grid(row=0, column=1, columnspan=3, sticky='WE', padx=5, pady=5)

  #linha 1
  tk.Label(tab1, text='Tipo').grid(row=1, column=0, sticky='W', padx=5, pady=5)
  tipo_var = tk.StringVar()
  tk.Radiobutton(
    tab1, 
    text='Dissertativa', 
    value='Dissertativa',
    variable=tipo_var
  ).grid(row=1, column=1, sticky='W', padx=5, pady=5)
  tk.Radiobutton(
    tab1,
    text='Alternativa',
    value='Alternativa',
    variable=tipo_var
  ).grid(row=1, column=2, sticky='W', padx=5, pady=5)

  #linha 2
  tk.Label(tab1, text='Dificuldade:').grid(row=2, column=0, sticky='W', padx=5, pady=5)
  dificuldade_var = tk.StringVar()
  tk.Radiobutton(
    tab1,
    text='Fácil',
    value='Fácil',
    variable=dificuldade_var  
  ).grid(row=2, column=1, sticky='W', padx=5, pady=5)

  tk.Radiobutton(
    tab1,
    text='Médio',
    value='Médio',
    variable=dificuldade_var  
  ).grid(row=2, column=2, sticky='W', padx=5, pady=5)

  tk.Radiobutton(
    tab1,
    text='Difícil',
    value='Difícil',
    variable=dificuldade_var  
  ).grid(row=2, column=3, sticky='W', padx=5, pady=5)
  
  #linha 3
  tk.Label(
    tab1, 
    text='Pergunta exemplo'
  ).grid(row=3, column=0, sticky='W', padx=5, pady=5)

  #linha 4
  pergunta_exemplo = tk.Text(tab1)
  pergunta_exemplo.configure(height=20)
  pergunta_exemplo.grid(
    row=4, column=0, columnspan=4, sticky='WE', padx=5, pady=5
  )
  
  #linha 5
  tk.Label(
    tab1, 
    text='Resposta'
  ).grid(row=5, column=0,sticky='W', padx=5, pady=5)

  #linha 6
  resposta_chagpt = tk.Text(tab1)
  resposta_chagpt.configure(height=20)
  resposta_chagpt.grid(
    row=6, column=0, columnspan=4, sticky='WE', padx=5, pady=5
  )

  #linha 7
  def executar():
    resposta_chagpt.delete('1.0', 'end')
    resposta = criar_pergunta(
      assunto_entry.get(),
      tipo_var.get(),
      dificuldade_var.get(),
      pergunta_exemplo.get('1.0', 'end')
    )
    resposta_chagpt.insert('1.0', resposta)  
  ok_button = tk.Button(tab1, text='OK', command=executar)
  ok_button.grid(
    row=7, column=0, columnspan=4, sticky='WE', padx=5, pady=5
  )

  for i in range(8):
    tab1.grid_rowconfigure(i, weight=1)
  for i in range(4):
    tab1.grid_columnconfigure(i, weight=1)

  return tab1


def criar_tela(criar_pergunta, responder_pergunta):
  window = tk.Tk()
  window.title("ChatGPT - Gerador/Corretor de Questões")
  window.minsize(900, 600)
  notebook = ttk.Notebook(window, padding=10)
  tab1 = criar_aba1(notebook, criar_pergunta)
  tab2 = criar_aba_2(notebook, responder_pergunta)
  notebook.pack(expand=True, fill='both')
  window.mainloop()