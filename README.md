# Spenders
Personal app for better money management

**Execute Spenders**
 ```console
mmhernandez@spenders:~$ python main.py
```

**secrets**
You're going to need a secrets package containing a secrets.py module.

```
spenders
│   README.md
│   config.py    
│   LICENSE    
│   main.py    
│
└───include
│   │   __init__.py
│   │
│   └───modules
│       │   __init__.py
│       │   smtp.py
│   
└───secrets
    │   __init__.py
    │   secrets.py
```

**__init__.py**
```python
__all__ = ["secrets"] # mysterious purposes

from. import *
```

**secrets.py**
```python
# Configurations

# From Email
FEMAIL = "from_email@gmail.com"

# App password
PASSWORD = "your_app_password"

# PASSWORD = "regular_password"

# To Email
TEMAIL = "to_email@gmail.com"
```

**_App password_ and _regular password_**
I am using an _app password_ Gmail provided me due to the 2 step authentication I have in my from_email@gmail.com. You can create one yourself following [this tutorial](https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882).
If you do not have 2 step authentication you can use your _regular password_, the one you use to log into your account.
