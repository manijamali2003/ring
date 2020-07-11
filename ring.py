# Ring (c) 2020 Mani Jamali. MIT License

import hashlib, sys, time,os, platform

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

## Ring v2 with 14 section ##
class ring2:
    ## RING INFORMATION ##

        ## AUTHER NAME ##
    owner = 'empty'
    def set_owner (self,value):
        self.owner = value

        ## COMPANY ##
    company = 'empty'
    def set_company (self,value):
        self.company = value

        ## EMAIL ##
    email = 'empty'
    def set_email (self,value):
        self.email = value

        ## WEBSITE ##
    website = 'empty'
    def set_website (self,value):
        self.website = value

        ## LICENSE NAME ##
    license = 'empty'
    def set_license (self,value):
        self.license = value

        ## LICENSE TEXT

    text = 'empty'
    def set_license_file (self,filename):
        file = open (filename,'r')
        self.text = file.read()
        file.close()

        ## LICENSE KEY ##
    key = 'empty'
    def set_key (self,value):
        self.key = value

        ## OPERATING SYSTEMS SUPPORT ##
    os = 'empty'
    def set_os_supports (self,value):
        self.os = value

        ## TRIAL FREE ##
    limit_free = 'empty'
    def set_limit_free (self,value):
        self.limit_free = str(value)

        ## TERIAL COMMERCIAL ##
    limit_commercial = 'empty'
    def set_limit_commercial (self,value):
        self.limit_commercial = str(value)

    def create(self):
        open('LICENSE.rvd', 'w')
        file = open('LICENSE.rvd', 'w')

        ## Header of RING-V2 ##
        file.write("RING-V2,") # 0
        file.write(hashlib.sha3_512('In the name of God, the Compassionate, the Merciful\nRING-V2 (c) 2020 Mani Jamali. FREE SOFTWARE MIT LICENSE'.encode()).hexdigest() + ",") # 1

        # RING BODY ##
        file.write(hashlib.sha3_512(self.owner.encode()).hexdigest() + ",") # 2
        file.write(hashlib.sha3_512(self.company.encode()).hexdigest() + ",") # 3
        file.write(hashlib.sha3_512(self.email.encode()).hexdigest() + ",") # 4
        file.write(hashlib.sha3_512(self.website.encode()).hexdigest() + ",") # 5
        file.write(hashlib.sha3_512(self.license.encode()).hexdigest() + ",") # 6
        file.write(self.text+',') # 7
        file.write(hashlib.sha3_512(self.os.encode()).hexdigest() + ",") # 8
        file.write(hashlib.sha3_512(self.limit_free.encode()).hexdigest() + ",") # 9
        file.write(hashlib.sha3_512(self.limit_commercial.encode()).hexdigest() + ",") # 10
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getctime("LICENSE.rvd"))).encode()).hexdigest() + ",") # 11
        file.write(hashlib.sha3_512(str(time.ctime(os.path.getmtime("LICENSE.rvd"))).encode()).hexdigest() + ",") # 12
        if self.key.startswith('R-'):
            file.write(hashlib.sha3_512(self.key.encode()).hexdigest() + ",") # 13
        file.close()

    def check (self):
        if os.path.isfile('LICENSE.rvd'):
            file = open('LICENSE.rvd', 'r')
            l = file.read()
            l = l.split(',')
            file.close()

            if l[0] == 'RING-V2':
                if l[1] == hashlib.sha3_512('In the name of God, the Compassionate, the Merciful\nRING-V2 (c) 2020 Mani Jamali. FREE SOFTWARE MIT LICENSE'.encode()).hexdigest():
                    if l[2] == hashlib.sha3_512(self.owner.encode()).hexdigest():
                        if l[3] == hashlib.sha3_512(self.company.encode()).hexdigest():
                            if l[4] == hashlib.sha3_512(self.email.encode()).hexdigest():
                                if l[5] == hashlib.sha3_512(self.website.encode()).hexdigest():
                                    if l[6] == hashlib.sha3_512(self.license.encode()).hexdigest():
                                        os = ''
                                        real_os = platform.system()
                                        # Linux
                                        # Windows
                                        # Mac # find in https://stackoverflow.com/questions/1854/what-os-am-i-running-on
                                        # Linux|Mac
                                        # Linux|Windows
                                        # Windows|Mac
                                        # Windows|Linux
                                        # Mac|Linux
                                        # Mac|Windows
                                        # All

                                        checkos = False

                                        if l[8]==hashlib.sha3_512('Linux'.encode()).hexdigest():
                                            if real_os=='Linux':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Windows'.encode()).hexdigest():
                                            if real_os=='Windows':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Mac'.encode()).hexdigest():
                                            if real_os=='Darwin':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Linux|Windows'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Windows|Linux'.encode()).hexdigest():
                                            if real_os=='Linux' or real_os=='Windows':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Linux|Mac'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Mac|Linux'.encode()).hexdigest():
                                            if real_os=='Linux' or real_os=='Darwin':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Windows|Mac'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Mac|Windows'.encode()).hexdigest():
                                            if real_os=='Windows' or real_os=='Darwin':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('Linux|Windows|Mac'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Linux|Mac|Windows'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Mac|Linux|Windows'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Mac|Windows|Linux'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Windows|Mac|Linux'.encode()).hexdigest() or l[8]==hashlib.sha3_512('Windows|Linux|Mac'.encode()).hexdigest():
                                            if real_os=='Linux' or real_os=='Darwin' or real_os=='Windows':
                                                checkos = True
                                            else:
                                                checkos = False

                                        elif l[8]==hashlib.sha3_512('All'.encode()).hexdigest():
                                            checkos = True

                                        elif l[8]=='empty':
                                            checkos = True
                                        else:
                                            checkos = False

                                        ## Check
                                        if checkos:

                                            free = 'empty'
                                            commercial = 'empty'

                                            ## Check free ##
                                            if l[9] == hashlib.sha3_512('empty'.encode()).hexdigest():
                                                free = True
                                            else:
                                                t = time.gmtime() ## Get all times for now
                                                y = t.tm_year
                                                m = t.tm_mon
                                                d = t.tm_mday
                                                
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