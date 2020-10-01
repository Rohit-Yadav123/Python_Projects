import time
from plyer import notification
if __name__=='__main__':
    while(True):

        notification.notify(
            title="Please Drink Water Now!",
            message='It is very necessory for health',
            timeout=3
        )
        time.sleep(60*60)
#THIS IS CODE
