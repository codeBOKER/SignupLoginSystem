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

print("Fixing password hashing for users...")

# Fix testuser2 password
try:
    user = User.objects.get(username='testuser2')
    if user.password == 'test2pass123':  # Plain text password
        user.set_password('test2pass123')  # This will hash it properly
        user.save()
        print(f"Fixed password for {user.username}")
    else:
        print(f"Password for {user.username} is already hashed")
except User.DoesNotExist:
    print("testuser2 does not exist")

# Check other users too
for user in User.objects.all():
    # Check if password looks like plain text (no $ symbols which indicate hashing)
    if '$' not in user.password and len(user.password) < 50:
        print(f"Warning: {user.username} may have unhashed password: {user.password}")

print("\nPassword fix complete!")