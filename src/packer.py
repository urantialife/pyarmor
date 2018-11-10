#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
#############################################################
#                                                           #
#      Copyright @ 2018 -  Dashingsoft corp.                #
#      All rights reserved.                                 #
#                                                           #
#      pyarmor                                              #
#                                                           #
#      Version: 4.3.2 -                                     #
#                                                           #
#############################################################
#
#
#  @File: packer.py
#
#  @Author: Jondy Zhao(jondy.zhao@gmail.com)
#
#  @Create Date: 2018/11/08
#
#  @Description:
#
#   Pack obfuscated Python scripts with any of third party
#   tools: py2exe, py2app, cx_Freeze, PyInstaller
#

'''After the py2exe or cx_Freeze setup script works, this tool let you
to obfuscate all the python source scripts and package them again. The
basic usage:

    python packer.py --type py2exe /path/to/src/entry.py

It will replace all the original python scripts with obfuscated ones
in the compressed archive generated by py2exe or cx_Freeze.

'''

import logging
import os
import shutil
import subprocess
import sys
import time

from distutils.util import get_platform
from py_compile import compile as compile_file
from zipfile import PyZipFile

try:
    import argparse
except ImportError:
    # argparse is new in version 2.7
    import polyfills.argparse as argparse

try:
    from pyarmor import main as call_armor
except ImportError:
    from .pyarmor import main as call_armor

def update_library(libzip, obfdist):
    # # It's simple ,but there are duplicated .pyc files
    # with PyZipFile(libzip, 'a') as f:
    #     f.writepy(obfdist)
    filelist = []
    for root, dirs, files in os.walk(obfdist):
        filelist.extend([os.path.join(root, s) for s in files])

    with PyZipFile(libzip, 'r') as f:
        namelist = f.namelist()
        f.extractall(obfdist)

    for s in filelist:
        compile_file(s, s + 'c')

    with PyZipFile(libzip, 'w') as f:
        for name in namelist:
            f.write(os.path.join(obfdist, name), name)

def checker(func):
    def wrap(src, entry, setup, packcmd, output, libname):
        path = os.getcwd()
        os.chdir(os.path.abspath(os.path.dirname(__file__)))
        try:
            return func(src, entry, setup, packcmd, output, libname)
        finally:
            os.chdir(path)
    return wrap

@checker
def _packer(src, entry, setup, packcmd, output, libname):
    project = os.path.join('projects', 'build-for-packer-v0.1')

    options = 'init', '--type', 'app', '--src', src, '--entry', entry, project
    call_armor(options)

    filters = ('global-include *.py', 'prune build, prune dist',
               'exclude %s %s pytransform.py' % (entry, script))
    options = ('config', '--runtime-path', '',  '--disable-restrict-mode', '1',
               '--manifest', ','.join(filters), project)
    call_armor(options)

    os.chdir(project)

    options = 'build', '--no-runtime', '--output', 'dist'
    call_armor(options)

    shutil.copy(os.path.join('..', '..', 'pytransform.py'), src)
    shutil.move(os.path.join(src, entry), '%s.bak' % entry)
    shutil.move(os.path.join('dist', entry), src)

    dest = os.path.dirname(setup)
    script = os.path.basename(setup)
    p = subprocess.Popen([sys.executable, script] + packcmd, cwd=dest)
    p.wait()
    shutil.move('%s.bak' % entry, os.path.join(src, entry))
    os.remove(os.path.join(src, 'pytransform.py'))

    update_library(os.path.join(output, libname), 'dist')

    options = 'build', '--only-runtime', '--output', 'runtimes'
    call_armor(options)

    for s in os.listdir('runtimes'):
        if s == 'pytransform.py':
            continue
        shutil.copy(os.path.join('runtimes', s), output)

    os.chdir('..')
    shutil.rmtree(os.path.basename(project))

def packer(args):
    _type = 'freeze' if args.type.lower().endswith('freeze') else 'py2exe'

    if args.path is None:
        src = os.path.abspath(os.path.dirname(args.entry[0]))
        entry = os.path.basename(args.entry[0])
    else:
        src = os.path.abspath(args.path)
        entry = os.path.relpath(args.entry[0], args.path)
    setup = os.path.join(src, 'setup.py') if args.setup is None \
        else os.path.abspath(args.setup)

    if args.output is None:
        dist = os.path.join(
            'build', 'exe.%s-%s' % (get_platform(), sys.version[0:3])
        ) if _type == 'freeze' else 'dist'
        output = os.path.join(os.path.dirname(setup), dist)
    else:
        output = os.path.abspath(args.output)
    
    packcmd = ['py2exe', '--dist-dir', output] if _type == 'py2exe' \
        else ['build', '--build-exe', output]
    libname = 'library.zip' if _type == 'py2exe' else \
        'python%s%s.zip' % sys.version_info[:2]

    _packer(src, entry, setup, packcmd, output, libname)

def add_arguments(parser):
    parser.add_argument('-v', '--version', action='version', version='v0.1')

    parser.add_argument('-t', '--type', default='py2exe',
                        choices=('py2exe', 'py2app',
                                 'cx_Freeze', 'PyInstaller'))
    parser.add_argument('-p', '--path',
                        help='Base path, default is the path of entry script')
    parser.add_argument('-s', '--setup',
                        help='Setup script, default is setup.py')
    parser.add_argument('-O', '--output',
                        help='Directory to put final built distributions in' \
                        ' (default is output path of setup script)')
    parser.add_argument('entry', metavar='Entry Script', nargs=1,
                        help='Entry script')

def main(args):
    parser = argparse.ArgumentParser(
        prog='packer.py',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='Pack obfuscated scripts',
        epilog=__doc__,
    )
    add_arguments(parser)
    packer(parser.parse_args(args))

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(levelname)-8s %(message)s',
    )
    main(sys.argv[1:])
