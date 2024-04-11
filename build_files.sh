echo "BUILD START" 
<<<<<<< HEAD
python -m ensure pip 
python -m pip install -r requirements.txt 
python manage.py collectstatic --noinput --clear 
echo "BUILD END"
=======
python3.9 -m ensurepip 
python3.9 -m pip install -r requirements.txt 
python3.9 manage.py collectstatic
echo "BUILD END"
>>>>>>> f68ab5b7fe624ab13f0de34138b4310974e0340a
