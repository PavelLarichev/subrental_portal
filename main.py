from app.app import start_service

app = start_service()


def runserver():
    app.run(host='0.0.0.0', port=8000)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)