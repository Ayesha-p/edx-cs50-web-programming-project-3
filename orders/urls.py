# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.index, name = "index"),
    path("signup/", views.signup_page, name = "signup"),
    path("login/", views.login_page, name = "login"),
    path("logout/", views.logout_page, name = "logout"),
    path("new-account/", views.new_account, name = "new-account"),
    path("account-login/", views.account_login, name = "account-login"),
    path("profile/", views.profile, name = "profile"),
    path("place-order/", views.place_order, name = "place-order"),
    path("get-price/", views.get_price, name = "get-price"),
    path("review-order/", views.review_order, name = "review-order"),
    path("get-orders/", views.get_orders, name = "get-orders"),
    path("get-order-info/", views.get_order_info, name = "get-order-info"),
    path("complete-order/", views.complete_order, name = "complete-order"),
]
