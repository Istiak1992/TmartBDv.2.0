{
    "apps": [{
        "name": "server",
        "script": "manage.py",
        "args": ["runserver", "0.0.0.0:8000"],
        "exec_mode": "fork",
        "wait_ready": true,
        "autorestart": false,
        "max_restarts": 5,
        "interpreter" : "pipenv",
        "interpreter_args": "run python3"
    }]
}