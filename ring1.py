# Ring (c) 2020 Mani Jamali. MIT License

import hashlib, sys, time,os

## Create License ##
def create (owner,license,key1):
    open ('LICENSE.rvd','w')
    file = open ('LICENSE.rvd','w')
    file.write("RING-V1,")
    file.write(hashlib.sha3_512('In the name of God, the Compassionate, the Merciful'.encode()).hexdigest()+",")
    file.write(hashlib.sha3_512(owner.encode()).hexdigest()+",")
    file.write(hashlib.sha3_512(license.encode()).hexdigest()+",")
    # https://www.w3resource.com/python-exercises/python-basic-exercise-64.php
    file.write (hashlib.sha3_512(str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest()+",")
    file.write (hashlib.sha3_512(str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest() + ",")
    if key1.startswith('R-'):
        file.write(hashlib.sha3_512(key1.encode()).hexdigest()+",")
    file.close()

## Embeded License ##
def check (owner,license,key1):
    file = open ('LICENSE.rvd','r')
    l = file.read()
    l = l.split(',')
    file.close()

    ## Conditions ##
    if l[0]=='RING-V1':
        if l[1]==hashlib.sha3_512('In the name of God, the Compassionate, the Merciful'.encode()).hexdigest():
            if l[2]==hashlib.sha3_512(owner.encode()).hexdigest():
                if l[3]==hashlib.sha3_512(license.encode()).hexdigest():
                    if l[4]==hashlib.sha3_512(str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest():
                        if l[5]==hashlib.sha3_512(str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest():
                            if l[6]==hashlib.sha3_512(key1.encode()).hexdigest():
                                return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

create('hello','GPLv3','R-1435')
print (check('hello','GPLv3','R-1435'))