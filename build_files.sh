# installl dependencies using the correct python environment 
python3 -m pip install  --upgrade pip   #upgrade pip to ensure compatibility 
python3 -m pip install -r requirements.txt
python3 manage.py collectstatic --noinput
#hth