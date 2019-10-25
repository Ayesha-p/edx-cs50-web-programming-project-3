# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Regular_pizza, Sicilian_pizza, Toppings, Pasta, Salads
from .models import Subs, Dinner_platters
from .models import Custom_user, Orders

from . import extraFunc
import json

# Create your views here.

# This function acts as the homepage or '/' route of the website.
# It renders the homepage of the website and checks if the user is authenticated or not.
# If the user is not authenticated then the 'Login to add to cart' message is displayed.
# If the user is a customer (non-staff member) then the homepage with menu is displayed again.
# If the user is a staff member then the Shop's Interface is displayed.
def index(request):

    menu_section = []
    menu_section.append(Regular_pizza.objects.all())
    menu_section.append(Sicilian_pizza.objects.all())
    menu_section.append(Toppings.objects.all())
    menu_section.append(Pasta.objects.all())
    menu_section.append(Salads.objects.all())
    menu_section.append(Subs.objects.all())
    menu_section.append(Dinner_platters.objects.all())

    menu_section_head = ['Regular pizza', 'Sicilian pizza', 'Toppings', 'Pasta', 'Salads', 'Subs', 'Dinner platters']
    menu_section_head_data = ['Regular_pizza', 'Sicilian_pizza', 'Toppings', 'Pasta', 'Salads', 'Subs', 'Dinner_platters']

    menu = zip(menu_section, menu_section_head, menu_section_head_data)

    context = {'menu': menu}
    user = request.user

    if not request.user.is_authenticated:
        return render(request, "orders/index.html", context)
    else:
        username = user.get_username()

        if user.is_staff:
            context = {'username':username}
            return render(request, "orders/shop.html", context)
        else:
            context = {'menu': menu, 'username':username, 'user_logged_in':True}
            return render(request, "orders/index.html", context)

# This function renders the signup page.
def signup_page(request):
    return render(request, "orders/signup.html")

# This function renders the login page.
def login_page(request):
    return render(request, "orders/login.html")

# This function renders the logout page and logs the user out of the website.
# Additionally the rendered page clears the cart (For security reasons).
def logout_page(request):
    user = request.user
    logout(request)
    context = {'from':"ACCOUNT LOGOUT:", 'message':"LOGGED OUT SUCCESSFULLY!"}
    return render(request, "orders/misc.html", context)

# This function handles the requests for new accounts.
# If the desired new account can be created then that account is created and a summary page is rendered.
def new_account(request):
    username = str(request.POST.get("username"))
    password = str(request.POST.get("password"))
    first_name = str(request.POST.get("first_name"))
    last_name = str(request.POST.get("last_name"))
    email = str(request.POST.get("email"))
    info = ["username : " + username, "password : " + password, "email : " + email, 
    "first name : " + first_name, "last name : " + last_name]

    # Checks for invalid username or password or email field.
    if (username or password or email) == "":
        context = {"message":"INVALID USERNAME OR PASSWORD OR EMAIL"}
        return render(request, "orders/signup.html", context)

    # Checks if the provided username already exists in database or not.
    # If an username with same value is found then the signup page is rendered with an informative message.
    if (username or password) is not None:
        try:
            check_user_exist = User.objects.get(username = username)
            check_user_exist = True
        except User.DoesNotExist:
            check_user_exist = False

        if check_user_exist is True:
            context = {"message":"Username already taken!"}
            return render(request, "orders/signup.html", context)

        # Creates the user with the provided data.
        user = User.objects.create_user(username = username, password = password, email = email,
        first_name = first_name, last_name = last_name)
        user.save()

        user_custom = Custom_user(username = username)
        user_custom.save()

        customer_group = Group.objects.get(name = "CUSTOMER")
        user.groups.add(customer_group)

    # It now renders the account summary page.
    context = {'from':"NEW ACCOUNT CREATED!", 'info':info}
    return render(request, "orders/misc.html", context)

# This function handles the account login requests.
# It authenticates the user if proper username and password is provided.
# Upon successful authentication, this function renders the index page.
# If authentication is failed then the error message page is rendered.
def account_login(request):
    username = str(request.POST.get("username"))
    password = str(request.POST.get("password"))
    info = ["Username  : " + username, "Password : " + password]
    context = {'from':"ACCOUNT LOGIN", 'info':info}

    user = authenticate(request, username = username, password = password)

    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("orders:index"))
    else:
        context = {'from':"ACCOUNT LOGIN ERROR:", 'message':"INVALID CREDENTIALS!"}
        return render(request, "orders/misc.html", context)

# This function renders the user profile page.
def profile(request):
    old_order = False
    user = request.user
    username = str(user.get_username())

    # Checks if the user is authenticated or not.
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("orders:index"))

    # The 'SEARCH_LIMIT' is the maximum number of orders to be displayed in the latest orders area.
    SEARCH_LIMIT = 5
    user = Custom_user.objects.get(username = username)

    try:
        user_orders = (user.orders)
        user_orders = (user_orders.split(","))[:SEARCH_LIMIT]
        check_old_orders = True
    except:
        check_old_orders = False

    previous_orders = []
    previous_orders_status = []

    if check_old_orders is True:
        if len(user_orders) == 0:
            old_order = False
        else:
            old_order = True
            for i in range(0, len(user_orders)):
                previous_orders.append(user_orders[i])
                order = Orders.objects.get(order_id = user_orders[i])
                order_status = order.status
                if order_status is True:
                    order_status = "COMPLETE"
                else:
                    order_status = "PENDING"
                previous_orders_status.append(order_status)

    previous_orders = zip(previous_orders, previous_orders_status)

    context = {'username':username, 'old_order':old_order ,'previous_orders':previous_orders}
    return render(request, "orders/profile.html", context)

# This function is used to place an user's order.
# It calculates the price of the order and creates that order and places it (Saves the order_id in the respective user's object).
def place_order(request):
    user = request.user
    username = str(user.get_username())
    cart = str(request.POST.get("cart-items-place-order"))
    total_price, cart_status = extraFunc.cal_price(cart)
    price = str(total_price)
    order_id = '0'
    if cart_status is True:
        order_status = True
    else:
        order_status =False

    if price == '0':
        order_status = False
    else:
        if cart_status is True:
            order_id = extraFunc.make_order(username, cart, price)
            order_id = str(order_id)
            extraFunc.place_order(username, order_id)

    order_id_status = order_status
    cart = cart.split(",")
    context = {'new_order':True, 'price':price, 'order_status':order_status, 'cart':cart, 'order_id':order_id, 'order_id_status':order_id_status}
    return render(request, "orders/orders.html", context)

# This function returns the price of an order.
# It works as an AJAX system.
# The csrf exempt is required here as the CSRF token is not used while making the requests.
@csrf_exempt
def get_price(request):
    order_list = str(request.POST.get('cart-items-get-price'))
    total_price, cart_status = extraFunc.cal_price(order_list)
    price = str(total_price)
    if cart_status is True:
        price_status = True
    else:
        price_status =False
    context = {'price':price, 'price_status':price_status}
    return HttpResponse(json.dumps(context))

# This function renders the order's review page.
def review_order(request):
    user = request.user
    username = str(user.get_username())
    order_id = request.POST.get("order-id")
    order = Orders.objects.get(order_id = order_id)
    price = order.price
    order_status = order.status
    if order_status is True:
        order_status = "COMPLETE"
    else:
        order_status = "PENDING"
    cart = (order.content).split(",")
    order_id_status = True
    context = {'new_order':False, 'price':price, 'order_status':order_status, 'cart':cart, 'order_id':order_id, 'order_id_status':order_id_status}
    return render(request, "orders/orders.html", context)

# This function is used in the Shop's Interface system.
# It returns the last 10 orders which have not been completed yet.
# It works as an AJAX system.
# The csrf exempt is required here as the CSRF token is not used while making the requests.
@csrf_exempt
def get_orders(request):
    orders_status = False
    orders_id = []
    request_type = request.POST.get('get-orders')
    if request_type == 'last_ten':
        orders = Orders.objects.order_by('-order_id').filter(status = False)[:10]
        # It returns the last (newest) 10 orders.
    else:
        orders = False
    if orders is not False:
        for order in orders:
            orders_id.append(order.order_id)
        orders_status = True
    else:
        orders_status = False

    context = {'orders_status':orders_status, 'orders_id':orders_id}

    return HttpResponse(json.dumps(context))

# This function returns an order's information.
# It works as an AJAX system.
# The csrf exempt is required here as the CSRF token is not used while making the requests.
@csrf_exempt
def get_order_info(request):
    order_info_status = False
    price = 0
    content = 0
    order_id = str(request.POST.get('order-id'))
    try:
        order = Orders.objects.get(order_id = order_id)
        price = str(order.price)
        content = order.content.split(',')
        order_status = order.status
        order_info_status = True
    except:
        order_info_status = False
    context = {'order_info_status':order_info_status, 'order_id':order_id, 'price':price,'order_status':order_status, 'content':content}
    return HttpResponse(json.dumps(context))

# This functions is used to mark an order as 'Completed'.
# It works as an AJAX system.
# The csrf exempt is required here as the CSRF token is not used while making the requests.
@csrf_exempt
def complete_order(request):
    completion_status = False
    order_id = str(request.POST.get('order-id'))
    try:
        order = Orders.objects.get(order_id = order_id)
        order.status = True
        order.save()
        completion_status = True
    except:
        completion_status = False
    if completion_status is True:
        context = {'order_status':True}
    else:
        context = {'order_status':False}

    return HttpResponse(json.dumps(context))
