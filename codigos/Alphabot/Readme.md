<h1 align="center"> Esta es la guia de uso de los codigos creados para la utilización en el Alphabot </h1> 

Para el alphabot se realizo un pequeño truco ya que no se contaba con mucho tiempo para hacer el traslado de los programas, y verificar las condiciones de carrera mientras corría sus 
propios programas. En este caso como servidor se corrió todo en una raspberry aparte, y luego se le mandaba el movimiento al alphabot. Para poder controlar estas plataformas se utilizo 
Termius. 

1. Primero vamos a abrir los siguientes archivos en la computadora que esta actuando como servidor 1, este servidor recibe las coordenadas del sistema de captura de movimiento
ROBOTAT. 
```
- Robotat_Connect_Alpha.py
```
Este programa tiene vinculado  **AlphabotRaspi.py** , este no es necesario abrirlo en la implementación pero si, si se necesita cambiar el puerto de salida o de entrada de información. 


2. Luego dentro de la raspberry, vamos a abrir en python

```
ServidorSocket_Alpha.py
```
Este programa es el que recibe las coordenadas que manda el servidor 1, para luego enviarlas al principal **sokkt.py**. Este es el que las transforma y las envía a su siguiente destino, luego este siguiente destino las regresa
y este mismo programa las vuelve a transformar y las envía al programa de movimiento. Podemos decir que este es la base del proceso de traslado de información. Este programa esta viculado  con **Movimiento1.py** que es en donde se ejecutan las instrucciones para que el robot se pueda mover.
Este programa es la ultima version del movimiento para alphabot ya que utiliza colores. Este **Movimiento1.py** funciona asi mismo como servidor ya que envía los valores al alphabot. 


3. Luego abrimos el programa en C  
```
sot.c 

```
Este es el que ejecuta el algoritmo de robotica de enjambre PSO que recibe las coordenadas actuales y provee unas coordenadas futuras las cuales son enviadas de regreso hacia **sokkt.py** para que este pueda enviarlas al movimiento y que el Bytebot pueda ejecutarlas y hacer el movimiento pedido.

Dentro de este repositorio hace falta el codigo del servidor creado especialmente para esta prueba, pero se encuentra en el repositorio de Luis Nij. 

<h2 align="center"> Orden de apertura </h1> 

Estos codigos estan unidos en cierta manera de apertura, es decir que si no se abren en este orden el puerto no detecta información. Puede pasar que aveces el puerto por el que se esta enviando la información deje de 
responder y por lo tanto hay que cambiar de puerto, esto no es motivo de alarma. 

El orden para abrir los programas principales sería este 
1. Abrimos el servidor en Alphabot
   - Abrimos sot.c
     - Abrimos ServidorSocket_Alpha.py y sokkt.py y esperamos el mensaje de conexión entre la raspberry y el Alphabot. 
       -  Abrimos Robotat_Connect_Alpha.py 
     
Tomar en cuenta que para este y todos los programas el Robotat debe estar enviando información, ya que sino, no se podra conectar con el receptor y todo su codigo va a dejar de funcionar ya que la información esperada 
no va a aparecer. 

