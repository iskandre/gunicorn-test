#! /bin/sh
set -e
if [ -f ./.env ]
then
  export $(cat ./.env | xargs)
fi
printenv
echo "env variables imported"

image_name="${IMAGE_NAME:-"el-gunicorn/test"}"
tag_name="${TAG_NAME:-"gunicorn-meinheld"}"
use_tag="$image_name:$tag_name"

DOCKERFILE="${tag_name}.dockerfile"
docker build -t "$use_tag" --file "./docker-images/${DOCKERFILE}" ./docker-images/
docker run --rm -it --name el-gunicorn-test --env-file ./.env -p 8001:8001 $use_tag