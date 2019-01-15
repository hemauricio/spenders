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

# **_App password_ and _regular password_**

On **secrets.py** I am referencing two types of _PASSWORD_.

**App password:**

The account I am using to send emails has 2 step authentication activated, you
can not login with smtplib using the regular password you use on the Gmail
interface.

To be able to login with smtplib for an account with 2 step authentication
you will need an **_app password_**. You can create one yourself following [this tutorial](https://www.lifewire.com/get-a-password-to-access-gmail-by-pop-imap-2-1171882).

**Regular password:**

If you are going to use an account that does not have 2 step authentication you can use your **_regular password_**, the one you use to log into your account.
