#!/usr/bin/env bash

set -o errexit

# los pasos para correr django en un servidor
pip install --upgrade pip
# instalar los requerimiento del proyecto
pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate
