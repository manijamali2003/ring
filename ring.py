# Ring (c) 2020 Mani Jamali. MIT License

import hashlib, sys, time,os

## Ring 1 ##
class ring1:
    ## Create License with 7 section ##
    def create(self,owner, license, key1):
        open('LICENSE.rvd', 'w')
        file = open('LICENSE.rvd', 'w')
        file.write("RING-V1,")
        file.write(hashlib.sha3_512('In the name of God, the Compassionate, the Merciful'.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(owner.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(license.encode()).hexdigest() + ",")
        # https://www.w3resource.com/python-exercises/python-basic-exercise-64.php
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest() + ",")
        if key1.startswith('R-'):
            file.write(hashlib.sha3_512(key1.encode()).hexdigest() + ",")
        file.close()

    ## Embeded License ##
    def check(self,owner, license, key1):
        if os.path.isfile('LICENSE.rvd'):
            file = open('LICENSE.rvd', 'r')
            l = file.read()
            l = l.split(',')
            file.close()

            ## Conditions ##
            if l[0] == 'RING-V1':
                if l[1] == hashlib.sha3_512('In the name of God, the Compassionate, the Merciful'.encode()).hexdigest():
                    if l[2] == hashlib.sha3_512(owner.encode()).hexdigest():
                        if l[3] == hashlib.sha3_512(license.encode()).hexdigest():
                            if l[4] == hashlib.sha3_512(
                                    str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest():
                                if l[5] == hashlib.sha3_512(
                                        str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest():
                                    if l[6] == hashlib.sha3_512(key1.encode()).hexdigest():
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
        else:
            return False

## Ring v2 with 15 section ##
class ring2:
    ## RING INFORMATION ##

        ## AUTHER NAME ##
    owner = ''
    def set_owner (self,value):
        self.owner = value

        ## COMPANY ##
    company = ''
    def set_company (self,value):
        self.company = value

        ## EMAIL ##
    email = ''
    def set_email (self,value):
        self.email = value

        ## WEBSITE ##
    website = ''
    def set_website (self,value):
        self.website = value

        ## LICENSE NAME ##
    license = ''
    def set_license (self,value):
        self.license = value

        ## LICENSE TEXT

    text = ''
    def set_license_file (self,filename):
        file = open (filename,'r')
        self.text = file.read()
        file.close()

        ## LICENSE KEY ##
    key = ''
    def set_key (self,value):
        self.key = value

        ## OPERATING SYSTEMS SUPPORT ##
    os = ''
    def set_os_supports (self,value):
        self.os = value

        ## TRIAL FREE ##
    limit_free = ''
    def set_limit_free (self,value):
        self.limit_free = str(value)

        ## TERIAL COMMERCIAL ##
    limit_commercial = ''
    def set_limit_commercial (self,value):
        self.limit_commercial = str(value)

    def create(self):
        open('LICENSE.rvd', 'w')
        file = open('LICENSE.rvd', 'w')

        ## Header of RING-V2 ##
        file.write("RING-V2,")
        file.write(hashlib.sha3_512('In the name of God, the Compassionate, the Merciful\nRING-V2 (c) 2020 Mani Jamali. FREE SOFTWARE MIT LICENSE'.encode()).hexdigest() + ",")

        # RING BODY ##
        file.write('Do not edit this license,') # tell to hackers
        file.write(hashlib.sha3_512(self.owner.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(self.company.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(self.email.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(self.website.encode()).hexdigest() + ",")
        file.write(self.license.encode() + ",")
        file.write(self.text+',')
        file.write(hashlib.sha3_512(self.os.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(self.limit_free.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(self.limit_commercial.encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest() + ",")
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest() + ",")
        if self.key.startswith('R-'):
            file.write(hashlib.sha3_512(self.key.encode()).hexdigest() + ",")
        file.close()