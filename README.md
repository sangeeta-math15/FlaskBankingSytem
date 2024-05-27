# Banking System
This project is a simple banking system built using Python, Flask, and MongoDB following the MVC (Model-View-Controller) architecture. The system supports customer login with access tokens and basic banking operations such as viewing transaction history, depositing, withdrawing, and checking balances. Additionally, it includes optional banker features like viewing the account list and transaction history. The project also emphasizes security and error handling.


`Table of Contents `:
- Features
- Project Structure
- Installation
- Configuration
- Running the Application
- API Endpoints
- Security
- Error Handling
- Dependencies

`Features`
- Customer Login: Secure login using username and password with JWT access tokens.
- Transactions: Perform deposits and withdrawals, view transaction history, and check account balance.
- Banker Features (Optional): View the list of all customer accounts and their transaction history.
- Security: JWT authentication, environment-based secret keys, and input validation.
- Error Handling: Comprehensive error handling for invalid inputs, authentication issues, and other potential errors.

`Installation`
- Create a virtual environment:

- `python3 -m venv venv`
- `source venv/bin/activate`

- Install dependencies:
`pip install -r requirements.txt`

- Set up MongoDB:
Ensure MongoDB is installed and running. Create a database named banking_system.

`Configuration`
- Environment Variables:Create a .env file in the root directory and add the configurations:

- Initialize the database:If necessary, create initial collections and insert initial data (e.g., user accounts).

`Running the Application`
- python run.py


`API Endpoints`
- customer Endpoints:
- POST /login: Customer login.
- POST /deposit: Deposit money.
- POST /withdraw: Withdraw money.
- GET /balance: Check account balance.
- GET /transactions: View transaction history.

- Banker Endpoints (Optional):
- GET /accounts: List all customer accounts.
- GET /transactions: View all transactions.

`Security`
- Authentication:JWT tokens are used to secure endpoints.
Secret Keys: Secret keys are stored in environment variables.
Input Validation: Proper input validation is implemented to prevent invalid data.


`Error Handling`
- Validation Errors: Detailed messages for invalid inputs.
Authentication Errors: Proper handling of authentication failures.
General Errors: Catch-all error handler for unexpected issues.

`Dependencies`
- Flask
- Flask-JWT-Extended
- PyMongo
- python-dotenv
