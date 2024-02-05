#!/bin/bash
# The way to tidy environmet.

PROJECT_ROOT="$(pwd)"

IP="127.0.0.1"
PORT=8000

# git関連
function git-commit() {
    git add "$PROJECT_ROOT"
    git commit
}

# django関連
function open-browser() {
    # WSL2 only                           # ubuntu 22.04 LTS
    explorer.exe http://"$IP":"$PORT"/ # || xdg-open http://"$IP":"$PORT"/
}

function run() {
    open-browser
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function admin() {
    explorer.exe http://"$IP":"$PORT"/admin/
    python3 "$PROJECT_ROOT"/manage.py runserver
}

function dj-test() {
    python3 "$PROJECT_ROOT"/manage.py test testapp
}

function migrate() {
    python3 "$PROJECT_ROOT"/manage.py makemigrations
    python3 "$PROJECT_ROOT"/manage.py migrate
}

function va() {
    # activate python venv
    if [ ! -f ./venv ]; then
        python3 -m venv venv
    fi
    source ./venv/bin/activate
}

alias mig="migrate"
