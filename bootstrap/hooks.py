# coding: utf-8
from os.path import join, dirname, pardir, abspath
from os import mkdir
from shutil import copy
import subprocess


BOOTSTRAP = abspath(dirname(__file__))
ROOT = abspath(join(BOOTSTRAP, pardir))

# Path where venv will be created. It's imported by bootstrapX.Y.py
VIRTUALENV = join(BOOTSTRAP, pardir)
VIRTUALENV_BIN = join(VIRTUALENV, 'bin')
VIRTUALENV_PROJECT = join(ROOT, 'project')

WITH_VENV = join(BOOTSTRAP, 'with_venv.sh')


def with_venv(*args):
    """
    Runs the given command inside virtualenv.
    """
    cmd = list(args)
    cmd.insert(0, WITH_VENV)
    return subprocess.call(cmd)

def with_project(*args):
    """
    Runs the given command inside virtualenv.
    """
    diretorios = list(args)
    for diretorio in diretorios:
        try:
            print 'Efetuando criacao do diretorio %s' % (diretorio)
            mkdir(diretorio)
        # Se diretorio existe executa bypass	
        except OSError:
            print 'Diretorio %s ja existe' % (diretorio)
            pass
    return    

def after_install(options, home_dir):
    # Cria os diretorios de apoio do projeto
    with_project(
        (join('mkdir', VIRTUALENV_PROJECT, 'media')),
        (join('mkdir', VIRTUALENV_PROJECT, 'sitestatic')),
        (join('mkdir', VIRTUALENV_PROJECT, 'static')),
        (join('mkdir', VIRTUALENV_PROJECT, 'templates')),    
    )
    copy(join(BOOTSTRAP, 'postactivate'), VIRTUALENV_BIN)
    with_venv('pip', 'install', '-r', join(ROOT, 'requirements.txt'))
    print "Done! Activate your virtualenv: source bin/activate"
