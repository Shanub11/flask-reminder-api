# Remind-Me-Later API ⏰

A lightweight Flask API for scheduling reminders with SMS/email notifications.

## ✨ Features
- **Schedule reminders** with custom messages and delivery times
- **Multiple notification channels** (Email & SMS ready)
- **Simple RESTful interface** (JSON in/out)
- **Persistent storage** (SQLite database)
- **Production-ready** (Error handling, input validation)

## 🛠️ Tech Stack
- Python 3.9+
- Flask (Web framework)
- SQLAlchemy (ORM)
- SQLite (Database)

## 🚀 Quick Start

### 1. Clone & Install
```bash
git clone https://github.com/Shanub11/flask-reminder-api.git
cd flask-reminder-api
pip install -r requirements.txt
```


### 2.  Start the Flask Server
python app.py

The API will be available at http://localhost:5000

**API Documentation
Base URL**
http://localhost:5000/api


**API Endpoints**
POST /api/reminders

**Create a new reminder**
Headers:
Content-Type: application/json

Request Body:
{
  "date": "2023-12-25",
  "time": "15:30",
  "message": "Christmas party",
  "notification_method": "email"
}

**🔍 Testing with Postman**
1. Setup in Postman
Open Postman and create a new collection

Add a new POST request

Set URL to http://localhost:5000/api/reminders

2. Configure Request
Method: POST

Headers:
Key: Content-Type
Value: application/json

Body:
Select "raw" and "JSON"
Paste the example JSON above

3. Send Request
Click "Send" button
Verify response (should be HTTP 201 Created)

Example successful response:

json
{
  "id": 1,
  "date": "2023-12-25",
  "time": "15:30:00",
  "message": "Christmas party",
  "notification_method": "email"
}

4. Test GET Request
Create new GET request to http://localhost:5000/api/reminders

Send to view all reminders

**💻 Command Line Testing**
cURL Example
bash
# Create reminder
curl -X POST http://localhost:5000/api/reminders \
  -H "Content-Type: application/json" \
  -d '{
    "date": "2023-12-25",
    "time": "15:30",
    "message": "Christmas party",
    "notification_method": "email"
  }'

# Get reminders
curl http://localhost:5000/api/reminders
