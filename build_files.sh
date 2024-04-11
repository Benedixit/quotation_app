echo "BUILD START" 
python -m ensure pip 
pip install django
python manage.py makemigrations
python manage.py migrate
python -m pip install -r requirements.txt 
python manage.py collectstatic --noinput --clear 
echo "BUILD END"
