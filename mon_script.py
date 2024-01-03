import os

# Accéder au secret
secret = os.environ.get('MON_SECRET')
secret = f'11AA{secret}'

print(f"Le secret est : {secret}")

