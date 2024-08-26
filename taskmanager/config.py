import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://uv06g5mpm02:hMh3OOUaGtwC@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/map_moan_perm_158073'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
