from django.db import models
from django.utils import timezone

class Cars(models.Model):
    Cars_Types = [    
        ('Toyota', 'Fortuner'),
        ('Toyota', 'Corolla'),
        ('Toyota', 'Camry'),
        ('Toyota', 'Land Cruiser'),
        ('Tata', 'Safari'),
        ('Tata', 'Harrier'),
        ('Tata', 'Nexon'),
        ('Hyundai', 'Santro'),
        ('Hyundai', 'Creta'),
        ('Hyundai', 'Venue'),
        ('Hyundai', 'Elantra'),
        ('Mahindra', 'Scorpio'),
        ('Mahindra', 'Thar'),
        ('Mahindra', 'XUV700'),
        ('Maruti Suzuki', 'Swift'),
        ('Maruti Suzuki', 'Baleno'),
        ('Maruti Suzuki', 'Dzire'),
        ('Honda', 'City'),
        ('Honda', 'Civic'),
        ('Honda', 'CR-V'),
        ('BMW', '3 Series'),
        ('BMW', '5 Series'),
        ('BMW', 'X5'),
        ('Mercedes-Benz', 'C-Class'),
        ('Mercedes-Benz', 'E-Class'),
        ('Mercedes-Benz', 'GLE'),
        ('Audi', 'A4'),
        ('Audi', 'A6'),
        ('Audi', 'Q7'),
        ('Tesla', 'Model S'),
        ('Tesla', 'Model 3'),
        ('Tesla', 'Model X'),
        ('Tesla', 'Model Y'),
        ('Porsche', '911'),
        ('Porsche', 'Cayenne'),
        ('Lamborghini', 'Huracan'),
        ('Lamborghini', 'Aventador'),
        ('Ferrari', '488 GTB'),
        ('Ferrari', 'Portofino'),
        ('Jaguar', 'XF'),
        ('Jaguar', 'F-Pace'),
        ('Land Rover', 'Range Rover'),
        ('Land Rover', 'Defender')
          ]

    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='cars/')
    type = models.CharField(choices=Cars_Types, max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    description = models.TextField(default='')
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"



    