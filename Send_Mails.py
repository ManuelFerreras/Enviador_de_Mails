import smtplib

seguir = 1

conn = smtplib.SMTP('smtp.gmail.com', 587)

conn.ehlo()
conn.starttls()

emisor = 'ejemplo@gmail.com' # Su email.
token = 'e87hfdjne71' # Token del email para uso de third-party apps.

conn.login(emisor, token) # Datos del usuario

while seguir == 1:
    destinatario = input('\nIngrese el mail del destinatario: ')
    mensaje = input('\nIngrese el mensaje del texto: \n')
    
    conn.sendmail(emisor, destinatario, mensaje) 

    print('\nMail enviado con exito...')

    try:
        seguir = int(input("\nSi desea enviar otro mail, ingrese 1: "))
    except:
        seguir = 0
        print("\nNos vemos")
        
conn.quit()
