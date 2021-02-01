import datetime

def convert(Sekunde):
    return str(datetime.timedelta(seconds = Sekunde))
Sekunde = 264
print(convert(Sekunde))