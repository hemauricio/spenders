from datetime import datetime

def today(as_string=False, format="%Y-%m-%d"):
    _today = datetime.today()
    if as_string:
        return _today.strftime(format)
    return _today
