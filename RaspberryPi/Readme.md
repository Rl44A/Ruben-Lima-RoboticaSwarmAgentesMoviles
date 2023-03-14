
En el trabajo de graduación se utlizaron 2 plataformas diferentes de RaspberryPi, se utilizó 1 RaspberryPi Zero W y una RaspberryPi 3B+. Estas plataformas tienen el beneficio de actuar bajo los mismos comandos GPIO por lo que los codigos son intercambiables y se desarrollan para el uso en ambas. Sin embargo se tienen que tener en cuenta las diferencias en el poder de procesamiento y de uso de librerias externas desarrolladas para una arquitectura en específico. 

Para lograr acceder a estas plataformas se necesita guardar la imagen de un archivo en una SD y luego introducirla a la Raspi utilizada, para poder hacerlo de manera correcta se recomienda ver este video hecho por RaspberryPi  [Raspberry Pi Imager](https://www.youtube.com/watch?v=ntaXWS8Lk34 "How to use Raspberry Pi Imager "). 

Luego de esto, para poder tener una visualización de las Raspberrys dentro de nuestra computadora necesitamos un medio de conexión, se recomienda para esto utilizar Termius, ya que nos permite acceder por medio de SSH asi como tambien visualizar los documentos y pasar documentos de nuestra computadora a cualquier raspberry que este conectada. En el siguiente link se deja un video para la instalación del mismo, luego de la instalación se recomienda vincularlo con la cuenta de Github universitaria para poder obtener todos los beneficios que esta plataforma ofrece a un estudiante.  [Instalación Termius](https://www.youtube.com/watch?v=Mfk1RMeUnNA "Descargar e instalar Termius").

## Guia de Raspberry Pi

Aqui se van a dar algunas guías para el uso correcto de los agentes moviles y la RaspberryPi de estos. 

### Comandos Utiles 

Para compilar algún código desde la terminal
```sh
gcc nombre_del_archivo.c -o _ejecutable_
```

### Errores Comunes 

Si el error mostrado dice 
```sh
gcc nombre_del_archivo.c -o _ejecutable_
```
### Proceso de encendido correcto
Los leds de la raspberry
