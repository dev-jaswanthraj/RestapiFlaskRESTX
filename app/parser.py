from flask_restx import reqparse
import datetime as dt

def dateChecker(value):
    Y, m, d = list(map(int, value.split("-")))
    return dt.datetime(year=Y, month=m, day=d)

userRequestParser = reqparse.RequestParser()
userRequestParser.add_argument("name", type = str)
userRequestParser.add_argument("dob", type = dateChecker)