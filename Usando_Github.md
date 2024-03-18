# Uso de github

***
- [Uso de github](#uso-de-github)
  - [Crear repositorio Github](#crear-repositorio-github)
  - [Configuror sesión](#configuror-sesión)
  - [Conectar remoto](#conectar-remoto)
  - [Hago el add .](#hago-el-add-)
  - [Hago el commit](#hago-el-commit)
  - [Setear branch Main](#setear-branch-main)
  - [Hago el push](#hago-el-push)

## Crear repositorio Github

***
Luego de haber creado la cuenta, descargar e instalar git, se procede a logguear y crear un repositorio.
Una vez nombrado el repositoio se abre la terminal en la carpeta donde se tiene el proyecto a subir.

## Configuror sesión

***
En la terminal se utiliza el comando `git init` 
Se procede a Identificarse en git:
```
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@example.com"
```

## Conectar remoto

***
Se realiza desde la terminal la conexcion al repositorio en remoto:
```
git remote add origin https://github.com/"nombre_usuario"/"nombre_proyecto.git"
```
Esto lo entrega el mismo github

## Hago el add .

***
```
git add .
git status
```

## Hago el commit

***
`git commit -m "Mensaje del commit 1"`

## Setear branch Main

`git branch -M main`

## Hago el push

***
```
git push -u origin main
git push
```
