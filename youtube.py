from app import app, db
from app.models import User, Video, Likes, Comments


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Video': Video, 'Likes': Likes, 'Comments': Comments}


if __name__ == '__main__':
    app.run(debug=True)
