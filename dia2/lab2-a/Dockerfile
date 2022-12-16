# Escogemos la version de ubuntu.
ARG VERSION=18.04

# Declaramos la imagen base.
FROM ubuntu:${VERSION}

# Instalamos las librerias necesarias
RUN apt-get update && apt-get install -y curl nginx \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copiamos el proyecto
RUN mkdir /test-dir
ENV SHELL /bin/bash

# Exponemos el puerto 80 del contenedor
EXPOSE 80

# Iniciamos el servidor nginx, en runtime
CMD ["nginx", "-g", "daemon off;"]
