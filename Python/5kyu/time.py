import time
def make_readable(seconds):
    a = time.gmtime(seconds)
    hr = a.tm_hour
    if seconds==359999:
        hr = 99
        return str('%02d'%(hr))+':'+str('%02d'%(a.tm_min))+':'+str('%02d'%(a.tm_sec))
    else:
        return str('%02d'%(hr))+':'+str('%02d'%(a.tm_min))+':'+str('%02d'%(a.tm_sec))a
