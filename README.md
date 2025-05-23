## Icars 🚗 Car Rental System

The **Car Rental System** is a robust Django-based full-stack web application that enables customers to rent cars or book taxis across India. It features a multi-role login system for **Customers**, **Clients**, and **Admins**, along with a subscription model and detailed role-based dashboards. The application supports dynamic location handling, offline/online payments, car management by state, and administrative control through Django's backend.

---

### 🌟 Features

#### 👤 Customer Features:

* **Profile Management:** Create, edit, and manage personal profiles.
* **Subscription Plans:**

  * Choose **monthly** or **yearly** subscription plans.
  * Payments are **online-only** for subscriptions.
* **Car Rental & Taxi Booking:**

  * Rent cars (min. 1 day) or book taxis **from any state in India**.
  * Pickup and drop locations remain the same as selected.
* **Location Options:**

  * Use current geolocation
  * Choose from **mini-map**
  * Select an iCars (company) **office location**
* **Booking Management:**

  * View **current and upcoming bookings** in the user profile.
* **Payments:**

  * Subscription: Online
  * Rides/Rentals: Offline at pickup

---

#### 🚘 Client Features:

* **Profile Management:** Create or edit client profiles.
* **Car Management:**

  * Add cars to **any state in India**
  * Edit or delete car listings
* **Booking Updates:**

  * View bookings made for their listed cars.
* **Payments:**

  * Income is processed **through admin** (owner approval).

---

#### 🛠️ Admin Features:

* **Admin-Only Backend Access:** No public signup; accounts managed via Django Admin.
* **Profile Management:** Add or update admin profiles.
* **User Management:**

  * Edit/view **customer** and **client** details
  * Ban customers or clients if necessary
* **Car Control:**

  * Add, edit, or delete any car listings by state
* **Booking Oversight:**

  * Monitor all bookings, including those for admin-listed cars
* **Subscription Analytics:**

  * View details of customers who purchased subscriptions
  * Approve subscription payments manually

---

### 🔧 Tech Stack

* **Backend:** Django (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** MySQL / SQLite
* **Tools & APIs:** Django Admin Panel, MiniMap Integration, Geolocation API

---

### 🏆 Highlights

* Full-featured multi-role authentication and access control.
* Dynamic location integration with geolocation & map options.
* Real-time profile-based dashboards for all user types.
* Split payment methods (online/offline) and subscription-based access.
* Solely developed and managed backend and frontend logic.

---
## 🚀 Getting Started

1. Clone the Repository 
    ```bash
    git clone https://github.com/Godsonmd/icars.git
    cd icars
    ```
  
2. (Optional) Create a Virtual Environment
    ```bash
    python -m venv venv
    ```
      - On Linux and macOS (Unix-like systems) use:
        ```bash
        source venv/bin/activate
        ```
      - On Windows use:
        ```bash
        venv\Scripts\activate
        ```
3. Install Dependencies
    ```bash
    pip install -r requirements.txt
    ```
4. Apply Migrations
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. Create Superuser
   ```bash
   python manage.py createsuperuser
   ```
6. Run the Development Server
   ```bash
   python manage.py runserver
   ```
7. Visit the Site:
   - User Interface: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Django Admin Panel: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)


