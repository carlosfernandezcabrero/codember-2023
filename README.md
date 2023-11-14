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

+ Tiene una interfaz web hecha con Nuxt para ver los resultados, el tiempo que han tardado y el traceback del error si se produce una excepción mientras que se ejecutan. Ademas también devuelve la url del archivo de entrada usado en la solución.
+ Tiene una api en Python (Flask) que ejecuta las soluciones a los retos y obtiene los resultados, el tiempo que han tardado y el traceback del error si se produce una excepción mientras que se ejecutan. Ademas también devuelve la url del archivo de entrada usado en la solución. Pero, ¿Como puedes detectar las nuevas soluciones? Con importlib de Python, utilizándolo para importar dinámicamente el modulo que contiene la función que soluciona el reto. Ademas cada vez que se obtiene el modulo se hace un reload de el con importlib para que recargue la version cacheada.
+ Esta todo dockerizado, es decir, con un simple comando puedes levantar todo el sistema. Pero y si cambio la solución, ¿Tengo que levantar otra vez el sistema? Pues no, el docker-compose ya esta preparado para que puedas desarrollar tranquilamente en local y cada vez que guardes tu solución, al recargar la interfaz web, se recarguen los datos. ¿Pero como? Pues gracias a los volúmenes de Docker.

### Como utilizarlo

+ Primero debemos crear un archivo `.env` en el directorio `api` o renombrar el archivo `.env.example` que se encuentra en la carpeta `api` a `.env`. Despues debemos configurar la variable `REPOSITORY_LINK` en el archivo `.env` con la url hacia la carpeta donde vayamos a subir nuestras soluciones (GitHub, BitBucket, ...).
+ Tener instalado Docker Engine. [Instalar](https://docs.docker.com/engine/).
+ Ejecutar:

    ```bash
    docker compose up --build
    ```

+ Abrir la URL `http://localhost:3000`.

Ideas cogidas para el README del repositorio [https://github.com/jpaddeo/codember](https://github.com/jpaddeo/codember)
