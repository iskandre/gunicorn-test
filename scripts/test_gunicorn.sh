#! /bin/sh
set -e

if [ -f ./.env ]
then
  export $(cat ./.env | xargs)
fi
echo "env variables exported"
printenv

bash ./docker-images/entrypoint.sh
bash ./docker-images/start_gunicorn.sh