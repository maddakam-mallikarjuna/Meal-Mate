# Django Food Ordering Web App

## Overview
This is a web application developed using Django that allows users to browse restaurants, view menus, add items to a cart, and make payments via Razorpay. The app also features an admin panel where administrators can manage restaurants, menus, and items.

## Features

### User Features
- **User Authentication**: Users can sign up and log in.
- **View Restaurants**: Browse a list of available restaurants.
- **Menu and Cart**: View menu items, add items to cart, and update quantities.
- **Order Processing**: Purchase items from the cart.
- **Payment Integration**: Razorpay is used for secure payments.

### Admin Features
- **Admin Authentication**: Admins have separate login access.
- **Restaurant Management**: Add, edit, and delete restaurants.
- **Menu Management**: Add, update, or delete menu items for each restaurant.
- **Order Management**: View and manage customer orders.

## Installation

### Prerequisites
- Python (>= 3.x)
- Django (>= 4.x)
- Razorpay API Keys
- Database (SQLite by default, but configurable for PostgreSQL or MySQL)

### Steps to Install
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Arjun-0608/Meal-Mate.git
   cd Meal-Mate
   ```
2. **Create a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run Migrations**
   ```bash
   python manage.py migrate
   ```
5. **Create a Superuser (Admin Panel Access)**
   ```bash
   python manage.py createsuperuser
   ```
6. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```
7. **Access the App**
   - Open `http://127.0.0.1:8000/` in a browser.
   - Admin panel: `http://127.0.0.1:8000/admin/`

## Project Structure
```
Food_Restaurant_Application/
│-- Food_Restaurant_Project/
│   │-- Admin_app/
│   │-- Food_Restaurant_Project/
│   │-- Main_app/
│   │-- static/
│   │-- staticfiles/
│   │-- User_app/
│   │-- db.sqlite3
│   │-- manage.py
│-- myvirtualenv/
```

## Future Enhancements
- **User Reviews & Ratings**: Allow users to review and rate restaurants.
- **Order Tracking**: Real-time order tracking for users.
- **Email Notifications**: Notify users about order status via email.
- **Discount Coupons**: Apply promotional offers and discounts.
- **Multi-Vendor Support**: Extend platform capabilities to support multiple vendors.

## Contributing
Feel free to contribute by submitting pull requests. Ensure to follow best coding practices and document any new features properly.

## License
This project is licensed under the MIT License.

## Contact
For any queries or suggestions, reach out via email or GitHub issues.

## GitHub Repository
[Meal-Mate](https://github.com/Arjun-0608/Meal-Mate)

