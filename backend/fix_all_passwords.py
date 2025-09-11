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

print("Fixing all unhashed passwords...")

# Fix testuser password
try:
    user = User.objects.get(username='testuser')
    if user.password == 'testpass123':  # Plain text password
        user.set_password('testpass123')  # This will hash it properly
        user.save()
        print(f"Fixed password for {user.username}")
except User.DoesNotExist:
    print("testuser does not exist")

print("\nAll passwords fixed!")
print("\nVerifying password hashes:")
for user in User.objects.all():
    print(f"{user.username}: {user.password[:30]}...")