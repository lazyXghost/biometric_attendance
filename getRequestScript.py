import requests
import json
import cv2
import numpy as np

# url = 'http://localhost:5000/markAttendance'
# headers = {'Content-Type': 'application/json'}
# response = requests.post(url, headers=headers, json=json.dumps(np.array(cv2.imread('Extras/Self made model/Dataset/val_real.jpeg')).tolist()))
# print(response.json())

# url = "http://localhost:5000/leaveRequest"
# headers = {"Content-Type": "application/json"}
# response = requests.post(url, headers=headers, json=json.dumps({"student_id": 1, "name": "dishti", "rollno": "b20286", "mobile": "8130091185", "email": "b20286.students.iitmandi.ac.in", "hostel": "B16", "roomno": 13, "home_town": 1, "start": "2023-5-20", "end": "2023-5-30", "location": "Delhi", "emergency_no": "813009", "status": 1}))
# print(response.json())

# url = "http://localhost:5000/attendanceRecord"
# headers = {"Content-Type": "application/json"}
# response = requests.post(url, headers=headers, json=json.dumps({"startdate":"2023-05-23", "enddate":"2023-05-28"}))
# print(response.json())

# url = "http://localhost:5000/leaveStatus"
# headers = {"Content-Type": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.json())
