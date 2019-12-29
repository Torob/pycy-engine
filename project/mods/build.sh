#!/bin/bash

function build_module {
    echo '[building] '$1
    cd $1 && echo '[moved] '`pwd`
    python setup.py build_ext --inplace
    mv *.so ..
    echo '[moving back] '`pwd` && cd ..
}

mods=$(ls -d */ | cut -f1 -d'/')
for mod in $mods; do build_module $mod ; done