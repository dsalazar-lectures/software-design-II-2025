"""
Decorator Pattern demo: User roles and permissions

Run Command:
    python lab3/decorator-pattern/src/demo.py
    
Description:
    - This demo shows the Decorator Pattern using a user role system.
    - The base user has a default role of "user" with basic permissions.
    - Decorators can add new roles like "admin" or "superadmin" with more access.
    - The `has_permission` function checks if the user can perform an action.


Outputs:
    Shows how decorators can be stacked to combine functionalities.
    
    The printed output shows the permissions for each role level:
        User: view -> True, edit/delete -> False
        Admin: view/edit -> True, delete -> False
        SuperAdmin: view/edit/delete -> True
"""

from user_decorators import User, AdminDecorator, SuperAdminDecorator
from user_permissions import has_permission

def show_permissions(usuario):
    for action in ["view", "edit", "delete"]:
        print(f"- Permision: {action} ->", has_permission(usuario, action))

# 5. CLIENT
def _demo():
    user = User("Maria")
    
    print("User (base):", user.get_info())
    show_permissions(user)

    admin = AdminDecorator(user)
    print("\nAdmin decorator applied to User:", admin.get_info())
    show_permissions(admin)
    
    super_admin1 = SuperAdminDecorator(admin)
    print("\nSuperAdmin decorator applied on Admin (User -> Admin -> SuperAdmin):", super_admin1.get_info())
    show_permissions(super_admin1)
    
    super_admin2 = SuperAdminDecorator(user)
    print("\nSuperAdmin decorator applied on User (User -> SuperAdmin):", super_admin2.get_info())
    show_permissions(super_admin2)

if __name__ == "__main__":
    _demo()
