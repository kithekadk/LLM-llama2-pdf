#!/bin/bash
python -m venv .venv

pip install -r requirements.txt

cd chroma

git submodule update --init --recursive

docker-compose up --build

cd ../

docker build -t medassist .

docker run -d -p 5000:5000 medassist