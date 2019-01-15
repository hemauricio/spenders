from include.modules import smtp

def main():
    _smtp = smtp.SMTP()
    _smtp.open_connection()
    _smtp.create_msg()
    _smtp.send_email()
    _smtp.close_connection()

if __name__ == "__main__":
    main()
