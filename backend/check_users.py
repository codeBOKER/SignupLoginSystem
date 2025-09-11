#!/usr/bin/env python3
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append('/home/amr/Desktop/projects/SignupLoginSystem/backend')

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Setup Django
django.setup()

from django.contrib.auth.models import User

print("All users in database:")
users = User.objects.all()
for user in users:
    print(f"Username: {user.username}, Active: {user.is_active}, Staff: {user.is_staff}, Superuser: {user.is_superuser}")

print("\nChecking testuser2 specifically:")
try:
    user = User.objects.get(username='testuser2')
    print(f"Found testuser2 - Active: {user.is_active}")
    print(f"Password hash: {user.password[:20]}...")
except User.DoesNotExist:
    print("testuser2 does not exist")

print("\nChecking admin user:")
try:
    admin = User.objects.get(is_superuser=True)
    print(f"Found admin: {admin.username} - Active: {admin.is_active}")
except User.DoesNotExist:
    print("No admin user found")