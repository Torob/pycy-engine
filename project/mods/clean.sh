#!/bin/bash

function yes_or_no {
    while true; do
        read -p "$* [y/n]: " yn
        case $yn in
            [Yy]*) return 0  ;;  
            [Nn]*) echo "Aborted" ; return  1 ;;
        esac
    done
}

function clean_up {
    rm -rf *.so && echo '[success]'
}

if [[ "$1" == "--no-prompt" ]]; then
    clean_up
else
    yes_or_no '[removing all so modules] ' && clean_up
fi