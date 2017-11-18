""" Models and database functions for Community database. """

from flask_sqlalchemy import SQLAlchemy
# from flask_login import UserMixin

# Connect to the PostgreSQL database

db = SQLAlchemy()

# Model definitions


class Address(db.Model):
    """Standard format for address information for user location."""

    __tablename__ = 'addresses'

    add_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    lat = db.Column(db.Float(), nullable=False)
    lng = db.Column(db.Float(), nullable=False)
    formatted_add = db.Column(db.String(200), nullable=True)

    def __repr__(self):
        """Prints address object in a more helpful way"""

        return "<Address: add_id=%s lat=%s lng=%s>" % (self.add_id,
                                                       self.lat,
                                                       self.lng)


class Donor(db.Model):
    """Donor information collected when user registers."""

    __tablename__ = 'donors'

    donor_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    add_id = db.Column(db.ForeignKey(Address.add_id), nullable=True)
    phone_number = db.Column(db.String(100), nullable=True)

    address = db.relationship("Address", backref=db.backref("donors"))

    def __init__(self, name, email, password, add_id):
        self.name = name
        self.email = email
        self.password = password
        self.add_id = add_id

    def __repr__(self):
        """Prints donor object in a more helpful way"""

        return "<Donor: donor_id=%s name=%s email=%s>" % (self.donor_id, self.name,
                                                          self.email)

    # Necessary functions for Flask-login
    # def get_id(self):
    #     return str(self.user_id)


class Receiver(db.Model):
    """Receiver information collected when user registers."""

    __tablename__ = 'receivers'

    receiver_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    email = db.Column(db.String(75), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    add_id = db.Column(db.ForeignKey(Address.add_id), nullable=True)
    phone_number = db.Column(db.String(100), nullable=True)

    address = db.relationship("Address", backref=db.backref("receivers"))

    def __init__(self, name, email, password, add_id):
        self.name = name
        self.email = email
        self.password = password
        self.add_id = add_id

    def __repr__(self):
        """Prints receiver object in a more helpful way"""

        return "<Receiver: receiver_id=%s name=%s email=%s>" % (self.receiver_id, self.name,
                                                                self.email)

    # Necessary functions for Flask-login
    # def get_id(self):
    #     return str(self.user_id)


class Food(db.Model):
    """Food specifications."""

    __tablename__ = 'foods'

    food_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    donor_id = db.Column(db.ForeignKey(Donor.donor_id), nullable=False)
    receiver_id = db.Column(db.ForeignKey(Receiver.receiver_id), nullable=True)
    name = db.Column(db.String(50), nullable=False)
    date_of_expiration = db.Column(db.DateTime, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    prepared = db.Column(db.Boolean, nullable=False)
    gluten = db.Column(db.Boolean, nullable=False)
    refrigerated = db.Column(db.Boolean, nullable=False)
    nuts = db.Column(db.Boolean, nullable=False)
    dairy = db.Column(db.Boolean, nullable=False)
    vegetarian = db.Column(db.Boolean, nullable=False)

    donor = db.relationship("Donor", backref=db.backref("donors"))
    receiver = db.relationship("Receiver", backref=db.backref("receivers"))

    def __repr__(self):
        """Prints category object in a more helpful way"""

        return "<Food: foods_id=%s name=%s>" % (self.food_id,
                                                self.name)


##############################################################################
# Helper function

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PstgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///food'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from server import app
    connect_to_db(app)
    print "Connected to DB."

    # # In case tables haven't been created, create them
    db.create_all()
