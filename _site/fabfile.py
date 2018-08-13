
from fabric.api import local, abort, run, lcd, cd, settings, sudo, env

env.hosts = [
    'sparkpl.ug',

    ]
def deploy():
    with cd("/var/www/prod/sparkpl.ug"):
        sudo('git pull origin master', user='www-data')
        sudo('jekyll /var/www/prod/sparkpl.ug /var/www/prod/static_files/sparkpl.ug',user='www-data')
