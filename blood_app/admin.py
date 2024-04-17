from django.contrib import admin

from blood_app.models import *

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Blood_Donation)
admin.site.register(Order)