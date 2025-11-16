"""
Defines user roles and permissions for the Decorator Pattern demo.

- Assigns numeric levels to roles and permissions.
- Checks if a user's role is high enough to perform a given action.
"""


ROLE_LEVEL = {
    "user": 1,
    "admin": 2,
    "superadmin": 3
}

PERMISSION_LEVEL = {
    "view": 1,
    "edit": 2,
    "delete": 3
}

def highest_role_level(roles):
    highest = 0
    for role in roles:
        level = ROLE_LEVEL.get(role, 0)
        if level > highest:
            highest = level
    return highest


def has_permission(user, action):
    user_level = highest_role_level(user.get_roles())
    level_required = PERMISSION_LEVEL[action]
    return user_level >= level_required
