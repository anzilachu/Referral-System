This is a Django API for a user referral system.

Features:

User Registration
User Details Retrieval
Referral List Retrieval

Endpoints:

1. Register: (POST /register/)
    username (string, required)
    email (string, required)
    password (string, required)
    referral_code (string, optional)

2. User Details: (GET /details/)
    Request
      Headers:
      Authorization: Token <your_token_here>
    Response:
      username (string)
      email (string)
      referral_code (string)
      registration_timestamp (datetime)

3. Referrals: (GET /referrals/)
  Request
    Headers:
    Authorization: Token <your_token_here>
  Response:
    A list of dictionaries, each containing:
    name (string) of the referred user
    referral_code (string) of the referred user
    registration_timestamp (datetime) of the referred user
    Pagination: Results are paginated (e.g., 20 users per page).
