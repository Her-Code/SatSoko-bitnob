# SatSoko-bitnob
## **📋 Prerequisites Checklist**

- Node.js 16+ installed
- Python 3.8+ installed
- pipenv installed (`pip install pipenv`)
- Git installed


## **🔧 Complete Installation Process**

### **1. Clone the Repository**
git clone https://github.com/your-username/satsoko-bitnob.git
cd satsoko-bitnob

2. Backend Setup
   # Navigate to backend
cd server

# Install Python dependencies
pipenv install

# Activate virtual environment
pipenv shell

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Initialize database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade

# Start backend server
flask run

3. Frontend Setup
   # Open new terminal and navigate to frontend

# Install Node.js dependencies
npm install

# If you encounter peer dependency issues
npm install --legacy-peer-deps

# Set up environment variables
cp .env.example .env
# Edit .env with your configuration

# Start frontend development server
npm start

4. Bitnob Integration Setup
   # Open new terminal and navigate to bitnob
cd bitnob

# Install Node.js dependencies
npm install

# Set up environment variables
cp .env.example .env
# Edit .env with your Bitnob API credentials

# Start Bitnob service
npm start

## **🌐 Application URLs**

| Service | URL | Description
|-----|-----|-----
| Frontend | [http://localhost:3000](http://localhost:3000)
| Backend API | [http://localhost:5000](http://localhost:5000)
| Bitnob Service | [http://localhost:3001](http://localhost:3001)

## **🧪 Testing the Application**

### **1. Frontend Testing**

- Visit `http://localhost:3000`
- Test user registration and login
- Browse marketplace and add items to cart
- Test checkout process with both payment methods


### **2. Backend API Testing**

- Use Postman collection provided
- Test all API endpoints
- Verify database operations
- Check authentication flows


### **3. Lightning Integration Testing**

- Test Lightning invoice creation
- Verify payment processing
- Check webhook functionality

  ## **📚 Additional Resources**

- [React Documentation](https://reactjs.org/docs)
- Flask Documentation
- https://docs.bitnob.com/
