from main import db


class User1(db.Model):  # notice that our class extends db.Model
    __tablename__ = 'userregister'  # this is the name we want the table in database to have. id=db.Column(db.Integer, primary_key=True)


firstname = db.Column(db.String(20), unique=False, nullable=False)
lastname = db.Column(db.String(20), unique=False, nullable=False)
dateofbirth = db.Column(db.String(20), unique=False, nullable=True)
residentialaddress = db.Column(db.String(20), unique=True, nullable=False)
nationality = db.Column(db.String(20), unique=False, nullable=True)
nationalidentificationnumber = db.Column(db.String(50), unique=True, nullable=False)
email = db.Column(db.String(50), unique=True, nullable=False)
password = db.Column(db.String(256), unique=False, nullable=False)
# represent the object when it is queried for def __repr__(self):
return '<Register {}>'.format(self.id)


class User2(db.Model):  # notice that our class extends db.Model
    __tablename__ = 'userregister'  # this is the name we want the table in database to have. id=db.Column(db.Integer, primary_key=True)


firstname = db.Column(db.String(20), unique=False, nullable=False)
lastname = db.Column(db.String(20), unique=False, nullable=False)
dateofbirth = db.Column(db.String(20), unique=False, nullable=True)
residentialaddress = db.Column(db.String(20), unique=True, nullable=False)
nationality = db.Column(db.String(20), unique=False, nullable=True)
nationalidentificationnumber = db.Column(db.String(50), unique=True, nullable=False)
email = db.Column(db.String(50), unique=True, nullable=False)
password = db.Column(db.String(256), unique=False, nullable=False)
# represent the object when it is queried for def __repr__(self):
return '<Register {}>'.format(self.id)


class User3(db.Model):  # notice that our class extends db.Model
    __tablename__ = 'userregister'  # this is the name we want the table in database to have. id=db.Column(db.Integer, primary_key=True)


firstname = db.Column(db.String(20), unique=False, nullable=False)
lastname = db.Column(db.String(20), unique=False, nullable=False)
dateofbirth = db.Column(db.String(20), unique=False, nullable=True)
residentialaddress = db.Column(db.String(20), unique=True, nullable=False)
nationality = db.Column(db.String(20), unique=False, nullable=True)
nationalidentificationnumber = db.Column(db.String(50), unique=True, nullable=False)
email = db.Column(db.String(50), unique=True, nullable=False)
password = db.Column(db.String(256), unique=False, nullable=False)
# represent the object when it is queried for def __repr__(self):
return '<Register {}>'.format(self.id)
