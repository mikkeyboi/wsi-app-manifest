import os
import subprocess

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
subprocess.run(['git', 'config', '--global', 'user.name', 'GitHub Actions'])
subprocess.run(['git', 'config', '--global', 'user.email', 'actions@github.com'])
subprocess.run(['git', 'add', 'version.txt'])
subprocess.run(['git', 'commit', '-m', f'Increment version to {new_version}'])
token = os.getenv('GITHUB_TOKEN')
subprocess.run(['git', 'push', f'https://{token}@github.com/mikkeyboi/webcam_stream_incubation.git'])
