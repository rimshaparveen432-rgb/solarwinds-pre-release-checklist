import hashlib

def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


file_hash = calculate_hash("app.py")

print("SHA-256 Hash Verification")
print("File: app.py")
print("SHA-256:", file_hash)
