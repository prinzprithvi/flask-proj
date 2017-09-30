from flask_mongoengine import MongoEngine
db = MongoEngine()


class User(db.Document):
    username = db.StringField(unique=True)
    active = db.BooleanField(default=True)
    authenticated = db.BooleanField(default=False)

    def get_id(self):
        return str(self.id)

    def is_active(self):
        return self.active

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
