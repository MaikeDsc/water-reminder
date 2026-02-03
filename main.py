import time
from plyer import notification

def lembrete():
    notification.notify(
        title = 'como vai a hidratação?',
        message = 'ja é hora de dar um gole d\'água !',
        app_icon = 'garrafa.ico',
        timeout = 10, 
    )

print("/" * 60)
print("-- bem vindo ao Water reminder! --".center(60, '/'))
print("/" * 60)

print("\nQual o intevalo de tempo pata receber as notificações? \n")

# converte os minutos em segundos para o time.sleep
minutos = int (input("Digite os minutos desejados de intevalo aqui : "))
tempo  = minutos * 60


#eviará a notificação a cada 45 minutos
print(f"\nNotificações configuradas para cada {minutos} minutos. \n-- Water reminder ativo ! -- ")
while True:
    lembrete()
    time.sleep(tempo)
