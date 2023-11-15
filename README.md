<div align="center">

![Codember](./images/codember.webp)

# [codember](https://codember.dev)

Resolución de los retos del juego [codember](https://codember.dev/) creado por [@midudev](https://github.com/midudev/) para la comunidad.

</div>

## Tabla de retos

| Challenge |                                   Solución                                   |
| :-------: | :--------------------------------------------------------------------------: |
|    #01    | [Python](reto1/main.py)                                                      |
|    #02    | [Python](reto2/main.py)                                                      |

<hr/>

## ¿Pensabas que solo tenia esto?

Para hacer algo especial con este repositorio he hecho lo siguiente:

+ Tiene una interfaz web hecha con Nuxt para ver los resultados, los nombres de los reto, los tiempos de ejecución, el código fuente, la url del archivo con los datos de entrada y las trazas de error, si se produce una excepción, de las soluciones. Ademas permite volver a ejecutar las soluciones con tan solo pulsar un botón.
+ Tiene una api en Python (Flask) que ejecuta las soluciones a los retos y obtiene los resultados, los nombres de los reto, los tiempos de ejecución, el código fuente, la url del archivo con los datos de entrada y las trazas de error, si se produce una excepción, de las soluciones. Pero, ¿Como puedes detectar las nuevas soluciones? Con importlib de Python, utilizándolo para importar dinámicamente el modulo que contiene la función que soluciona el reto. Ademas cada vez que se obtiene el modulo se hace un reload de el con importlib para invalidar la versión cacheada.
+ Esta todo dockerizado, es decir, con un simple comando puedes levantar todo el sistema. Pero y si cambio la solución, ¿Tengo que levantar otra vez el sistema? Pues no, el docker-compose ya esta preparado para que puedas desarrollar tranquilamente en local y cada vez que guardes tu solución, al recargar la interfaz web, se recarguen los datos. ¿Pero como? Pues gracias a los volúmenes de Docker.

### Uso

#### Requisitos

+ Tener instalado Docker Engine. [Instalar](https://docs.docker.com/engine/).

#### Arrancar

+ Ejecutar:

    ```bash
    docker compose up --build
    ```

+ Abrir la URL `http://localhost:3000`.

#### Desarrollar soluciones a los retos

Para crear una solución apara un reto debemos crear una carpeta con el nombre del reto en la carpeta `api` dentro de la carpeta `src`.

Dentro de la carpeta con el nombre del reto debemos crear un archivo `main.py`. Dentro de este debemos crear una variable en la raíz del script con la url del archivo con los datos de entrada llamada `input_url`. También dentro de el debemos crear una función con el nombre `solution` que deberá devolver la solución del reto. Esta función deberá recibir un parámetro llamado `input`. Este parámetro contendrá los datos de entrada devueltos por la url definida en el mismo archivo en la variable llamada `input_url`. Dentro de la carpeta con el nombre del reto debemos crear como mínimo este archivo pero podemos crear cualquier otro archivo que queramos.

### Contribuir

+ Hacer fork del proyecto.
+ Crear rama con el nombre del cambio.
+ Hacer pull request con el cambio desde la rama que hemos creado a la rama main de este repositorio.

### Notas

Ideas cogidas para el README del repositorio [https://github.com/jpaddeo/codember](https://github.com/jpaddeo/codember)
