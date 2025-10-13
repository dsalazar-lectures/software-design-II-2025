from user_decorators import User, AdminDecorator, SuperAdminDecorator
from user_permissions import has_permission

def mostrar_permisos(usuario):
    for action in ["view", "edit", "delete"]:
        print(f"- Action: {action} ->", has_permission(usuario, action))

# 5. CLIENT
def _demo():
    user = User("Maria")
    
    print("User:", user.get_info())
    mostrar_permisos(user)

    admin = AdminDecorator(user)
    print("\nAdmin decorator:", admin.get_info())
    mostrar_permisos(admin)

    super_admin = SuperAdminDecorator(admin)
    print("\nSuperAdmin decorator:", super_admin.get_info())
    mostrar_permisos(super_admin)


if __name__ == "__main__":
    _demo()
