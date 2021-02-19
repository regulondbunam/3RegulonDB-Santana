# [Software name]

# Description

Este modulo se encargara de extraer archivos de diferentes formatos pueden ser csv,txt o xlsx, para poder tomar su data y metadata, una vez tomando esos datos se encargara de tranasformalos y validarlos para corroborar que sean datos correctos mediante JSONSchemas, una vez validados se crea un JSON con su data y metadata corrrespondientes.

# Motivation

los datos procesados se convirten en un JSON debido a que esta informacion se almacenara posteriormente en una base de datos documental que se encargara de alojar los todos los datos, la base se llama DATOS HT


# System requirements

[If the software does make high demand on particular resources, then this should be clearly advertised and explained.]

# Install 

sudo dnf install python3 -y



# Quick start
El siguiente comando se encargara de correr el modulo
python3 ht_validate_transform -i <temlatesDir> -t geneExpressionContrast -out  <validJsonFile> -o <InvalidJsonFile>  -js_metadata <JSONSchemaMetadataFile>  -js_data <JSONSchemaDataFile> -log <logFile>

# Project website 

Poder visualizar los datos como tal en una plataforma web no se podr adebido a que el proyecto aun sigue en desarrallo pero al terminar se podran visualizar en la siguiente pagina web:
http://regulondb.ccg.unam.mx/gene?organism=ECK12&term=ECK120000050&format=jsp&type=gene

# License
MIT

# Support contact information
regusoft@ccg.unam.mx

# Software quality checklist

El codigo se encuentra en su version 1.0 y podria tener mejoras con forme sea la necesidad del proyecto o de los datos

**Accessibility**

- [ ] Unique DOI [identifier](http://....) (Please update identifier and link)
- [ ] Version control system

**Documentation**

- [ ] README file

**Learnability**

- [ ] Quick start

**Buildability**

- [ ] INSTALL file

**Identity**

- [ ] Website

**Copyright & Licensing**

- [ ] LICENSE file

**Portability**

- [ ] Multiple platforms
- [ ] Browsers

**Supportability**

- [ ] E-mail address
- [ ] Issue tracker
- [ ] Slack
- [ ] Gitter

**Analysability**

- [ ] Source code structured
- [ ] Sensible names
- [ ] Coding standards - [style guides](http://google.github.io/styleguide/)

**Changeability**

- [ ] CONTRIBUTING file
- [ ] Code of Conduct file
- [ ] Code changes, and their authorship, publicly visible

**Reusability**

- [ ] Source code set up in a modular fashion

**Security & Privacy**

- [ ] Passwords must never be stored in unhashed form


