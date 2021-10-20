#! /bin/sh
set -e

if [ -f env_concurrency.list ]
then
  export $(cat env_concurrency.list | xargs)
fi
echo "env variables exported"
printenv

bash entrypoint.sh
bash start.sh