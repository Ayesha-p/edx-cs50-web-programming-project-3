# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

from django.db import models

# Create your models here.

class Regular_pizza(models.Model):
    name = models.CharField(max_length = 100)
    price_small = models.DecimalField(max_digits = 4, decimal_places = 2)
    price_large = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Sicilian_pizza(models.Model):
    name = models.CharField(max_length = 100)
    price_small =models.DecimalField(max_digits = 4, decimal_places = 2)
    price_large = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Toppings(models.Model):
    name = models.CharField(max_length = 40)
    price = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)

    def __str__(self):
        return self.name

class Subs(models.Model):
    name = models.CharField(max_length = 100)
    price_small = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    price_large = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Pasta(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Salads(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Dinner_platters(models.Model):
    name = models.CharField(max_length = 100)
    price_small = models.DecimalField(max_digits = 4, decimal_places = 2)
    price_large = models.DecimalField(max_digits = 4, decimal_places = 2)

    def __str__(self):
        return self.name

class Custom_user(models.Model):
    username = models.CharField(max_length = 200, null = True)
    orders = models.CharField(max_length = 1000, null = True, blank = True)

class Orders(models.Model):
    content = models.CharField(max_length = 800, null = True)
    status = models.BooleanField(default = False)
    order_id = models.CharField(max_length = 100, null = True)
    price = models.CharField(max_length = 10, null = True, blank = True, default = '0')
