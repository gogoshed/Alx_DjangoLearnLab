from django.contrib.auth.models import Group, Permission
from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.apps import apps

@receiver(post_migrate)
def create_groups_and_permissions(sender, **kwargs):
    if sender.name == "relationship_app":
        # Define groups
        groups = ["Admins", "Editors", "Viewers"]
        for group_name in groups:
            group, created = Group.objects.get_or_create(name=group_name)

        # Assign permissions
        Book = apps.get_model('relationship_app', 'Book')
        can_view = Permission.objects.get(codename='can_view', content_type__app_label='relationship_app')
        can_create = Permission.objects.get(codename='can_create', content_type__app_label='relationship_app')
        can_edit = Permission.objects.get(codename='can_edit', content_type__app_label='relationship_app')
        can_delete = Permission.objects.get(codename='can_delete', content_type__app_label='relationship_app')

        # Assign to groups
        Group.objects.get(name='Admins').permissions.set([can_view, can_create, can_edit, can_delete])
        Group.objects.get(name='Editors').permissions.set([can_view, can_create, can_edit])
        Group.objects.get(name='Viewers').permissions.set([can_view])
