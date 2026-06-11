# Repositorio del robot Rhino

## Consideraciones para la gestión del repositorio
* Utilizar nombre de directorios con estilo `underscore` (tales como `src`, `doc`, `hardware`).
* Evitar usar caracteres especiales como tíldes y eñes en nombres de directorios y archivos.
* Tener en cuenta los siguientes criterio para los commits: [https://chris.beams.io/posts/git-commit/](https://chris.beams.io/posts/git-commit/).
* Edición de Markdown: [https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Contenido
Este repositorio contiene lo siguiente (agregar enlaces en cada ítem):
* 
### Descripción

El **Rhino XR4** es un robot manipulador industrial tipo brazo robótico, popular en entornos educativos y de investigación durante las décadas de 1980 y 1990. Este robot es conocido por su versatilidad y facilidad de uso, lo que lo convirtió en una herramienta ideal para enseñar conceptos de robótica y control automático.

### Características Generales

- **Estructura Mecánica**: El Rhino XR4 cuenta con un brazo robótico con múltiples grados de libertad, diseñado para simular el movimiento de un brazo humano.

- **Componentes Principales**:
  - **Base giratoria**: Permite movimientos en el plano horizontal.
  - **Articulaciones**: Simulan los movimientos del hombro, codo y muñeca.
  - **Pinza o efector final**: Herramienta utilizada para agarrar objetos.
  - **Motores paso a paso**: Controlan las articulaciones para movimientos precisos.


### Funcionamiento

El robot se programa para realizar tareas como ensamblaje, manipulación de objetos o movimientos repetitivos. La programación incluye la definición de trayectorias y la ejecución automática de comandos para mover el brazo a posiciones predefinidas.

### Aplicaciones

Aunque no es un robot industrial de alta capacidad, el Rhino XR4 ha sido ampliamente utilizado en universidades, centros de investigación y laboratorios educativos para:

- Enseñar robótica y control automático.
- Experimentar con cinemática y dinámica de robots.
- Desarrollar proyectos educativos de programación y control.


### Controlador Mark IV

Para operar el Rhino XR-4, se utiliza el **controlador Mark IV** desarrollado por Rhino Robotics, Ltd. Este controlador cuenta con un sistema abierto adecuado tanto para la enseñanza como para la experimentación en robótica.

#### Características del Controlador Mark IV

- **Integración Completa**: El Mark IV integra fuentes de alimentación, comunicación, lógica de microprocesador, compatibilidad con dispositivos de programación, capacidad de entrada/salida (E/S) y un lenguaje de software. Este controlador es compatible con cualquier robot de la serie Rhino XR o SCARA.

- **Control PID Avanzado**: Utiliza algoritmos de control proporcional, integrativo y derivativo (PID) para gestionar la velocidad máxima de hasta ocho motores codificados, brindando un control preciso sobre el robot.

- **Capacidades de Entrada/Salida**: 
  - Ocho pares de líneas de entrada.
  - Ocho interruptores de entrada.
  - Ocho pares de líneas de salida.
  Todas las líneas de E/S están limitadas en corriente para garantizar un funcionamiento seguro, funcionando de manera similar a las líneas de entrada de grado industrial.

- **Fuente de Energía Versátil**: La energía requerida por las líneas de E/S puede ser proporcionada directamente por el controlador o por un dispositivo de entrada externo.

- **Dispositivo de Programación**: Incluye un dispositivo de programación con su propio microprocesador que se comunica con el host a través de RS-232C. Este dispositivo admite dos líneas alfanuméricas de 16 caracteres cada una, proporcionando un sistema de interacción totalmente funcional.

El controlador Mark IV ofrece una solución robusta para controlar y programar el Rhino XR-4, ideal para entornos educativos y de investigación.

### Control del Rhino XR4

Para controlar los brazos del robot, es importante conocer cómo se realizan los movimientos de cada motor mediante el controlador Mark IV:

- **Botón A**: Cierra o abre la pinza.
- **Botón B**: Rotación de la pinza. (360 grados)
- **Botón C**: Rotación de la muñeca (250 grados).
- **Botón D**: Rotación de la muñeca (180 grados).
- **Botón E**: Rotación del hombro (150 grados).
- **Botón F**: Rotación del cuerpo (350 grados).

Con esta información, se puede seleccionar el botón necesario y ajustar el movimiento correspondiente.


#### Configuración de un Nuevo Punto de Inicio

- Con el botón **Set Soft Home** puedes guardar un nuevo punto de partida ("home").
- Utiliza el botón **Go to Soft Home** para mover el robot a ese punto.

Este proceso permite tener un control preciso sobre el robot Rhino XR4 y facilitar la programación de movimientos y rutinas.


Luego de conocer movimientos y aprender comandos para poder mover el Brazo robótico, se procedio a la instalación de Ubuntu (ya que no se tenia), para la posterior instalación de ROS2.

#### Configuración para 0 absoluto

-Estando en el menu de inicio presionar el boton **Config** luego de ver en el display **go to the hard mode** presionar enter 
-Esto pondra al rhino en su posicion 0

## Instalación de Ubuntu 24.04

Para utilizar ROS2 Humble con el robot Rhino XR4, es recomendable instalar Ubuntu 24.04, ya que este sistema operativo es compatible con la versión Humble de ROS2. A continuación, se detalla el proceso de instalación de Ubuntu y ROS2.
Requisitos previos

    Computadora compatible: Asegúrate de que tu computadora cumpla con los requisitos mínimos de hardware para instalar Ubuntu 24.04.
    USB de arranque: Necesitarás un pendrive con al menos 4 GB de capacidad para crear un medio de instalación.

Paso 1: Crear un USB de arranque

    Descargar la imagen ISO de Ubuntu 24.04 desde el sitio oficial: https://ubuntu.com/download.
    Crear el USB de arranque usando una herramienta como Rufus (en Windows) o Etcher (en Linux/Mac).
        Selecciona la imagen ISO descargada y el dispositivo USB en el programa, luego sigue las instrucciones para crear el medio de instalación.

Paso 2: Instalar Ubuntu 24.04

    Reiniciar la computadora con el USB de arranque conectado.
    Accede al menú de arranque presionando la tecla correspondiente (usualmente F12, ESC o DEL).
    Selecciona la opción para arrancar desde el USB.
    Cuando se cargue la pantalla de instalación de Ubuntu, selecciona:
        Instalar Ubuntu.
        Idioma y zona horaria correctos.
        Particiona tu disco o elige una instalación limpia según lo necesites.
    Completa los pasos de instalación y, al finalizar, reinicia el sistema.

## Instalación de ROS2 Humble en Ubuntu 24.04

Una vez instalado Ubuntu 24.04, puedes proceder con la instalación de ROS2 Humble, en este caso se siguio los pasos de https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html.


## Que  es ROS2?

¿Qué es ROS?

ROS (Robot Operating System) es un conjunto de bibliotecas y herramientas que ayudan a los desarrolladores a construir aplicaciones robóticas complejas. A pesar de su nombre, ROS no es un sistema operativo en sí, sino una capa de software que permite la comunicación y coordinación entre los diferentes componentes de un sistema robótico.

### Conceptos claves

#### Nodos 

Los nodos son procesos individuales que ejecutan código en un sistema robótico. En un robot, puede haber varios nodos, y cada uno de ellos tiene una función específica, como controlar un motor, leer sensores o procesar imágenes.

### Publicar y Suscribir

ROS se basa en un modelo de comunicación publicador-suscriptor para facilitar la transferencia de datos entre nodos.

    Publicar: Un nodo puede publicar información en un "tema" (topic). Los temas son canales de comunicación donde los nodos publican datos.
    Suscribir: Otro nodo puede suscribirse a ese tema y recibir la información que se está publicando.


### Temas (Topics)

Los temas son canales de comunicación por donde los nodos intercambian información. Cuando un nodo publica un mensaje, lo hace en un tema, y todos los nodos que están suscritos a ese tema recibirán ese mensaje.


### Mensajes

Los mensajes son las estructuras de datos que los nodos intercambian. Pueden contener información de diferentes tipos, como números enteros, flotantes, cadenas de texto o incluso datos más complejos, como imágenes o coordenadas 3D.

### Paquetes (Packages)

En ROS, el código se organiza en paquetes, que contienen nodos, archivos de configuración y otros recursos necesarios para que el sistema robótico funcione. Un paquete puede contener varios nodos que trabajan juntos para realizar tareas específicas.



## Comunicación serie Rhino con python

El primer paso para establecer la comunicación serie con el robot Rhino XR4 fue consultar el manual del robot, con el fin de comprender la estructura de la trama de datos necesaria para una comunicación correcta.

Los parámetros requeridos para esta comunicación son los siguientes:

    Velocidad de transmisión (baudrate): 9600 baudios.
    Tamaño de byte (bytesize): 7 bits.
    Paridad: Paridad impar (odd parity).
    Bits de parada (stopbits): 2 bits.

Estos valores aseguran que la información se transmita de manera correcta entre el controlador del robot y la computadora, cumpliendo con los estándares necesarios para una comunicación eficiente en un entorno serie RS232.
Luego se realizó el primer script de python para las primeras pruebas de funcionamiento, para este primer script se tuvo en cuenta los comandos mostrados en la siguiente tabla para las acciones que se quiere realizar, para ver más comandos leer el Manual.

## Comandos para el control del Rhino XR4

| **Comando** | **Significado**                                      | **Comentarios**                                                                 |
|-------------|------------------------------------------------------|---------------------------------------------------------------------------------|
| MC          | Inicia el movimiento coordinado de todos los motores |                                                                                 |
| MI          | Inicia el movimiento independiente de todos los motores |                                                                               |
| PD,m,d      | Establece la posición de destino absoluta del motor m |m=['B','C','D','E','F']       ;         (-32700 < d < 32700)
| VG,d        | Establece la velocidad del sistema                   | Poco frecuente, pero necesario para la configuración inicial                    |
| VS,m,d      | Establece la velocidad del motor m                   | Poco frecuente, pero necesario para la configuración inicial                    |
| TH          | Entrega el control al PC host (entra en modo host)   |                                                                                 |
| TX          | Entrega el control a la paleta de programación (entra en modo paleta de programación) |                                                 |
| GC          |  Cierra la pinza                                        |                                                                                |
| GO          |  Abre la pinza                                        |                                                                                |


La primera comunicación serial se realizo con el siguiente script de python [Primer Script](scr/python/SerTest.py).

Luego de tener la base para la comunicacion, se realizo el siguiente script en python [Segundo Script](scr/python/joint.py) que permite publicar, utilizando librerias de ROS, la informacion de cada motor del robot RHINO en el topico /Joint_state.


## Modelado con URDF

URDF (Unified Robot Description Format) es un formato basado en XML utilizado para describir la estructura y los componentes de un robot de manera precisa y detallada. Fue diseñado para la comunidad de desarrollo de robots con ROS (Robot Operating System) y se ha convertido en un estándar para representar modelos de robots. URDF permite especificar las partes físicas del robot, como los enlaces rígidos (links), las articulaciones (joints) y los sensores. También permite definir propiedades adicionales como materiales, geometría y cinemática.

El uso de URDF es fundamental en simulaciones de robots en entornos como Gazebo o RViz, ya que proporciona una representación precisa de la geometría, la dinámica y las restricciones de un robot.

## Principales Componentes de URDF

-*Links:* Son las partes físicas del robot, como el cuerpo, brazos o ruedas. Cada link se describe con propiedades geométricas y visuales.

-*Joints:* Conectan los links y permiten el movimiento relativo entre ellos. Los tipos comunes de juntas son revolute (rotacional), prismatic (lineal), fixed (fija) y continuous (rotacional ilimitado).

-*Sensores y Actuadores:* Se pueden incluir en el modelo URDF para definir dispositivos como cámaras, LIDAR y motores.

-*Geometría y Colisiones:* Definen la forma física de las piezas del robot y las interacciones entre ellas.

## Porque utilizar URDF

1. **Simulación**: Los modelos URDF se pueden utilizar en simuladores como Gazebo y RViz para visualizar y probar el comportamiento del robot.
2. **Planificación de Movimiento**: Al describir la cinemática del robot, URDF ayuda a generar trayectorias y controlar los movimientos.
3. **Compatibilidad con ROS**: URDF está completamente integrado con ROS, lo que facilita la interoperabilidad entre componentes de software y hardware.
    
## Instalacion

Se recomienda utilizar Ubuntu, ya que es el sistema nativo para el que está desarrollado ROS2 y, por ende, es el más fácil de instalar mediante "deb packages" en la página oficial de ROS2 (https://www.ros.org/). La última versión en la que probamos que funciona es la Jazzy Jalisco.

#### Una vez instalado ROS2:

1. **Configuracion de Entorno**
    ```bash
    sudo apt update && sudo apt upgrade
    ```
    **Configurar la ruta:** en la misma página donde está la guía de instalación de la distribución de ROS2, en el panel de la izquierda, entrar en Tutorials --> Beginner: CLI tools --> Configuring environment.

    ```bash
    sudo apt update
    ```


2. **Instlaciones necesarias**

    ```bash
    sudo apt install ros-<distro>-joint-state-publisher
    sudo apt install ros-<distro>-joint-state-publisher-gui
    sudo apt install ros-<distro>-xacro
    ```

## Visualizacion en rviz
1. **Clonar directorio rhino:** 
   Dentro, estarán los directorios python y src.

2. **Construir utilizando colcon**
   Ubicado dentro del directorio rhino, ejecutar en la terminal:
   ```bash
   colcon build --symlink-install
   ```
   Una vez construido, en el directorio rhino aparecerán los directorios _install_, _log_ y _build_.

3. **Ejecutar rviz**
   Primero se debe configurar el entorno, posicionado sobre el directorio _rinho_:
   ```bash
   . install/setup.bash
   ```
   Luego, teniendo al controlador del rhino conectado por puerto serie, y ubicado en el directorio _rinho_:
   ```bash
   ros2 launch rhino_description test_rhino_rviz.launch.py
   ```
