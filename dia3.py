
##Desafío del día 3

nombres=[] #lista de nombres
apellidos_lista=[]#lista de apellidos
numeros_telefonicos=[]#lista de numeros telefonicos
correos_electronicos=[]#lista de correos electronicos
i_ds=[] #lista de ids

cantidad_usuarios   =  input('Ingresa la cantidad de nuevos usuarios a registrar: ')
for i_d in range(int(cantidad_usuarios)):



    #LONGITUDES DE ENTRE 5 - 50 CARACTERES

    nombre              =   input('Ingresa tu(s) nombre(s): ')
    while len(nombre) < 5 or len(nombre) > 50:
        print('Ingrese un nombre de entre 5 y 50 caracteres. ')
        nombre = input('Ingresa tu(s) nombre(s): ')



    apellidos           =   input('Ingresa tu(s) apellido(s): ')
    while len(apellidos) < 5 or len(apellidos) > 50:
        print('Ingrese un nombre de entre 5 y 50 caracteres. ')
        apellidos = input('Ingresa tu(s) apellido(s): ')



    numero_de_telefono  =   input('Ingresa tu numero de telefono: ') #Longitud de 10 caracteres
    while len(numero_de_telefono) != 10 :
        print('Ingrese un numero telefonico valido (de 10 digitos). ')
        numero_de_telefono = input('Ingrese el numero telefonico: ')



    correo_electronico  =   input('Ingresa tu correo electronico:')  #longitud de entre 5 y 50 caracteres
    while len(correo_electronico) < 5 or len(correo_electronico) > 50:
        print('Ingrese un correo electrónico de entre 5 y 50 caracteres. ')
        correo_electronico = input('Ingresa tu correo electronico ')



    print('Hola' + ' ' + nombre + ' ' + apellidos + ' en breve recibirás un correo a ' + correo_electronico)

    i_ds.append(int(i_d))
    nombres.append(nombre)
    apellidos_lista.append(apellidos)
    numeros_telefonicos.append(numero_de_telefono)
    correos_electronicos.append(correo_electronico)

for i in range(len(i_ds)):

    print('ID: '+ str(i))
    print('Nombre(s): '+ nombres[i])
    print('Apellido(s)' + apellidos_lista[i])
    print('Numero telefónico: ' + numeros_telefonicos[i])
    print('Correo electronico: ' + correos_electronicos[i])
    print(' ----------------------------------------------')

#fin

