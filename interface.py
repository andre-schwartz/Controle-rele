from tkinter import *
import RPi.GPIO as GPIO

#FUNÇÃO AO CLICAR NO BOTAO
def mudaRele():                                            #| void mudaRele() {
    if (varStatus.get() == "DESLIGADO"):                   #|    if (varStatus.get() == "DESLIGADO") {
        varStatus.set("LIGADO")                            #|       varStatus.set("LIGADO");
        GPIO.output(2, True)                               #|       digitalWrite(2, HIGH);
                                                           #|    
        label_on.pack(padx = 100, pady = 20)               #|    
        label_off.pack_forget()                            #|    
                                                           #|    
    else:                                                  #|    } else {
        varStatus.set("DESLIGADO")                         #|       varStatus.set("DESLIGADO");
        GPIO.output(2, False)                              #|       digitalWrite(2, LOW);
                                                           #|    
        label_on.pack_forget()                             #|    
        label_off.pack(padx = 100, pady = 20)              #|    }
                                                           #| }    
#FIM DA FUNÇÃO

# CRIANDO JANELA DA INTERFACE GRAFICA
janela = Tk()
janela.title("Controle de Rele")
janela.configure(background="white")

#ADD BOTÕES
btn = Button(janela, text = "ON/OFF", command = mudaRele)
btn.pack(padx = 100, pady = 20)

#VARIAVEL PARA TEXTO
varStatus = StringVar(janela, "DESLIGADO")
#ADD TEXTO
status = Label(janela, textvariable = varStatus)
status.pack(padx = 100)

#ADD IMAGENS
img_off = PhotoImage( file = "botOff.png")
img_on  = PhotoImage( file = "botOn.png")

label_on  = Label(janela, image = img_on)
label_off = Label(janela, image = img_off)

label_off.pack(padx = 100, pady = 20)

# FIM DA JANELA 

# PARA TESTAR A JANELA NO PYTHON DO PC
#OBS. RETIRAR COMANDOS DE GPIO

if (__name__ == "__main__"):
    janela.mainloop()