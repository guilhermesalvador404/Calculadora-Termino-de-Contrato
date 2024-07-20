import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from dateutil.relativedelta import relativedelta

class CalculadoraTerminoContratoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Término de Contrato")
        self.root.configure(background='white')
        
        self.entry_style = {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)}
        self.label_style = {'bg': 'white', 'fg': 'black', 'font': ('Arial', 12)}

        self.create_widgets()

    def create_widgets(self):
        frame_entrada = tk.Frame(self.root, padx=10, pady=10, background='white')
        frame_entrada.pack()

        label_data_inicial = tk.Label(frame_entrada, text="Data inicial (dd/mm/aaaa):", **self.label_style)
        label_data_inicial.grid(row=0, column=0, padx=5, pady=5)
        self.entry_data_inicial = tk.Entry(frame_entrada, width=15, **self.entry_style)
        self.entry_data_inicial.grid(row=0, column=1, padx=5, pady=5)

        label_duracao = tk.Label(frame_entrada, text="Duração do contrato (meses):", **self.label_style)
        label_duracao.grid(row=1, column=0, padx=5, pady=5)
        self.entry_duracao = tk.Entry(frame_entrada, width=10, **self.entry_style)
        self.entry_duracao.grid(row=1, column=1, padx=5, pady=5)

        botao_calcular = tk.Button(self.root, text="Calcular Término", command=self.calcular_e_mostrar, **self.entry_style)
        botao_calcular.pack(pady=10)

        self.label_resultado = tk.Label(self.root, text="", **self.label_style)
        self.label_resultado.pack()

    def validar_entrada_data(self, data_str):
        try:
            datetime.strptime(data_str, "%d/%m/%Y")
            return True
        except ValueError:
            return False

    def validar_entrada_meses(self, meses_str):
        try:
            meses = int(meses_str)
            if meses > 0:
                return True
            else:
                return False
        except ValueError:
            return False

    def calcular_termino_contrato(self, data_inicial_str, meses_de_duracao):
        try:
            data_inicial = datetime.strptime(data_inicial_str, "%d/%m/%Y")
            data_final = data_inicial + relativedelta(months=meses_de_duracao)
            return data_final.strftime("%d/%m/%Y")
        except ValueError as e:
            messagebox.showerror("Erro", str(e))
            return None

    def calcular_e_mostrar(self):
        data_inicial_str = self.entry_data_inicial.get()
        meses_de_duracao = self.entry_duracao.get()

        # Validar entrada de data
        if not self.validar_entrada_data(data_inicial_str):
            messagebox.showerror("Erro", "Formato de data inválido. Use o formato dd/mm/aaaa.")
            return
        
        # Validar entrada de meses
        if not self.validar_entrada_meses(meses_de_duracao):
            messagebox.showerror("Erro", "Número de meses inválido. Digite um valor numérico positivo.")
            return

        resultado = self.calcular_termino_contrato(data_inicial_str, int(meses_de_duracao))

        if resultado:
            self.label_resultado.config(text=f"Data de término do contrato: {resultado}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraTerminoContratoApp(root)
    root.mainloop()
