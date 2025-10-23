from Profile.IUserProfile import IUserProfile


class UserProfile(IUserProfile):
    # Implementación simulada de acceso a perfiles de usuario
    def get_user_preferences(self, user_id):
        print(f"Obteniendo preferencias del usuario {user_id}")
        return {"diet": "vegetariano", "allergies": ["gluten"]}
