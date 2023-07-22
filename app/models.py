from app import db

# For Testing
class TestTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)

class ImportTestTable(db.Model):
    id = db.Column(db.Integer, primary_key = True)

# Real one, Simple Blog Application

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    dob = db.Column(db.DateTime)

    def __repr__(self):
        return f"<{self.name} {self.id}>"

