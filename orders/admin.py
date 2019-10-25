# Copyright (C) 2019 OM SANTOSHKUMAR MASNE. All Rights Reserved.
# Licensed under the GNU Affero General Public License v3.0 only (AGPL-3.0-only) license.
# See License.txt in the project root for license information.

from django.contrib import admin

from .models import Regular_pizza, Sicilian_pizza, Toppings
from .models import Subs, Pasta, Salads, Dinner_platters

from .models import Custom_user, Orders

# Register your models here.

admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Toppings)
admin.site.register(Subs)
admin.site.register(Pasta)
admin.site.register(Salads)
admin.site.register(Dinner_platters)

admin.site.register(Custom_user)
admin.site.register(Orders)
