# to rain rasa
rasa train

# to run rasa shell with local files
rasa shell --model model --credentials ./local_files/credentials.yml --endpoints ./local_files/endpoints.yml --debug --cors "*" --enable-api
rasa run --model model --credentials ./local_files/credentials.yml --endpoints ./local_files/endpoints.yml --debug --cors "*" --enable-api

# permissions
sudo chgrp -R root /etc/rasa/* && sudo chmod -R 770 /etc/rasa/*
sudo chown -R 1001 /etc/rasa/db && sudo chmod -R 750 /etc/rasa/db

# to build actions image
docker build -t kiran_action:v1.0.0 .

# login user
sudo python3 rasa_x_commands.py create --update admin me <PASSWORD>

