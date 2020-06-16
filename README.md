# Introduction

This is a repository consisting of basic features of Youtube 

## Instructions

    cd youtube
    pip install -r requirements.txt
    python youtube.py

I have covered basic of youtube as :

1. A user can register and login using the registered email id.
2. Any user can watch the video.
3. Any authenticated user can upload a video.
4. Any authenticated user can like and comment on any video.
5. Everybody will be able to see the comments and likes on each post.
6. User can visit and update his own profile.
7. User can update the video also.
8. all static files will be saved in static folder inside the project.

## Directory Structure :

    youtube
        |––app
        |    ├── __init__.py
        |    ├── __pycache__
        |    │   ├── __init__.cpython-37.pyc
        |    │   ├── forms.cpython-37.pyc
        |    │   ├── models.cpython-37.pyc
        |    │   └── routes.cpython-37.pyc
        |    ├── forms.py
        |    ├── models.py
        |    ├── routes.py
        |    ├── static
        |    │   ├── avatar
        |    │   │   ├── 23d8d20e2fa8df7d.jpg
        |    │   │   ├── 55276111791d6acc.jpg
        |    │   │   ├── 5d2f51d83ddf8140.jpg
        |    │   │   ├── avatar.png
        |    │   │   └── fb1f24e3840a74b0.jpg
        |    │   ├── cover_pics
        |    │   │   └── cover.png
        |    │   ├── css
        |    │   │   └── main.css
        |    │   └── videos
        |    │       ├── 00cd3681b6b97632.mov
        |    │       ├── 12004f8cfb357640.mov
        |    │       ├── 1dfd854cecaa239e.mov
        |    │       ├── 2640298ae9ebb4e4.mov
        |    │       ├── 2bdd405edcdaffbe.mov
        |    │       ├── 2ccdacd063bf37eb.mov
        |    │       ├── 4179f0e211262d7f.mov
        |    │       ├── 43355c2bad63f306.mov
        |    │       ├── 55a63f36d249c6c5.mov
        |    │       ├── 77b112d30a605bee.mov
        |    │       ├── 77da43ae5ae5e336.mov
        |    │       ├── 9c104d496984104c.mov
        |    │       ├── a6ff2fede0cb68be.mov
        |    │       ├── a97014b9c9d77f66.mov
        |    │       ├── bc16df7174913450.mov
        |    │       ├── da951eb38314dfc5.mov
        |    │       └── f67c2ab6c15a510a.mov
        |    └── templates
        |        ├── account.html
        |        ├── home.html
        |        ├── layout.html
        |        ├── login.html
        |        ├── register.html
        |        ├── update_video.html
        |        ├── upload.html
        |        └── video.html
        |–– migrations
        |–– venv
        |–– .gitignore
        |–– config.py
        |–– README.md
        |–– requirements.txt
        |–– youtube.code-workspace
        |–– youtube.db
        |–– youtube.py