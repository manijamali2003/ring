# ring

Ring (c) 2020 Mani Jamali. MIT License

# How to use it?

```shell script
git clone https://github.com/manijamali2003/ring
```

## How to use ring v1 in my codes? ##

- Create your license (license.py just in your system):

```python
import ring

ring.ring1.create ('Your Company name','Your license name','R-nnnn') ## Instead of nnnn enter 4th digit number e.g. R-1234
```

- Run license script
- Create your main script code for your app:

```python
import ring

key = ring.ring1.check ('Your Company name','Your license name','R-nnnn') ## Instead of nnnn enter 4th digit number e.g. R-1234

if key==True:
    print ("Welcome to this commercial app!")
else:
    print ("Please buy this app, now you are use fake or unreal license")
```

- You should compile your app with python compilers
- Then send your app and LICENSE.rvd (created by ring1) to your customer and earn some money
