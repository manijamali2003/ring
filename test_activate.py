import ring

r2 = ring.ring2()
r2.set_owner('Mani Jamali')
r2.set_company('Pasand Team')
r2.set_email('manijamali2003@gmail.com')
r2.set_key('R-1245')
r2.set_license('ITPLv3')
r2.set_limit_free(30) # 30 days you can use as free
r2.set_limit_commercial(100) # 100 days after 30 days you can use this app
r2.set_os_supports('Windows|Linux') # Both Windows and Linux
r2.set_website('www.itpasand.com')
r2.set_license_file('README.md')
r2.create()