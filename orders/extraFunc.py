# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

from .models import Regular_pizza, Sicilian_pizza, Toppings, Pasta, Salads
from .models import Subs, Dinner_platters
from .models import Custom_user, Orders
from django.contrib.auth.models import User
import time

# This function calculates the price of an cart.
# It then returns that price, and the status (any problems or not) of calculation of the price.
# It handles any malacious or unintentional changes made to the cart.
def cal_price(order_list):
    status = True
    total = 0
    if order_list == '' or order_list is None:
        total = 0
        status = True
        return total, status

    order_list = order_list.split(',')
    for order in order_list:
        order = order.split('--')
        try:
            item_name = str(order[0])
            item_type = str(order[1])
            size = str(order[2])
        except:
            item_name = 0
            item_type = 0
            size = 0

        try:
            if size == 'default':
                get_price = item_name + ".objects.filter(name=\"" + item_type + "\")[0].price"
                price = eval(str(get_price))

            elif size is not 'default':
                get_price = item_name + ".objects.filter(name=\"" + item_type + "\")[0].price_" + size
                price = eval(str(get_price))
        except:
            price = 0
            status = False

        total += price

    return total, status


# This function makes an order and returns its ID (order_id).
# This function uses the user's id and the timestamp to create an order's id.

# Anything related to user should not be used in making custom id (eg. Order ids), as it is a bad practice.
# As it might leak sensitive information to a potential attacker/hacker (malacious user).
def make_order(username, cart, price):
    timestamp = int(time.time())
    user_id = (User.objects.get(username = username)).id
    order_id = str(user_id) + "-" + str(timestamp)
    order = Orders(content = cart, order_id = order_id, price = price)
    order.save()
    return order_id

# This function is used to place an order (Saves the order_id in the respective user's object).
# This function does not return anything.
def place_order(username, order_id):
    user = Custom_user.objects.get(username=username)
    user_current_orders = user.orders
    if user_current_orders is None:
        user.orders = order_id
    else:
        user.orders = order_id + "," + user_current_orders
    user.save()
