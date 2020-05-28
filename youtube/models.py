from datetime import datetime
from youtube import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    age = db.Column(db.Integer, nullable=False)
    address = db.Column(db.Text, nullable=False)
    register_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    videos = db.relationship('Video', backref='author', lazy='dynamic')

    def __repr__(self):
        return f"User('{self.user_name}', '{self.email}')"


class Video(db.Model):
    video_id = db.Column(db.Integer, primary_key=True)
    video_title = db.Column(db.String(120), nullable=False)
    video_content = db.Column(db.String(40), nullable=False)
    video_size = db.Column(db.Float, nullable=False)
    views_count = db.Column(db.Integer, nullable=False, default=0)
    upload_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    likes_count = db.Column(db.Integer, nullable=False, default=0)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f"Video('{self.video_title}', '{self.upload_time}')"


class Likes(db.Model):
    like_id = db.Column(db.Integer, primary_key=True)
    like = db.Column(db.Integer, nullable=False, default = 0)
    like_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    video_id = db.Column(db.Integer, db.ForeignKey('video.video_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f"Video('{self.video_id}', '{self.user_id}', {self.like})"


class Comments(db.Model):
    comment_id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    comment_time = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    video_id = db.Column(db.Integer, db.ForeignKey('video.video_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def __repr__(self):
        return f"Video('{self.user_id}', '{self.comment}', {self.video_id})"