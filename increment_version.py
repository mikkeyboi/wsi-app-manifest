import os

# Read the current version from version.txt
with open('version.txt', 'r') as file:
    current_version = file.read().strip()

# Increment the version number
parts = current_version.split('.')
parts[-1] = str(int(parts[-1]) + 1)
new_version = '.'.join(parts)

# Write the new version back to version.txt
with open('version.txt', 'w') as file:
    file.write(new_version)
