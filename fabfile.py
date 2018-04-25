from fabric.api import *
from contextlib import contextmanager as _contextmanager
from shutil import copyfile
from datetime import datetime

env.hosts = ['root@172.16.0.9']
env.virtualenv = '/var/djangoprojects/sitio_caae_env'
env.project = env.virtualenv + '/sitio_caae'
env.activate = "source %s/bin/activate" % (env.virtualenv,)

@_contextmanager
def virtualenv():
    with cd(env.project):
        with prefix(env.activate):
            yield

def deploy():
    local("git push production")
    with virtualenv():
        run("git pull")
        run("pip install -r requirements.txt --quiet")
        run("python manage.py migrate")
        run("yes yes | python manage.py collectstatic")

def dump():
    with virtualenv():
        output = run("python manage.py dumpdata --indent=2 --natural")
        with open('backup-latest.json', 'w') as backup:
            backup.write(output)
        copyfile('backup-latest.json', "backup_%s.json" % datetime.now().strftime('%Y-%b-%d_%H:%M:%S'))

def sync():
    dump()
    local("python manage.py reset contenttypes --noinput")
    local("python manage.py loaddata backup-latest.json")


