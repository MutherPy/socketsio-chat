python-sockets.io chat
======================
______________________

1) Start service.

    Settings

        Service's settings store in
    
            settings.py

        Settings that can be modified:
   
            1) FastAPI settings:

                FRONT_DIR -- path to folder with frontend
                MEDIA_DIR -- path to folder for storing media
                SECRET_KEY -- base64, encoded bytes

            2) Uvicorn settings:

                port -- port to serve
                workers -- uvicorn workers

    Service can be started as:

        Python script
    
            python main.py

        Docker container

            docker-compose up -d

    Dependencies are storing in:

        requirements.txt

2. Using service.

    By default, service starts on 8003.

    So, to start using go to:

        {domain_name}:8003

    Enter your username and password.
   
    Optionally you can specify room you want to connect.

    Otherwise, you will be connected to 'common' room.
