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

# Commit the changes to the repository
os.system('git config --global user.name "GitHub Actions"')
os.system('git config --global user.email "actions@github.com"')
os.system('git add version.txt')
os.system(f'git commit -m "Increment version to {new_version}"')
os.system('git push')
