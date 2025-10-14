"""
Decorator Pattern Example: User Roles

- Shows how to add new roles without changing the original User class.
- Each decorator wraps a user and gives extra roles (admin, superadmin).
- Decorator structure: Interface → Concrete Component → Base Decorator → Concrete Decorators.
"""

from abc import ABC, abstractmethod

# 1. INTERFACE (IComponent)
class IUser(ABC):
    
    @abstractmethod
    def get_roles(self):
        """Returns list of roles assigned to user"""
        pass

    @abstractmethod
    def get_info(self):
        """Returns user information"""
        pass


# 2. CONCRETE COMPONENT
class User(IUser):
    
    def __init__(self, username, roles=None):
        self.username = username
        self._roles = roles or ["user"]  # Default role is "user"

    def get_roles(self):
        return self._roles

    def get_info(self):
        return {"username": self.username, 
                "roles": self.get_roles()}
        

# 3. BASE DECORATOR
class UserDecorator(IUser):

    def __init__(self, user: IUser):
        self._user = user  # Reference to the component being decorated

    def get_roles(self):
        return self._user.get_roles()

    def get_info(self):
        info = self._user.get_info()
        info["roles"] = self.get_roles()  # Update roles with decorated roles
        return info


# 4. CONCRETE DECORATORS
class AdminDecorator(UserDecorator):
    
    def get_roles(self):
        base = self._user.get_roles()
        for role in ["admin"]:
            if role not in base:
                base.append(role)
        return base


class SuperAdminDecorator(UserDecorator):

    def get_roles(self):
        base = self._user.get_roles()
        for role in ["admin", "superadmin"]:
            if role not in base:
                base.append(role)            
        return base
