from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

# ----------------------
# Author, Book, Library, Librarian models
# ----------------------

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'
    )
    published_date = models.DateField(default=timezone.now)

    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can change book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title


class Library(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(
        Book,
        related_name='libraries'
    )

    def __str__(self):
        return self.name


class Librarian(models.Model):
    name = models.CharField(max_length=100)
    library = models.OneToOneField(
        Library,
        on_delete=models.CASCADE,
        related_name='librarian'
    )

    def __str__(self):
        return self.name


# ----------------------
# UserProfile for roles
# ----------------------

class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('Librarian', 'Librarian'),
        ('Member', 'Member'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default='Member'
    )

    def __str__(self):
        return f"{self.user} - {self.role}"


# ----------------------
# Signal to auto-create UserProfile
# ----------------------

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)




class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books'
    )
    published_date = models.DateField(default=timezone.now)

    class Meta:
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
