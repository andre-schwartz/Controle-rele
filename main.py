import RPi.GPIO as GPIO                                    #| #include <Raspberry.h>
import interface                                           #| #include <interface.h>
                                                           #|    
GPIO.setwarnings(False)                                    #|    
                                                           #|    
# SETUP DAS PORTAS                                         #| void setup() {
#GPIO.setmode(GPIO.BOARD) # CONTAGEM FISICA DOS PINOS      #|    
GPIO.setmode(GPIO.BCM) #CONTAGEM DO PINOUT, Nº GPIO        #|    
GPIO.setup(2, GPIO.OUT)                                    #|    pinMode(2, OUTPUT);    
                                                           #|    
GPIO.output(2, False)                                      #|    digitalWrite(2, LOW);
                                                           #| }    
                                                           #|    
# LOOP PARA MANTER JANELA ATIVA                            #| void loop() {   
janela.mainloop()                                       #|    interface.loop();
                                                           #| }