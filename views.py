import numpy as np
from flask import request, jsonify
import json
from utils import *

"""
Student.query.filter_by(firstname='Sammy').all()
Student.query.get(3)
@app.route('/<int:student_id>/')
def student(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template('student.html', student=student)
"""

def predict():
    img = np.array(json.loads(request.json), dtype=np.uint8)
    return (jsonify(predictSpoofing(img)))