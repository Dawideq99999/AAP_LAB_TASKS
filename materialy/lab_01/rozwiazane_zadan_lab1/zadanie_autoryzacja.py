from functools import wraps

# ===== AKTUALNY UŻYTKOWNIK =====
current_user = {"username": "admin", "role": "superuser"}


# ===== DEKORATOR =====
def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") != role:
                raise PermissionError(
                    f"Użytkownik {current_user.get('username')} nie ma wymaganej roli: {role}"
                )
            return func(*args, **kwargs)
        return wrapper
    return decorator


# ===== FUNKCJE TESTOWE =====
@require_role("superuser")
def usun_dane():
    print("Dane zostały usunięte")


@require_role("admin")
def panel_admina():
    print("Panel administratora")


# ===== URUCHOMIENIE =====
usun_dane()      
panel_admina()   