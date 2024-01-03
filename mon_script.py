import os

# Accéder au secret
secret = os.environ.get('MON_SECRET')

print(f"Le secret est : {secret}")

