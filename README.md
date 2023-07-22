# ¡LEER IMPORTANTE!
Aquí están los integrantes del grupo:

    - Felipe Ramos
    - Javiera Vera
    - Pablo Quinteros
    - Israel Franco

## Título del Proyecto
Sistema de Inventario de Librería "El Gran Poeta"

## Descripción del Proyecto
Proyecto nacido por la necesidad del usuario, Librería El Gran Poeta, que se basa netamente en gestionar su inventariado e información de las existencias en bodega (creación, lectura, actualización y eliminación de registros), así como el registro de movimientos de productos entre bodegas .

## Tecnologías Utilizadas
- Backend: Django - Framework web para el desarrollo del backend del sistema. Django es ampliamente conocido por su enfoque en la productividad y seguridad, lo que lo hace ideal para construir aplicaciones web complejas y escalables.

- Frontend: ReactJS - Biblioteca de JavaScript para la construcción de interfaces de usuario interactivas y eficientes. ReactJS es muy popular debido a su enfoque en el desarrollo de componentes reutilizables y su capacidad para crear aplicaciones de página única (SPA) de alto rendimiento.

- Base de Datos: MySQL - Sistema de gestión de bases de datos relacional utilizado para almacenar la información del inventario. MySQL es ampliamente utilizado y se destaca por su rendimiento y confiabilidad.

- XAMPP: XAMPP es una solución de paquete de software libre que proporciona un servidor web Apache, una base de datos MySQL y los intérpretes de PHP y Perl en un solo paquete. Es una herramienta muy útil para crear un entorno de desarrollo local para probar y desarrollar aplicaciones web antes de implementarlas en un servidor en producción.

## Comenzando: 🚀
Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

## Pre-requisitos: 📋
Que cosas necesitas para instalar el software y cómo instalarlas:

1. MySQL y XAMPP instalados en tu máquina.
2. Python y Django instalados.

## Instalación: 🔧
A continuación, se presentan los pasos para tener un entorno de desarrollo ejecutándose:

1. Clona los repositorios desde GitHub:
git clone https://github.com/felipeRAMOS2612/react-inacap.git
git clone https://github.com/felipeRAMOS2612/django-inacap.git

2. Configura el entorno virtual e instala las dependencias:
cd nombre-de-carpeta
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

3. Crea la base de datos y aplica las migraciones:
python manage.py makemigrations
python manage.py migrate

4. Ejecuta el servidor de desarrollo:
python manage.py runserver

5. Abre tu navegador y accede a `http://localhost:8000` para ver el proyecto en funcionamiento.


## Herramientas utilizadas: 🛠️

- Django - Framework web utilizado para el desarrollo del sistema.
- React JS - Utilizado para la documentación de la base de datos.
- MySQL - Base de datos utilizada para almacenar la información del inventario.
- XAMPP - Herramienta para crear el entorno de desarrollo con servidor web y base de datos.

## Autores: ✒️
- Felipe Ramos
- Javiera Vera
- Pablo Quinteros
- Israel Franco

## Contactos: 📧
- felipe.ramos34@inacapmail.cl
- javiera.vera22@inacapmail.cl
- pablo.quintero@inacapmail.cl
- israel.franco@inacapmail.cl

## Estado del Proyecto: 🚧
Proyecto en fase beta en espera de evaluación de docente.

## Notas adicionales: 📝

- Este proyecto es una primera aproximación a un sistema de inventario para la librería "El Gran Poeta". A medida que avanza el desarrollo, se pueden agregar más funcionalidades y mejoras para satisfacer las necesidades específicas del usuario así como también arreglar detalles de errores y optimización de codigo.

- Se han implementado mecanismos de autenticación y validación de usuarios para garantizar que solo los usuarios (Jefes de bodegas y bodegueros) autorizados puedan acceder y manipular la información del inventario.

- Para cualquier consulta o soporte técnico, no dudes en ponerte en contacto con el equipo de desarrollo a través de [felipe.ramos34@inacapmail.cl].

¡Gracias por utilizar nuestra app!