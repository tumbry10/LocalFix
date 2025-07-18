from django.contrib import admin
from .models import Category, Service, Booking, Payment, Review

# Register your models here.
admin.site.register(Category)
admin.site.register(Service)
admin.site.register(Booking)
admin.site.register(Review)
admin.site.register(Payment)