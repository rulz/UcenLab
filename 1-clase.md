UcenLab
=========
Pasos a seguir para instalar y crear Django

***1. Instalar [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/en/latest/)***
(virtualenvwrapper: es para crear un entorno (una carpeta) del proyecto y de esa maneja instalar los requerimientos de cada proyecto)
```
sudo pip install virtualenvwrapper
```
luego configurar carpeta del viertualenvs
en
```
mac:
vim .bash_profile

linux:
vim .profile
```
y pegas el código
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/<directorio>
source /usr/local/bin/virtualenvwrapper.sh
```
```
source .bash_profile
mkvirtualenv nombre_del_proyecto
workon nombre_del_proyecto
```
salir del entorno
```
deactivate
```

***2. Instalar Django***
```
pip install django
```
***3. Crear un proyecto con Django***
```
django-admin startproject nombre_del_proyecto
```
***4. Crear una aplicación (módulo) con Django***
```
django-admin startapp nombre_de_la_app
```
***5. Modelar en la aplicación creada***

tiene que ir al archivo
```
nombre_de_la_app/models.py
```
***6. Mostrar las entidades modeladas en el admin de django***

tiene que ir al archivo
```
nombre_de_la_app/admin.py
```
tiene que importar el modelo creado
```
from . import models
o
from .models import Entidad
```
luego para mostrar la entidad en el admin es
```
@admin.register(models.Entidad)
class EntidadAdmin(admin.ModelAdmin):
    pass
o

@admin.register(Entidad)
class EntidadAdmin(admin.ModelAdmin):
    pass
```
**7. Crear un registro de la entidad creada***

tiene que ir a la url
```
127.0.0.1:8000/admin/
```
hacer click en la entidad creada

***8. Cree un registro de esa entidad***
***9. Cree otra entidad con una llave foranea de la entidad anterior***








