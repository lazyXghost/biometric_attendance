from flask import Flask
from views import * 

app = Flask(__name__)
# app.route('/markAttendance', methods=['POST'])(markAttendance)
app.route('/leaveRequest', methods=['POST'])(leaveRequest)
app.route('/attendanceRecord', methods=['POST'])(attendanceRecord)
app.route('/leaveStatus', methods=['GET'])(leaveStatus)

if __name__ == '__main__':
    app.run(debug=True)
