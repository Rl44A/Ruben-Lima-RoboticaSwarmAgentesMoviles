# Implementación y validación de algoritmos de robótica de enjambre en plataformas móviles en la nueva mesa de pruebas del laboratorio de robótica de la UVG

En este proyecto se realiza la validación del PSO, un algoritmo de robotica de enjambre desarrollado en un trabajo de graduación anterior sobre plataformas moviles para así poder utilizarlas como partículas en simulaciónes. Las plataformas utilizadas son el Bytebot, desarrollado por Julio en otro trabajo de graduación y el Bytebot3B, desarrollado por mi persona utilizando el Bytebot de base. 

 ![PS3O](https://user-images.githubusercontent.com/60798417/204691414-226293f9-3b90-4dd7-a137-5123ce1b5455.gif)

# Indice
1. [Pre-rrequisitos](#Pre-rrequisitos)
2. [codigos](#codigos)
3. [Documentos](#Documentos)
4. [RaspberryPi](#RaspberryPi)
5. [Piezas](#Piezas)
6. [Construido](#Construido)


### Pre-rrequisitos📋

Para poder correr los programas se necesita instalar algunos componentes 

Libreria ZMQ en la RaspberryPi

```
sudo apt-get install libtool pkg-config build-essential autoconf automake
```
Instalamos libsodium
```
wget https://github.com/jedisct1/libsodium/releases/download/1.0.3/libsodium-1.0.3.tar.gz
tar -zxvf libsodium-1.0.3.tar.gz
cd libsodium-1.0.3/
./configure
make
sudo make install
```
Instalamos ZMQ
```
wget https://github.com/zeromq/libzmq/releases/download/v4.3.2/zeromq-4.3.2.tar.gz
tar -zxvf zeromq-4.3.2.tar.gz
cd zeromq-4.3.2/
./configure
make
sudo make install
sudo ldconfig
```
Luego para Python3 tenemos que instalarlo 
```
sudo apt-get install python3-dev python3-pip
sudo pip3 install pyzmq
```

### Codigos🔧

En esta carpeta se encuentran los codigos utilizados por cada robot, dentro de cada carpeta hay un Readme con la explicación del funcionamiento de los mismos. Esta divido en 2 carpetas con el nombre de cada robot y luego con los lenguajes utilizados, Python, C, Matlab. 

### Documentos📋
Dentro de esta carpeta están los trabajos escritos desarrollado en el transcurso del periodo de investigación y realización de este trabajo de graduación. 

### RaspberryPi⚙️

En esta carpeta se da una explicación basica de lo necesario para poder iniciar la raspberry y lograr comunicarse con ella, una guía basica de consejos y errores comúnes. 

### Piezas🔩

En esta carpeta se detallan las piezas utilizadas para el Bytebot3B


## Construido🛠️

Aquí se hace un resumen de las herramientas utilizadas en todo el proyecto, estas pueden variar a disposición de las siguientes actualizaciones del proyecto. 

* [Spyder/Anaconda ](https://www.anaconda.com) - IDE utilizado en windows
* [Termius](https://termius.com) - Manejador de comunicaciónes
* [Optitrack](https://optitrack.com) - Sistema de captura de movimiento
* [ZMQ](https://zeromq.org) - Framework
* 
* 

