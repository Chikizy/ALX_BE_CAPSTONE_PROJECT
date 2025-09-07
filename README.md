# ALX_BE_CAPSTONE_PROJECT
# ALX_BE_CAPSTONE_PROJECT: a rentals management api

The Rentals Management API is designed to manage rental properties. 
It allows property owners to create, update, and delete rental listings, while renters can view and search listings. 
The API supports user authentication with role-based permissions (owners vs. renters) and provides pagination and filtering for efficient listing management.

Features Implemented
- **User Authentication (accounts app)**:
  - User registration with role validation (`owner` or `renter`).
  - User login with token generation.
  - Profile retrieval for authenticated users.
- **Rental Listings (listings app)**:
  - CRUD operations for rental listings (create, read, update, delete).
  - Role-based permissions: Only owners can create, update, or delete listings; renters can view listings.
  - Pagination (10 listings per page, adjustable).
  - Filtering by address and price, searching by title, description, or address.

***  Project Structure   ***
rentals_api/: Django project directory
    -accounts/: App for user authentication
    -listings/: App for Rental listings

***    API Endpoints    ***
User Authentication:
    **POST** /rental_api/accounts/register/: Register a user (public)
    **POST** /rental_api/accounts/login/: login and get a token
    **GET** /rental_api/accounts/profile/: Retrieve user profile (authenticated)

Rental Listings:
    **GET** /api/listings/: List all listings (authenticated, paginated).
    **POST** /api/listings/: Create a listing authenticated,owners only).
    **GET** /api/listings/<id>/: Retrieve a listing (authenticated).
    **PUT/PATCH** /api/listings/<id>/: Update a listing (authenticated, owners only).
    **DELETE** /api/listings/<id>/: Delete a listing (authenticated, owners only).

TESTING

1. TEST USER AUTHENTICATION
    **REGISTER A USER:**
    Request:
        Method: **POST**
        URL: http://localhost:8000/rentals_api/accounts/register/
        Body (JSON):
        {
            "username": "testowner",
            "email": "owner@example.com",
            "password": "securepassword123",
            "role": "owner",
            "bio": "Property owner",
            "contact_info": "0123-456-789"
        }

    **TEST INVALID ROLE:**
    Request:
        Method: **POST**
        URL: http://localhost:8000/rentals_api/accounts/register/
        Body (JSON):
        {
            "username": "testrole",
            "email": "roletest@example.com",
            "password": "securepassword111",
            "role": "free",
            "bio": "Property renter",
            "contact_info": "0123-456-7891"
        }
        
    **LOGIN**
    Request:
        Method: **POST**
        URL: http://localhost:8000/rentals_api/accounts/login/
        Body (JSON):
        {
            "username": "testowner",
            "password": "securepassword123"
        }

    **RETRIEVE A PROFILE**
        Request:
            Method: **GET**
            URL: http://localhost:8000/rentals_api/accounts/profile/
        Headers: Authorization: Token <user-token>

2.  TEST RENTAL LISTINGS
    Owners can create, retrieve, update and del.ete listings as long as the listing creator is matches the user sending the 'delete' request
    Renters can only retrieve or read listings.

    **CREATE A LISTING (OWNER):**
    Request:
        **POST**
        URL: http://localhost:8000/api/listings/
        Headers: Authorization: Token <owner_token>
        Body (JSON):
        {
            "title": "Cozy Beach House",
            "description": "A lovely beachfront property.",
            "address": "123 Ocean Drive",
            "price_per_night": 150.00,
            "availability_dates": {"start": "2025-09-01", "end": "2025-09-30"}
        }
        
    **LIST ALL LISTINGS**
    Request:
        **GET**
        URL: http://localhost:8000/api/listings/
        Headers: Authorization: Token <owner_token or renter_token>

    **FILTER LISTINGS**
    Request:
        **GET**
        URL: http://localhost:8000/api/listings/?price_per_night=150.00
        Headers: Authorization: Token <owner_token or renter_token>

    **SEARCH LISTINGS**
    Request:
        **GET**
        URL: http://localhost:8000/api/listings/?search=beach
        Headers: Authorization: Token <owner_token or renter_token>

    **RETRIEVE A LISTING**
        Request:
            **GET**
            URL: http://localhost:8000/api/listings/1/
            Headers: Authorization: Token <owner_token or renter_token>
    
    **UPDATE A LISTING**
    Request:
        **PUT**
        URL: http://localhost:8000/api/listings/1/
        Headers: Authorization: Token <owner_token or renter_token>
        Body (JSON):
        {
            "title": "Updated Beach House",
            "description": "A lovely beachfront property.",
            "address": "123 Ocean Drive",
            "price_per_night": 175.00,
            "availability_dates": {"start": "2025-10-01", "end": "2025-10-31"}
        }

    **DELETE A LISTING(OWNER)**
    Request:
        **DELETE**
        URL: http://localhost:8000/api/listings/1/
       Headers: Authorization: Token <owner_token>

    **TEST UNAUTHORIZED ACTION(RENTER)**
    Request:
        **POST**
        URL: URL: http://localhost:8000/api/listings/1/
        Headers: Authorization: Token <renter_token>
        Body (JSON):
            {
                "username": "testowner",
                "email": "owner@example.com",
                "password": "securepassword123",
                "role": "owner",
                "bio": "Property owner",
                "contact_info": "0123-456-789"
            }
