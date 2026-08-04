import alchemy
print("== Alembic 4 ===")
print("Accessing the alchemy module using 'import alchemy'")
print(f"Testing create_air: {alchemy.create_air()}")
try:
    alchemy.create_earth()
except Exception as e:
    print(e)
