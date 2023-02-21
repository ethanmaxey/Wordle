#!/usr/bin/python

from paver.easy import *
import paver
import os
import glob
import shutil
import sys

sys.path.append(os.path.dirname(__file__))


@task
def setup():
    sh('python -m pip install -U coverage')
    pass


@task
def test():
    sh('python -m coverage run --source src.wordle -m unittest discover -s test')
    sh('python -m coverage html')
    sh('python -m coverage report --show-missing')
    pass


@task
def clean():
    for pycfile in glob.glob("*/*/*.pyc"): os.remove(pycfile)
    for pycache in glob.glob("*/__pycache__"): os.removedirs(pycache)
    for pycache in glob.glob("./__pycache__"): shutil.rmtree(pycache)
    try:
        shutil.rmtree(os.getcwd() + "/cover")
    except:
        pass
    pass


@task
def radon():
    sh('radon cc src -a -nb')
    sh('radon cc src -a -nb > radon.report')
    if os.stat("radon.report").st_size != 0:
        raise Exception('radon found complex code')
    
@task
def ui():
    sh('python -m pip install -U pygame')
    sh('python src/wordle_gui.py')
    pass

@task
def cleanup():
    for coverage in glob.glob("./.coverage"): os.remove(coverage)
    for radon_report in glob.glob("./radon.report"): os.remove(radon_report)
    for folder in glob.glob("*/htmlcov"): os.removedirs(folder)
    for folder in glob.glob("./htmlcov"): shutil.rmtree(folder)
    pass

@task
@needs(['setup', 'clean', 'test', 'radon'])
def default():
    pass