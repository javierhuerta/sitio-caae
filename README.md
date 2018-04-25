# sitio-caae
Sitio web Centro de apoyo academico al estudiante

## Software necesario 

* Python 2.7
* pip 
* virtualenv

pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Copiar archivo dev.py a local_settings.py en carpeta settings


## Para actualizar base de datos
1. python manage.py migrate
2. python manage.py shell
from django.contrib.contenttypes.models import ContentType

ContentType.objects.all().delete()

3. python manage.py loaddata backup.json
