from fabric.api import run, sudo, local, cd, env

env.hosts = ['orlando.thraxil.org']
env.user = 'anders'

def restart_gunicorn():
    sudo("restart auratus", shell=False)

def prepare_deploy():
    local("make test")

def deploy():
    code_dir = "/var/www/auratus/auratus"
    with cd(code_dir):
        run("git pull origin master")
        run("make migrate")
        run("make collectstatic")
        run("make compress")
    restart_gunicorn()
