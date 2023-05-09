
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':"https://faceattendence-729e0-default-rtdb.asia-southeast1.firebasedatabase.app/"
    })

ref = db.reference('Students')


data = {
    "321654":
        {
            "name": "Aritra Chatterjee",
            "major": "CSE",
            "starting_year":2019,
            "total_attendance":6,
            "year":4,
            "sem":8,
            "last_attendance_time": "2023-04-30 00:54:34"
        },
    "349652":
        {
            "name": "Alokendu Ghosh",
            "major": "CSE",
            "starting_year":2019,
            "total_attendance":5,
            "year":4,
            "sem":8,
            "last_attendance_time": "2023-04-30 00:54:34"
        },
    "358421":
        {
            "name": "Arijit",
            "major": "CSE",
            "starting_year":2019,
            "total_attendance":8,
            "year":4,
            "sem":8,
            "last_attendance_time": "2023-04-30 00:54:34"
        },
}

for key,value in data.items():
    ref.child(key).set(value)
