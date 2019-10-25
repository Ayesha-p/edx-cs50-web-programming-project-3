# Project 3 : PIZZA!

## Web Programming with Python and JavaScript

# This project has been created by ***OM SANTOSHKUMAR MASNE*** .

### Created on 27/03/2019.
### All dates mentioned in this project are in the format: DD/MM/YYYY.

### This website is a project website created for EDX course, Web Programming with Python and JavaScript.

### This is an web-app for an online PIZZA SHOP.

---

### USAGE:

#### Requirements:

* Install the necessary requirements: `pip install -r requirements.txt`.

#### SAFETY CHECKS:

* Check the `settings.py` file in `pizza` directory.

#### DATABASE SETUP:

* Setup the database by using the following commands in the project root directory:
1. `python manage.py makemigrations`.
2. `python manage.py migrate`.

#### SETUP ADMIN:

* Run the following commands:
1. `python manage.py createsuperuser`.
2. Follow on screen instructions.

#### Running the server (app):

* Type these commands in the terminal from the project root directory:
    * `python manage.py runserver`.

#### ADDING MENU ITEMS TO DATABASE:

1. Login to Django Administration interface.
2. Add the desired items to their respective categories.

---

### The website's functions as described below:

* This project is a website for an online pizza shop.

* The customer's experience:

    * The '/' route lands the user at the homepage. The website's homepage shows the menu items.

    * If the user is not logged in, then the menu items cannot be added to cart.

        * The user has to register to use the features of the website.

        * The user may register by using the `SIGNUP` button on the homepage. This will open the signup form.

        * Once the user is registered successfully, the user is redirected to the website homepage. If there are problems in registration, then a error page is shown.

        * The user can login to his account using the `LOGIN` button available at the homepage.

    * The user can then select the desired items from the menu by click on the appropriate option (large/small/default size).

    * The user can check his cart in the profile section, by clicking on the `CART` button.

        * The user can remove items from the cart by clicking on them.

        * The user also has an option to get the price of current cart items.

        * The user can also check the status of his recent orders from the profile.

        * Upon selecting an order id from the recent orders section, the user is displayed the order's items and the order's status.

* The shop worker's experience:

    * The '/' route lands the user at the shop's interface.

    * Recently placed orders (maximum 10 at a time) are shown in shop's interface.

    * Any of these orders can be selected to view its contents and set its status to complete (denoting the order has been successfully completed).

* Menu items and their prices can be changed through the Django Administration interface.


A footer is also shown on index (homepage) page, displaying the name of the creator of this project and short information about the project.


Many other HTML and CSS properties are used in this project website to enhance its appearance.
This project website is also compatible with devices with small screens (screen resolution).

---

### OTHER NOTES:

* Using anything related to user should not be used in making custom id (eg. Order ids), as it is a bad practice.

* In this project, local storage is used for storing the cart items and are not stored on the server.

* As new user might be able to access other user's carts, and might be considered as an security issue.

* So, as a security measure and to let others use the cart feature, the local storage items are cleared once the user logs out.

---

## This project uses [DJANGO](https://www.djangoproject.com).

## This project uses [BOOTSTRAP](https://getbootstrap.com).

---

## License:
### Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
### Copyright (c) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
