from flask_restx import fields

class DateFormat(fields.Raw):
    def format(self, value):
        return value.strftime("%Y-%m-%d")
    
user_details = {
    "id": fields.Integer,
    "name": fields.String,
    "dob": DateFormat,
}