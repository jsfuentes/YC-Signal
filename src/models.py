from mongoengine import *
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
import boto3
from botocore.client import Config

from . import login_manager

s3 = boto3.client('s3', 
    config=Config(signature_version='s3v4')
)

class Users(UserMixin, Document):
    email = EmailField(required=True)
    password_hash = StringField()

    @property
    def password(self):
        raise AttributeError("password unreadable")

    #can just set with user.password = password and it will be auto hashed
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    @login_manager.user_loader
    def load_user(uid):
        return Users.objects(id=uid).first()

class Podcasts(Document):
    title = StringField()
    host = StringField()
    description = StringField()
    s3_photo_key = StringField()
    s3_photo_url = StringField()

    def presignPhoto(self):
        if self.s3_photo_key:
            self.s3_photo_url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': 'yc-signal-podcast-photo',
                    'Key': self.s3_photo_key
                }
            )
        self.save()

class Episodes(Document):
    title = StringField()
    podcast = ReferenceField('Podcasts')
    s3_audio_key = StringField()
    s3_audio_url = StringField()
    
    def presignAudio(self):
        if self.s3_audio_key:
            self.s3_audio_url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': 'yc-signal-episode-audio',
                    'Key': self.s3_audio_key
                }
            )
        self.save()
    
class Soundbites(Document):
    title = StringField()
    episode = ReferenceField('Episodes')
    podcast = ReferenceField('Podcasts')
    length = IntField()
    s3_audio_key = StringField()
    s3_audio_url = StringField()
    
    def presignAudio(self):
        if self.s3_audio_key:
            self.s3_audio_url = s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': 'yc-signal-soundbite-audio',
                    'Key': self.s3_audio_key
                }
            )
        self.save()

    