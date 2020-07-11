import ring

r = ring.ring1()
key = r.check('Pasand Team','PCLv1','R-2356')

if key==False:
    print ("Fake license")
else:
    print ("Welcome to this commercial application!")
