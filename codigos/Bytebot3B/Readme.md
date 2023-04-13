
<h1 align="center"> Esta es la guia de uso de los codigos creados para la utilización en el Bytebot 3B </h1> 


1. Primero vamos a abrir los siguientes archivos en la computadora que esta actuando como servidor 1, este servidor recibe las coordenadas del sistema de captura de movimiento
ROBOTAT. 
```
- Robotat_Connect3B.py
```
Este programa tiene vinculados otros 2 codigos que son **SoktCPY.py** y **sokt.py**, estos no son necesario abrirlos en la implementación pero si, si se necesita cambiar el puerto de salida o de entrada de información. 
El programa del Robotat_Connect3B tambien puede ser utilizado dentro de la misma raspberry ya que puede recibir las coordenadas del robotar, sin embargo lo utilice en computadoras separadas para asi agilizar la 
recepción de información y no cargar tanto a la raspberry. 

2. Luego dentro de la raspberry, vamos a abrir en python 

```
ServerCliente.py
```
Este programa es el que recibe las coordenadas que manda el servidor 1, para luego enviarlas al principal **Client.py**. Este es el que las transforma y las envía a su siguiente destino, luego este siguiente destino las regresa
y este mismo programa las vuelve a transformar y las envía al programa de movimiento. Podemos decir que este es la base del proceso de traslado de información. Este programa esta viculado con **Konectzmq.py** que es en
donde se hacen las conexiones con el algoritmo de enjambre y con **Movimiento.py** que es en donde se ejecutan las instrucciones para que el robot se pueda mover. 


3. Luego abrimos el programa en C  
```
ServidorzmqPSO.c

```
Este es el que ejecuta el algoritmo de robotica de enjambre PSO que recibe las coordenadas actuales y provee unas coordenadas futuras las cuales son enviadas de regreso hacia **Client.py** para que este pueda enviarlas al movimiento y que el Bytebot3B pueda ejecutarlas y hacer el movimiento pedido. 
<h2 align="center"> Orden de apertura </h1> 

Estos codigos estan unidos en cierta manera de apertura, es decir que si no se abren en este orden el puerto no detecta información. Puede pasar que aveces el puerto por el que se esta enviando la información deje de 
responder y por lo tanto hay que cambiar de puerto, esto no es motivo de alarma. 

El orden para abrir los programas principales sería este 
1. Abrimos ServidorzmqPSO.c
   - Abrimos ServerCliente.py y esperamos el mensaje de conexión entre ServidorzmqPSO.c  y este. 
     - Abrimos Robotat_Connect3B.py 
     
Tomar en cuenta que para este y todos los programas el Robotat debe estar enviando información, ya que sino, no se podra conectar con el receptor y todo su codigo va a dejar de funcionar ya que la información esperada 
no va a aparecer. 

Dentro de estas carpetas tambien se incluyen algunas versiones diferentes de ciertos programas para que se puedan entender las funciones y los cambios hechos para poder mejorarlas en un futuro. 
