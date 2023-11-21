#!/usr/bin/env bash
# a script to setup development virtual environment and install python django
python3 -m  venv
source venv/bin/activate
python3 -m pip install Django

# frontend
npx create-react-app  main
cd main
npm install -D tailwindcss
npx tailwindcss init
