duration: int = int(input("duration in seconds"))
days = duration//86400
hours = (duration - days*86400)//3600
minutes = (duration - days*86400 - hours*3600)//60
seconds = duration - days*86400 - hours*3600 - minutes*60
print(f"result days:hours:minutes:seconds {days} : {hours} : {minutes} : {seconds}")