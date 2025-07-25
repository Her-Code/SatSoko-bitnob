# SatSoko-bitnob
An integrated e-commerce platform leveraging Lightning payments via Bitnob.

📋 Prerequisites Checklist
Make sure the following are installed on your machine:

Node.js (v16 or higher)

Python (v3.8 or higher)

pipenv (pip install pipenv)

Git

🔧 Complete Installation Guide
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/satsoko-bitnob.git
cd satsoko-bitnob
2. Backend Setup
bash
Copy
Edit
# Navigate to backend folder
cd server

# 1. Navigate to the backend directory
cd server

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment

# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (CMD):
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate

# 4. Install all dependencies
pip install -r requirements.txt

# 5. Set environment variables (example for PowerShell)
$env:FLASK_APP = "app.py"
$env:FLASK_ENV = "development"

# 6. Initialize the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# 7. Run the Flask development server
flask run


# Set up the database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Start the backend server
flask run
3. Frontend Setup
bash
Copy
Edit
# Open a new terminal window/tab
cd client  # assuming the frontend folder is named 'client'

# Install Node.js dependencies
npm install

# If you face peer dependency issues
npm install --legacy-peer-deps

# Set up environment variables
cp .env.example .env
# Edit the .env file with frontend configuration

# Start the frontend dev server
npm start
4. Bitnob Integration Setup
bash
Copy
Edit
# Open another terminal window/tab
cd bitnob

# Install Node.js dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit the .env file with your Bitnob API credentials

# Start the Bitnob integration service
npm start

# 🌐 Application URLs
Service	URL	Description
Frontend	http://localhost:3000	React-based UI for the marketplace
Backend API	http://localhost:5000	Flask-powered REST API
Bitnob Service	http://localhost:3001	Bitnob Lightning integration

# 🧪 Testing the Application
1. Frontend Testing
Visit http://localhost:3000

Register a new user and log in

Browse the marketplace

Add items to cart and proceed to checkout

Test both traditional and Lightning payment methods

2. Backend API Testing
Use the provided Postman collection (or create your own)

Test endpoints for:

User authentication

Product listings

Cart and order operations

Confirm DB changes via migration and CRUD operations

3. Lightning / Bitnob Integration Testing
Create and verify Lightning invoices

Complete test payments

Confirm webhook handling and event tracking

Monitor transaction flow from frontend → Bitnob → backend

# 📚 Additional Resources
React Documentation https://reactjs.org/docs

Flask Documentation

Bitnob API Docs https://docs.bitnob.com/

🏁 Project Purpose
SatSoko-bitnob demonstrates seamless e-commerce integration with Bitcoin Lightning payments using Bitnob. It enables:

Easy vendor setup

Fast and cheap microtransactions

Modern web experience for emerging markets


