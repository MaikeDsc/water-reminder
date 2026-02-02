import time
from plyer import notification

def lembrete():
    notification.notify(
        title = 'como vai a hidratação?',
        message = 'ja é hora de dar um gole d\'água !',
        app_icon = 'garrafa.ico',
        timeout = 10, 
    )

#eviará a notificação a cada 42 minutos
while True:
    lembrete()
    time.sleep(45*60)
