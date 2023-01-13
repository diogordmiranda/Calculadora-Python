import tkinter as tk

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()

        # Titulo da Tela
        self.title("PyCalc")

        # Definindo Proporçao da tela
        self.geometry("180x250") 
    
        # Configuraçao inical do Display
        self.show = "0"
        self.equation = tk.StringVar()
        self.equation.set(self.show)

        entry = tk.Label(self, textvariable= self.equation, font="Calibri 20")
        entry.grid(row=0, column=0, columnspan=4,sticky="nsew")

        # Configuraçao do grid
        for i in range(4):
            self.columnconfigure(i, weight=1)

        for i in range(5):
            self.rowconfigure(i, weight=1)

        # Funcao para apertar algum botao
        def press(num):  
            self.text = num
            if self.show == '0':
                if num in ["+","-","*","/","="]:
                    self.text = ""
                else:
                    self.show = ""
            self.show = self.show + str(self.text)
            self.equation.set(self.show)

        # Funcao para realizar as operaçoes
        def evaluate():
            try:
                self.equation.set(self.show)
                self.total = str(eval(self.show))
                if len(self.total) > 20:
                    self.total = str(self.total[0:20])
                self.equation.set(self.total)
                self.show= ""
            except:
                self.equation.set("Error")
                self.show = ""

        # Funcao para Limpar o Display
        def clear():
            self.show = "0"
            self.equation.set(self.show)

        # Criaçao dos botoes numericos
        # Definicao da posicao dos botoes no grid 
        botao1 = tk.Button(self, text="1", command=lambda: press(1))
        botao1.grid(row=1, column=0, sticky="nsew")

        botao2 = tk.Button(self, text="2", command=lambda: press(2))
        botao2.grid(row=1, column=1, sticky="nsew")

        botao3 = tk.Button(self, text="3", command=lambda: press(3))
        botao3.grid(row=1, column=2, sticky="nsew")

        botao4 = tk.Button(self, text="4", command=lambda: press(4))
        botao4.grid(row=2, column=0, sticky="nsew")

        botao5 = tk.Button(self, text="5", command=lambda: press(5))
        botao5.grid(row=2, column=1, sticky="nsew")

        botao6 = tk.Button(self, text="6", command=lambda: press(6))
        botao6.grid(row=2, column=2, sticky="nsew")

        botao7 = tk.Button(self, text="7", command=lambda: press(7))
        botao7.grid(row=3, column=0, sticky="nsew")

        botao8 = tk.Button(self, text="8", command=lambda: press(8))
        botao8.grid(row=3, column=1, sticky="nsew")

        botao9 = tk.Button(self, text="9", command=lambda: press(9))
        botao9.grid(row=3, column=2, sticky="nsew")

        botao0 = tk.Button(self, text="0", command=lambda: press(0))
        botao0.grid(row=4, column=1, sticky="nsew")

        # Criacao do botao de Limpar
        # Definicao da posicao do botao no grid 
        botaoC = tk.Button(self, text="C", command=clear)
        botaoC.grid(row=4, column=0, sticky="nsew")

        # Criacao dos botoes das operacoes
        # Definicao da posicao dos botoes no grid 
        botaoIgual = tk.Button(self, text="=", command=evaluate)
        botaoIgual.grid(row=4, column=2, sticky="nsew")

        botaoSoma = tk.Button(self, text="+", command=lambda: press("+"))
        botaoSoma.grid(row=1, column=3, sticky="nsew")

        botaoDim = tk.Button(self, text="-", command=lambda: press("-"))
        botaoDim.grid(row=2, column=3, sticky="nsew")

        botaoMul = tk.Button(self, text="*", command=lambda: press("*"))
        botaoMul.grid(row=3, column=3, sticky="nsew")

        botaoDiv = tk.Button(self, text="/", command=lambda: press("/"))
        botaoDiv.grid(row=4, column=3, sticky="nsew")

if __name__ == "__main__":
    calculadora = Calculadora()
    calculadora.mainloop() 


