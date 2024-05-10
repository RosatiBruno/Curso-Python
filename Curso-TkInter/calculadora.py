from tkinter import *
import tkinter as tk
class Calculator:

    def __init__(self):

        # CONFIGURAÇÕES
        minWidth = 300  # Define o tamanho mínimo
        minHeight = 400  # Define a altura mínima

        maxWidth = int(minWidth * 1.3)  # Define o tamanho máximo
        maxHeight = int(minHeight * 1.3)  # Define a altura máxima

        topRatio = 1
        middleRatio = 7
        bottomRatio = 2

        topHeight = int(minHeight * topRatio / 10)  # Define a altura do frame de cima 10%
        middleHeight = int(minHeight * middleRatio / 10)  # Define a altura do frame do meio 70%
        bottomHeight = int(minHeight * bottomRatio / 10)  # Define a altura do frame de baixo 20%

        topFrameFont = "Arial 24 bold"  #Define a fonte, tamanho e estilo
        middleFrameFont = "Arial 24 bold"  #Define a fonte, tamanho e estilo
        bottomFrameFont = "Arial 24 bold"  #Define a fonte, tamanho e estilo

        # JANELA
        self.window = tk.Tk()

        root = self.window  # Apenas define 'self.window', como se fosse um alias
        root.title("Calculadora")  # Fornece o título para a calculadora
        root.minsize(minWidth, minHeight)  # Define o tamanho padrão mínimo
        root.maxsize(maxWidth, maxHeight)  # Define o tamanho padrão máximo

        # DIVISÃO DA CALCULADORA EM FRAMES
        #Frame de cima
        topFrame = Frame(
            root,
            width=minWidth,
            height=topHeight,
            bg="red"
        )

        #Frame do meio
        middleFrame = Frame(
            root,
            width=minWidth,
            height=middleHeight,
            bg="green"
        )

        #Frame de baixo
        bottomFrame = Frame(
            root,
            width=minWidth,
            height=bottomHeight,
            bg="blue"
        )

        #Faz as frames aparecerem na tela. O 'sticky="news"' faz eles serem redimencionaveis
        topFrame.grid(row=0, column=0, sticky="news")
        middleFrame.grid(row=1, column=0, sticky="news")
        bottomFrame.grid(row=2, column=0, sticky="news")

        #Quando redimenciona a tela, os objetos se centralizam
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=topRatio)
        root.rowconfigure(1, weight=middleRatio)
        root.rowconfigure(2, weight=bottomRatio)

        #Construindo o conteúdo dos Frames
        self._BuildTopFrameContent(topFrame, topFrameFont)

        self._BuildBottomFrameContent(bottomFrame, bottomFrameFont)

        # INICIA A CALCULADORA
        self.window.mainloop()  # Inicia a calculadora

    def _BuildTopFrameContent(self, frame: Frame, fontConfig) :

        self.lbl_display = Label(
            frame,
            text="texto de teste",
            anchor="e", #Mantém o texto preso na direita
            font=fontConfig
        )

        self.lbl_display.grid(row=0, column=0, sticky="news")

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)

    def _BuildBottomFrameContent(self, frame: Frame, fontConfig) :

        btn_clr = Button(
            frame,
            text="Clear",
            font=fontConfig,
            command=self.btn_clr_action
        )

        btn_eq = Button(
            frame,
            text="=",
            font=fontConfig,
            command=self.btn_eq_action
        )

        btn_clr.grid(row=0, column=0, sticky="news")
        btn_eq.grid(row=0, column=1, sticky="news")

        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)

    def btn_clr_action(self) :
        print("BOTÃO clear acionado")

    def btn_eq_action(self) :
        print("BOTÃO = acionado")

# CHAMADA DA CALCULADORA
Calculator()
