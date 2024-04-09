Proyecto Demostración

Se trata de una pequeña página para demostrar lo básico de mis habilidades de programación.
La página funciona en base a django y utiliza plantillas de startbootstrap para la estructura HTML y CSS del sitio. Esta demostración consiste en una página de inicio en la cual se pueden seleccionar 4 demostraciones de ejercicios de Python que corresponden a bucles, llamamiento de apis y uso de aleatoriedad, siendo 4 views escritas en Python llamadas desde las páginas HTML. Además, el sitio tiene la posibilidad de registrar un usuario, pidiendo un nombre y una contraseña que se guardan en una base de datos, lo que da acceso a una página de venta de inmuebles de ejemplo en el que se puede publicar un anuncio de venta con campos para el nombre, la descripción, el precio, la imagen de la vivienda y un llamamiento de una api de mapas que permite ver donde se encuentra dicho inmueble. 

Requirements: 
django
django-ckeditor
requests
pillow

Como usar la página en caso de no tener experiencia previa con github:
1. Descargar el proyecto y descomprimirlo.
   Para descargar el proyecto, hay que dar click en el botón verde que dice code y luego donde dice download zip.
2. Descargar e instalar Python: https://www.python.org/downloads/
   A la hora de usar el instalador, asegurate de que que "Add Python to PATH" este seleccionado.
3. Abrir el símbolo de sistema e ir a la carpeta del proyecto con el comando "cd dirección de la carpeta" y presionando enter. En mi caso sería "cd C:\Users\Usuario\Downloads\ProyectoDemostracion-main":
 ![image](https://github.com/AndresHerrero1/ProyectoDemostracion/assets/123222094/848b863c-a074-4d99-8644-76794d3c573c)
4.ahora copiamos y pegamos este comando, presionamos enter:
   pip install -r requirements.txt
5. El último comando: escribimos ahora "python manage.py runserver" y luego presionamos enter nuevamente. Debería salir lo siguiente:
![image](https://github.com/AndresHerrero1/ProyectoDemostracion/assets/123222094/b22307e3-506a-436c-a1ba-4bbbf507b328)
6. Copiamos "http://127.0.0.1:8000/" y lo pegamos en nuestro buscador, presionamos enter y ya estamos en la página.




