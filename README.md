Zappy is a tool that listen on a slack channel waiting for a trigger word 'go' to go collect tweets from twitter and store them in a mongo DB.

Tweets collected can be viewed on a web page

clone this repo 
change directory to the root of the project

within a virtualenv 
execute the following commands:
pip install -r requirments.txt
python3 manage.py migrate
python3 manage.py runserver
ssh -R zappy:80:localhost:8000 serveo.net //tunnel url for slack
cd frontend
npm start



