from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, blank=True)  # optional Bootstrap icon class

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name
    
class Service(models.Model):
    provider = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'provider'})
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    location = models.CharField(max_length=100)
    available_days = models.JSONField(default=list)  # e.g. ["Monday", "Wednesday"]
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'services'

    def __str__(self):
        return f"{self.title} by {self.provider.username}"
    
class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    seeker = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'role': 'seeker'})
    date = models.DateField()
    time_slot = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'bookings'

    def __str__(self):
        return f"{self.seeker.username} booking {self.service.title} on {self.date}"
    
class Review(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()  # 1 to 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f"Review for {self.booking.service.title} by {self.booking.seeker.username}"
    
class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=10, choices=[('paid', 'Paid'), ('failed', 'Failed')])
    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'payments'

    def __str__(self):
        return f"{self.status.upper()} - {self.amount} for {self.booking}"