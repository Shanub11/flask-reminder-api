from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# Initialize Flask app
app = Flask(__name__)

# Configure database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'reminders.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Models
class Reminder(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    message = db.Column(db.String(500), nullable=False)
    notification_method = db.Column(db.String(10), nullable=False)  # 'sms' or 'email'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Reminder {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'date': self.date.isoformat(),
            'time': self.time.isoformat(),
            'message': self.message,
            'notification_method': self.notification_method,
            'created_at': self.created_at.isoformat()
        }

# Routes
@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    data = request.get_json()
    
    # Validate required fields
    required_fields = ['date', 'time', 'message', 'notification_method']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Validate notification method
    if data['notification_method'].lower() not in ['sms', 'email']:
        return jsonify({'error': 'Invalid notification method. Use "sms" or "email"'}), 400
    
    try:
        # Parse date and time
        reminder_date = datetime.strptime(data['date'], '%Y-%m-%d').date()
        reminder_time = datetime.strptime(data['time'], '%H:%M').time()
        
        # Create new reminder
        reminder = Reminder(
            date=reminder_date,
            time=reminder_time,
            message=data['message'],
            notification_method=data['notification_method'].lower()
        )
        
        db.session.add(reminder)
        db.session.commit()
        
        return jsonify(reminder.to_dict()), 201
    
    except ValueError as e:
        return jsonify({'error': 'Invalid date or time format. Use YYYY-MM-DD for date and HH:MM for time'}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    reminders = Reminder.query.all()
    return jsonify([reminder.to_dict() for reminder in reminders])

# Create database tables
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
