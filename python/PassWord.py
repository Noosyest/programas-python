from tkinter import *

janela_2 = Tk()
janela_2.geometry('300x180+100+100')
janela_2.title('Registrar')

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

numero = ''

def registrar():
        if len(cx.get()) <= 5:
                if str(cx.get()).isnumeric():
                        janela = Tk()
                        janela.geometry('200x180+100+100')
                        janela.title('Senha')


                        def zero():
                                zero = numeros[0]
                                global numero
                                numero = str(numero) + str(zero)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def um():
                                um = numeros[1]
                                global numero
                                numero = str(numero) + str(um)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                        def dois():
                                dois = numeros[2]
                                global numero
                                numero = str(numero) + str(dois)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def tres():
                                tres = numeros[3]
                                global numero
                                numero = str(numero) + str(tres)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def quatro():
                                quatro = numeros[4]
                                global numero
                                numero = str(numero) + str(quatro)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def cinco():
                                cinco = numeros[5]
                                global numero
                                numero = str(numero) + str(cinco)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def seis():
                                seis = numeros[6]
                                global numero
                                numero = str(numero) + str(seis)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def sete():
                                sete = numeros[7]
                                global numero
                                numero = str(numero) + str(sete)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def oito():
                                oito = numeros[8]
                                global numero
                                numero = str(numero) + str(oito)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def nove():
                                nove = numeros[9]
                                global numero
                                numero = str(numero) + str(nove)
                                lb_1['text'] = numero
                                if len(numero) >= 6:
                                        lb_1['text'] = ' '
                                        numero = ''
                        def ok():
                                global numero
                                if lb_1['text'] == cx.get():
                                        lb_1['text'] = 'Acertou!'
                                        numero = ''
                                else:
                                        lb_1['text'] = 'Errou'
                                        numero = ''
                        def apagar():
                                global numero
                                numero = lb_1['text'][0:len(numero)-1]
                                lb_1['text'] = numero
                        def tudo():
                                global numero
                                numero = lb_1['text'] = ''


                        bt_ok = Button(janela, width=6, text='OK', command=ok)

                        bt_apagar = Button(janela, width=4, text='<<', command= apagar)
                        bt_tudo = Button(janela, width=4, text='APAGAR', command=tudo)


                        bt_0 = Button(janela, width=1, text=0, command= zero)
                        bt_1 = Button(janela, width=1, text=1, command= um)
                        bt_2 = Button(janela, width=1, text=2, command= dois)
                        bt_3 = Button(janela, width=1, text=3, command= tres)
                        bt_4 = Button(janela, width=1, text=4, command= quatro)
                        bt_5 = Button(janela, width=1, text=5, command= cinco)
                        bt_6 = Button(janela, width=1, text=6, command= seis)
                        bt_7 = Button(janela, width=1, text=7, command= sete)
                        bt_8 = Button(janela, width=1, text=8, command= oito)
                        bt_9 = Button(janela, width=1, text=9, command= nove)

                        lb_1 = Label(janela, text='')

                        bt_1.grid(row=0, column=0)
                        bt_2.grid(row=0, column=1)
                        bt_3.grid(row=0, column=2)
                        bt_4.grid(row=1, column=0)
                        bt_5.grid(row=1, column=1)
                        bt_6.grid(row=1, column=2)
                        bt_7.grid(row=2, column=0)
                        bt_8.grid(row=2, column=1)
                        bt_9.grid(row=2, column=2)
                        bt_0.grid(row=3, column=0)
                        bt_ok.place(x=36, y=84)

                        bt_apagar.grid(row=0, column=3)
                        bt_tudo.grid(row=1, column=3)

                        lb_1.place(x= 0, y=130)

                        janela.mainloop()
                else:
                        lb_aviso['text'] = 'Você deve digitar apenas números'
        else:
                lb_aviso['text'] = 'Sua senha deve ter 5 caracteres ou menos'

cx = Entry(janela_2, )
bt = Button(janela_2, width=5, text='OK', command=registrar)
lb = Label(janela_2, text='Digite sua senha')
lb_aviso = Label(janela_2, text='')



lb.pack()
cx.pack()
bt.pack()
lb_aviso.pack()

janela_2.mainloop()