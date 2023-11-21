#!/usr/bin/env bash
# a script to setup development virtual environment and install python django
python3 -m  venv
source venv/bin/activate
python3 -m pip install Django

# frontend
yarn create vite main --template react
cd main
yarn
yarn dev
yarn add -D tailwindcss postcss autoprefixer
yarn tailwindcss init -p
yarn dev
