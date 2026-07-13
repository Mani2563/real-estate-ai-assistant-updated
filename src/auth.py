import hashlib
import json
import re
from pathlib import Path


USER_DB = Path("users.json")


class AuthManager:

    @staticmethod
    def load_users():

        if not USER_DB.exists():
            USER_DB.write_text("[]")

        with open(USER_DB, "r") as file:
            return json.load(file)

    @staticmethod
    def save_users(users):

        with open(USER_DB, "w") as file:
            json.dump(users, file, indent=4)

    @staticmethod
    def hash_password(password):

        return hashlib.sha256(
            password.encode()
        ).hexdigest()

    @staticmethod
    def validate_password(password):

        pattern = (
            r"^(?=.*[a-z])"
            r"(?=.*[A-Z])"
            r"(?=.*\d)"
            r"(?=.*[@$!%*?&])"
            r"[A-Za-z\d@$!%*?&]{8,12}$"
        )

        return re.match(pattern, password)

    @staticmethod
    def email_exists(email):

        users = AuthManager.load_users()

        return any(
            user["email"].lower() == email.lower()
            for user in users
        )

    @staticmethod
    def register(name, email, password):

        if AuthManager.email_exists(email):

            return False, "Email already registered."

        if not AuthManager.validate_password(password):

            return (
                False,
                "Password must be 8-12 characters and contain uppercase, lowercase, digit and special character."
            )

        users = AuthManager.load_users()

        users.append(
            {
                "name": name,
                "email": email,
                "password": AuthManager.hash_password(password)
            }
        )

        AuthManager.save_users(users)

        return True, "Registration successful."

    @staticmethod
    def login(email, password):

        users = AuthManager.load_users()

        hashed = AuthManager.hash_password(password)

        for user in users:

            if (
                user["email"].lower() == email.lower()
                and user["password"] == hashed
            ):

                return True, user

        return False, None