#!/bin/bash

ownership() {
    # Fixes ownership of output files
    # source: https://github.com/BD2KGenomics/cgl-docker-lib/blob/master/mutect/runtime/wrapper.sh#L5
    user_id=$(stat -c '%u:%g' /code)
    chown -R ${user_id} /code
}


echo "Updating and installing missing packets"
pip install -r ./requirements.txt
echo "Waiting for postgress"
chmod +x /scripts/wait-for-it.sh
/scripts/wait-for-it.sh -t 80 $POSTGRES_SERVICE:5432 || exit 1

echo ''
echo '--------------------------'
echo 'Database migration'
echo '--------------------------'
echo ''
python /code/manage.py makemigrations || exit 1
python /code/manage.py migrate || exit 1

echo ''
echo '--------------------------'
echo 'Fixing ownership of files'
echo '--------------------------'
echo ''
ownership

echo ''
echo '--------------------------'
echo 'Run command'
echo $@
echo '--------------------------'
echo ''
$@ || exit 1