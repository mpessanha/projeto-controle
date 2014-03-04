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
VIRTUALENV_PROJECT = join(VIRTUALENV, 'project')

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
    		return mkdir(diretorio)
    # Se diretorio existe executa bypass	
    	except OSError:
    		pass     	

def after_install(options, home_dir):
    copy(join(BOOTSTRAP, 'postactivate'), VIRTUALENV_BIN)
    with_project(join(VIRTUALENV_PROJECT, 'project_dir.txt'))
    with_venv('pip', 'install', '-r', join(ROOT, 'requirements.txt'))
    print "Done! Activate your virtualenv: source bin/activate"
