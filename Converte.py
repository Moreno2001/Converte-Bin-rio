# ==================================================================================================@
# *AUTOR: Moreno Wande C. Baptista                   IDADE: 17
# *Data: 01/06/2018                                  PAÍS: ANGOLA
# *Facebook: https://www.facebook.com/moreno.wande.herinel
# ==================================================================================================@

# ==================================================================================================@
# * Um grupo anónimo com nome "Desconhecido", comunica-se com uma linguagem específica,
# * onde (A1B1111-A11A11B-111D1-B1E-A1B11A1-A111A1A1-A11A111A-A11B1B-A11A1111), quer dizer,
# * Olá Mundo, ajude a Agência de Contra-Inteligência, e crie um Programa,
# * que consegue traduzir este código. Bônus: crie uma interface gráfica usando o tkinter.
# ==================================================================================================@

import tkinter
import binascii
import platform
#from testes import  isbin, separa
#from tkinter import messagebox

def separa(string, ch):
    j = 8
    k = 0
    i = 0
    nstr = ''
    for i in range(int(len(string) / 8)):
        nstr = nstr + (string[k:j] + ch)
        
        k += 8
        j += 8
        i += 1
    #w = nstr[:len(nstr) - 1]
    return nstr

def mlpl():
    nlis = list()
    for i in range(len(self.function_)):
        nlis += self.function_[i]
    return nlis

def isbin(string):
    cont = int()
    for i in string:
        if i != '1' and i != '0':
            cont += 1
    if cont > 0:
        return False
    else: return True


class Program:
    # ==================================================================================================@
    # ===================================================================================================@
    def __init__(self, master):
        # global
        self.mastersobre = None
        self.defin = None
        self.gambiarra = int()
        self.colordef = 'white'
        #self.dec = int()
        # características dos Text
        self.larg_Texts = 36
        self.alt_Texts = 10
        self.arquitect = platform.architecture()[0]
        self.lim = int()

        if '64' in self.arquitect:
            self.lim = 20001
        else: self.lim = 10001

        # características dos botões
        self.colorbuttons = 'gray60'
        self.colorbuttonsfg = 'white'
        self.fonte = tuple(('Verdana', '10'))

        # características das janelas
        self.geometry_ = '700x370+200+100'
        self.background_ = 'white'
        self.c1bg = 'gray62'
        self.colortitlefg = 'gray24'
        self.colormsgfg = 'black'

        # Opções da janela
        master.resizable(False, False)
        master.geometry(self.geometry_)
        master.title('Decrypter 1.0')
        master['bg'] = self.background_
        
        # Frames
        self.f1 = tkinter.Frame(master)
        self.f1['bg'] = self.background_
        self.c1 = tkinter.Frame(master,
                                bg = self.c1bg,
                                bd = '30')
        self.f2 = tkinter.Frame(master)
        self.f2['bg'] = self.background_

        # Título
        self.titulo = tkinter.Label(master)
        self.titulo['text'] = 'Decrypter'
        self.titulo['bg'] = self.background_
        self.titulo['fg'] = self.colortitlefg
        self.titulo['font'] = ('Algerian 30 bold')
        self.titulo['bd'] = 10

        # criando imagem de fundo
        #self.Image = tkinter.PhotoImage(file = 'fundo.png')
        #w = tkinter.Label(self.c1, image = self.Image, bd = 0)
        #w.Image = self.Image
        #w.place(x = -1000, y = -200)

        # Menu's
        self.menubar = tkinter.Menu(master)
        self.arquivos = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Arquivos', menu=self.arquivos)
        self.arquivos.add_command(label='Definições', command = self.definicoes)

        self.arquivos.add_separator()

        self.arquivos.add_command(label='Sair', command=self.sair)

        self.editar = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Editar', menu=self.editar)

        self.editar.add_command(label='Descodificar',
                                   command=self.convert)
        self.editar.add_command(label='Converter',
                                   command=self.invert)
        self.editar.add_command(label='Limpar', command=self.limpar)

        self.editar.add_command(label = 'Converter para Binário', command = self.invertBin)

        self.ver = tkinter.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='Ver', menu=self.ver)

        self.ver.add_command(label='Sobre', command=self.sobre)
        self.ver.add_separator()
        self.ver.add_command(label = 'Ajuda', command = self.ajuda)

        master.config(menu=self.menubar)

        # ==============================================================================@
        #                                   MENSAGENS
        # ==============================================================================@
        self.msg1 = tkinter.Label(self.f1)
        self.msg1['text'] = 'Código'
        self.msg1['font'] = ('Verdana 8 bold italic')
        self.msg1['background'] = self.background_
        self.msg1['fg'] = self.colormsgfg

        self.msg2 = tkinter.Label(self.f1)
        self.msg2['text'] = 'Texto'
        self.msg2['font'] = ('Verdana 8 bold italic')
        self.msg2['background'] = self.background_
        self.msg2['fg'] = self.colormsgfg

        self.msglimit = tkinter.Label(self.f1)
        self.msglimit['text'] = '-'+str(self.lim)
        self.msglimit['font'] = ('Verdana 7')
        self.msglimit['background'] = self.background_
        self.msglimit['fg'] = self.colormsgfg

        self.msg3 = None

        # ==============================================================================@
        #             BARRA DE ROLAGEM E TEXT'S PARA ENTRADA E SAÍDA DE DADOS
        # ==============================================================================@

        self.entrada = tkinter.Text(self.c1)
        self.barra = tkinter.Scrollbar(self.c1)

        self.barra['orient'] = tkinter.VERTICAL
        self.barra['command'] = self.entrada.yview

        self.entrada['yscrollcommand'] = self.barra.set
        self.entrada['width'] = self.larg_Texts
        self.entrada['height'] = self.alt_Texts
        # self.entrada.bind('<Return>', self.convert)
        self.entrada.focus_force()

        self.barra2 = tkinter.Scrollbar(self.c1, orient=tkinter.VERTICAL)
        self.saida = tkinter.Text(self.c1, yscrollcommand=self.barra2.set)
        self.saida['width'] = self.larg_Texts
        self.saida['height'] = self.alt_Texts
        self.barra2['command'] = self.saida.yview

        # ===============================================================================@
        #                                     BOTÕES
        # ===============================================================================@

        self.botaodescodificar = tkinter.Button(self.f2)
        self.botaodescodificar['text'] = 'Descodificar'
        self.botaodescodificar['command'] = self.convert
        self.botaodescodificar['width'] = 12
        self.botaodescodificar['height'] = 1
        self.botaodescodificar['bg'] = self.colorbuttons
        self.botaodescodificar['fg'] = self.colorbuttonsfg
        #self.botaodescodificar['relief'] = tkinter.RIDGE
        self.botaodescodificar['font'] = self.fonte

        # Inverter Botão
        self.botaoinverso = tkinter.Button(self.f2)
        self.botaoinverso['text'] = 'Converter'
        self.botaoinverso.config(width=12,
                                 height=1,
                                 bg=self.colorbuttons,
                                 fg=self.colorbuttonsfg,
                                 font=self.fonte,
                                 command=self.invert)
        self.botaoinverso.bind('<Button-3>', self.invertBin)

        # ==============================================================================@
        #                               GERENCIAMENTO DE LEYOUT'S
        # ===============================================================================@
        self.titulo.pack()

        self.f1.pack()
        self.msg1.pack(side = tkinter.LEFT)
        self.msg2.pack(side = tkinter.LEFT, padx = 210)
        self.msglimit.pack(side = tkinter.LEFT)

        self.c1.pack()
        self.barra.pack(side=tkinter.LEFT, fill=tkinter.Y)
        self.entrada.pack(side=tkinter.LEFT)
        self.saida.pack(side=tkinter.LEFT)
        self.barra2.pack(side=tkinter.LEFT, fill=tkinter.Y)

        self.f2.pack(pady = 12)
        self.botaodescodificar.pack(side = tkinter.LEFT)
        self.botaoinverso.pack(side = tkinter.LEFT, padx = 182)

        # ===============================================================================@
        #                                    MÉTODOS
        # ==============================================================================@

    def sobre(self):
        traços = '\n' + '-' * 30 + '\n\n'
        control = tkinter.Toplevel()
        control['bg'] = 'white'
        #control.geometry('500x300+200+90')
        control.resizable(False, False)
        control.grab_set()
        control.focus_force()
        control.title('Sobre')
        
        self.mastersobre = control
        msg = tkinter.Label(self.mastersobre)
        msg['font'] = ('Verdana', '13', 'bold')
        msg['text'] = f"Decrypter v2.0-biconver{traços}" \
                      "Criador: Moreno Baptista\n" \
                      "Data da Atualização: 04/06/2018\n" \
                      "Data de Criação: 31/05/2018\n" \
                      "Participação: Motchodeny"
        msg['bg'] = control['bg']
        msg.pack(padx=1, pady=40)

        self.mastersobre.mainloop()
    def ajuda(self):
        ajuda = tkinter.Toplevel()
        ajuda.transient(master)
        ajuda.focus_force()
        ajuda.grab_set()

        ajuda['bg'] = 'white'
        ajuda.title('Ajuda')
        ajuda.geometry('+300+200')
        info = tkinter.Label(ajuda, text = 'Podes traduzir códigos em binários,\n'
                                           'Traduzir códigos em linguagem anónima que é feita de 1\'s e letras\n'
                                           'Podes Mudar a cor do programa no Menu Arquivos>Definições\n'
                                           'Podes Traduzir de Textos para binários ou para linguagem anónima\n'
                                           'Clique sobre o botão converter com\no botão direito do mouse para converter em binário'
                                           '\n\n'
                                           'Para um bom funcionamento Traduza textos com 20000\n'
                                           'letras para plataformas 64 bits\n'
                                           'e 10000 para plataformas 32 bits\n'
                                           'Na pasta font você encontra o código fonte deste programa\n'
                                           'É permitido alterações, preciso...\n'
                                           ,
                             bg = ajuda['bg'],
                             fg = 'black'
                                           )

        info.pack()

    def definicoes(self):
        self.defin = tkinter.Toplevel()
        self.defin.title('Definições')
        self.defin.geometry('400x250+200+100')
        self.defin['bg'] = self.colordef

        self.defin.focus_force()
        self.defin.transient(master)
        self.defin.grab_set()

        btmudarcor = tkinter.Button(self.defin,
                                    width = 10,
                                    height = 1,
                                    text = 'Mudar de Cor',
                                    command = self.mudarcor,
                                    bg='gray99')
        reverter = tkinter.Button(self.defin,
                                    width=10,
                                    height=1,
                                    text='Reverter',
                                  command = self.reverter,
                                  bg='gray99')

        self.msg3 = tkinter.Label(self.defin, bg = self.colordef)

        fechar = tkinter.Button(self.defin,
                                    width=10,
                                    height=1,
                                    text='fechar',
                                    command = self.fechardefin,
                                    bg = 'gray99')
        btmudarcor.pack(pady = 20)
        reverter.pack()
        self.msg3.pack(pady =10)
        fechar.pack(side = tkinter.BOTTOM, pady = 10)
        
    def fechardefin(self):
        self.defin.destroy()
        
    def mudarcor(self):
        back = 'gray20'
        master['bg'] = back
        self.defin['bg'] = back
        self.titulo['bg'] = back
        self.titulo['fg'] = 'white'
        self.f1['bg'] = back
        self.f2['bg'] = back
        self.c1['bg'] = 'darkred'

        self.msg1['bg'] = back
        self.msg1['fg'] = 'white'
        self.msg2['bg'] = back
        self.msg2['fg'] = 'white'

        self.botaodescodificar.config(font = ('Verdana 10 italic'),
                                      bg = 'white',
                                      fg = 'black')
        self.botaoinverso.config(font = ('Verdana 10 italic'),
                                 bg = 'white',
                                 fg = 'black')
        self.msg3['text'] = 'Olá!!! Como estás?'
        self.msg3['font'] = ('Verdana 15 bold italic')
        self.msg3['bg'] = back
        self.msg3['fg'] = 'white'
        self.gambiarra = 1

    def reverter(self):
        back = self.background_
        master['bg'] = back
        self.defin['bg'] = self.colordef
        self.titulo['bg'] = back
        self.titulo['fg'] = self.colortitlefg
        self.f1['bg'] = back
        self.f2['bg'] = back
        self.c1['bg'] = self.c1bg

        self.msg1['bg'] = back
        self.msg1['fg'] = self.colormsgfg
        self.msg2['bg'] = back
        self.msg2['fg'] = self.colormsgfg
        
        if self.gambiarra is 1:
            self.msg3['text'] = 'Eu estou Bem!! desde já...'
            self.gambiarra = 0
            
        self.msg3['bg'] = self.background_
        self.msg3['fg'] = self.colortitlefg

        self.botaodescodificar.config(font=self.fonte,
                                      bg = self.colorbuttons,
                                      fg = self.colorbuttonsfg)
        self.botaoinverso.config(font=self.fonte,
                                 bg = self.colorbuttons,
                                 fg = self.colorbuttonsfg)

    def sair(self):
        master.destroy()

    def limpar(self):
        self.entrada.delete(0.0, tkinter.END)
        self.saida.delete(0.0, tkinter.END)

        # convert: função para o botão descodificar

    def convert(self, param=None):
        text = self.entrada.get(0.0, tkinter.END)  # Dando o valor encontrado no Text de entrada numa var. text
        text = text.lower()# transformando toda string em minúsculo
        
        outstr = str()
        for i in text:
            if (i == 'a'):
                outstr = '0'
                text = text.replace(i, outstr)
            elif (i == 'b'):
                outstr = '0' * 2
                text = text.replace(i, outstr)
            elif (i == 'c'):
                outstr = '0' * 3
                text = text.replace(i, outstr)
            elif (i == 'd'):
                outstr = '0' * 4
                text = text.replace(i, outstr)
            elif (i == 'e'):
                outstr = '0' * 5
                text = text.replace(i, outstr)
            elif (i == 'f'):
                outstr = '0' * 6
                text = text.replace(i, outstr)
            elif (i == 'g'):
                outstr = '0' * 7
                text = text.replace(i, outstr)
            elif (i == 'h'):
                outstr = '0' * 8
                text = text.replace(i, outstr)
            elif (i == 'i'):
                outstr = '0' * 9
                text = text.replace(i, outstr)
            elif (i == 'j'):
                outstr = '0' * 10
                text = text.replace(i, outstr)
            elif (i == 'k'):
                outstr = '0' * 11
                text = text.replace(i, outstr)
            elif (i == 'l'):
                outstr = '0' * 12
                text = text.replace(i, outstr)
            elif (i == 'm'):
                outstr = '0' * 13
                text = text.replace(i, outstr)
            elif (i == 'n'):
                outstr = '0' * 14
                text = text.replace(i, outstr)
            elif (i == 'o'):
                outstr = '0' * 15
                text = text.replace(i, outstr)
            elif (i == 'p'):
                outstr = '0' * 16
                text = text.replace(i, outstr)
            elif (i == 'q'):
                outstr = '0' * 17
                text = text.replace(i, outstr)
            elif (i == 'r'):
                outstr = '0' * 18
                text = text.replace(i, outstr)
            elif (i == 's'):
                outstr = '0' * 19
                text = text.replace(i, outstr)
            elif (i == 't'):
                outstr = '0' * 20
                text = text.replace(i, outstr)
            elif (i == 'u'):
                outstr = '0' * 21
                text = text.replace(i, outstr)
            elif (i == 'v'):
                outstr = '0' * 22
                text = text.replace(i, outstr)
            elif (i == 'w'):
                outstr = '0' * 23
                text = text.replace(i, outstr)
            elif (i == 'x'):
                outstr = '0' * 24
                text = text.replace(i, outstr)
            elif (i == 'y'):
                outstr = '0' * 25
                text = text.replace(i, outstr)
            elif (i == 'z'):
                outstr = '0' * 26
                text = text.replace(i, outstr)
            else:
                pass

        self.saida.delete(0.0, tkinter.END)

        text = text.replace('\n', '')

        text = str(self.binstr(text))

        text = text.replace('\n', '')
        
        self.saida.insert(tkinter.END, text + '')  # Passando o texto já convertido para Text de saída

    def invert(self):
        text = self.saida.get(0.0, tkinter.END)
        
        text = self.strbin(text)
        text = self.funcinv(text)
        
        self.entrada.delete(0.0, tkinter.END)
        self.entrada.insert(tkinter.END, text)

    def invertBin(self, event = None):
        text = self.saida.get(0.0, tkinter.END)
        text = self.strbin(text)
        text = separa(text, ' ')
        self.entrada.delete(0.0, tkinter.END)
        self.entrada.insert(tkinter.END, text + '')

    def funcinv(self, string):
        string = string.replace('0' * 26, 'Z')
        string = string.replace('0' * 25, 'Y')
        string = string.replace('0' * 24, 'X')
        string = string.replace('0' * 23, 'W')
        string = string.replace('0' * 22, 'V')
        string = string.replace('0' * 21, 'U')
        string = string.replace('0' * 20, 'T')
        string = string.replace('0' * 19, 'S')
        string = string.replace('0' * 18, 'R')
        string = string.replace('0' * 17, 'Q')
        string = string.replace('0' * 16, 'P')
        string = string.replace('0' * 15, 'O')
        string = string.replace('0' * 14, 'N')
        string = string.replace('0' * 13, 'M')
        string = string.replace('0' * 12, 'L')
        string = string.replace('0' * 11, 'K')
        string = string.replace('0' * 10, 'J')
        string = string.replace('0' * 9, 'I')
        string = string.replace('0' * 8, 'H')
        string = string.replace('0' * 7, 'G')
        string = string.replace('0' * 6, 'F')
        string = string.replace('0' * 5, 'E')
        string = string.replace('0' * 4, 'D')
        string = string.replace('0' * 3, 'C')
        string = string.replace('0' * 2, 'B')
        string = string.replace('0', 'A')
        return string

    # =============================================================================================================*#
    # *                             Funções que Convertem de Binário pra Strings e vice-versa                      *#
    # *============================================================================================================*#

    def binstr(self, bits, encoding='latin-1', errors='surrogatepass'):
        try:
            if len(bits) < 1:
                return "O quê? Sou apenas um código?\n" \
                       " O binário sempre teve razão,\n" \
                       " como puderam fazer isso comigo?\n" \
                       " odeio todos vocês seres humanos\n"
            #elif bits.isalpha():
            #    return
            bits = bits.replace(' ', str())
            n = int(bits, 2)
            
            return self.int2bytes(n).decode(encoding, errors)
        except:
            encoding = 'utf-8'
            if len(bits) < 1:
                return "O quê? Sou apenas um código?\n" \
                       " O binário sempre teve razão,\n" \
                       " como puderam fazer isso comigo?\n" \
                       " odeio todos vocês seres humanos\n"
            if not(isbin(bits)):
                return 'Apenas Binários'
            bits = bits.replace(' ', str())
            n = int(bits, 2)
            
            return self.int2bytes(n).decode(encoding, errors)

    def strbin(self, text, encoding='latin-1', errors='surrogatepass'):
        try:
            if text in ' \n\t':
                return self.strbin('https://www.facebook.com/moreno.wande.herinel')
            text = text[:self.lim]
            bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
            return bits.zfill(8 * ((len(bits) + 7) // 8))
        except:
            encoding = 'utf-8'
            if text in ' \n\t':
                return self.strbin('https://www.facebook.com/moreno.wande.herinel')
            text = text[:self.lim]
            bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
            return bits.zfill(8 * ((len(bits) + 7) // 8))

    def int2bytes(self, i):
        hex_string = '%x' % i
        n = len(hex_string)
        return binascii.unhexlify(hex_string.zfill(n + (n & 1)))


# ======================================================================================@
# ======================================================================================@

master = tkinter.Tk()
Program(master)
master.mainloop()
