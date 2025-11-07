from abc import ABC, abstractmethod
from typing import List, Dict, Any

class IMenuCreationMediator(ABC):
    """Mediator interface for menu creation process"""

    @abstractmethod
    def notify(self, sender: str, event: str, data: Any = None) -> None:
        """Notifies the mediator about an event from a component"""
        pass

class MenuCreationMediator(IMenuCreationMediator):
    """
    Mediator that coordinates the menu creation process.
    Manages interactions between RecipeService, ProfileService, and MenuService.
    """

    def __init__(self, recipe_service, profile_service, menu_service):
        self._recipe_service = recipe_service
        self._profile_service = profile_service
        self._menu_service = menu_service
        self._creation_data = {}

    def notify(self, sender: str, event: str, data: Any = None) -> None:
        """Coordinates events from different services"""

        if event == "profile_loaded":
            print(f"Mediator: Profile loaded, getting restrictions...")
            self._creation_data['profile'] = data
            # Notify recipe service about restrictions
            self._load_suitable_recipes(data)

        elif event == "recipes_filtered":
            print(f"Mediator: {len(data)} recipes filtered, creating menu...")
            self._creation_data['recipes'] = data
            # Create menu with filtered recipes
            self._create_menu()

        elif event == "menu_created":
            print(f"Mediator: Menu created successfully!")
            self._creation_data['menu'] = data

    def _load_suitable_recipes(self, profile_data: Dict):
        """Loads suitable recipes based on profile"""
        # Simulates getting filtered recipes
        recipes = self._recipe_service.filter_by_profile(profile_data)
        self.notify("recipe_service", "recipes_filtered", recipes)

    def _create_menu(self):
        """Creates menu with collected data"""
        menu = self._menu_service.create(
            profile=self._creation_data['profile'],
            recipes=self._creation_data['recipes']
        )
        self.notify("menu_service", "menu_created", menu)

    def create_personalized_menu(self, user_id: int) -> Dict:
        """Initiates the personalized menu creation process"""
        print(f"Mediator: Starting menu creation for user {user_id}")

        # Load user profile
        profile = self._profile_service.get_by_user(user_id)
        self.notify("profile_service", "profile_loaded", profile)

        return self._creation_data.get('menu', {})


# Usage example
class SimpleRecipeService:
    def get_all(self):
        return [{"name": "Salad", "id": 1}, {"name": "Pasta", "id": 2}, {"name": "Bread", "id": 3}]

    def filter_by_profile(self, profile):
        if "gluten" in profile.get("restrictions", []):
            # Only salad is gluten-free
            return [self.get_all()[0]]
        return self.get_all()

class SimpleProfileService:
    def get_all(self):
        return [{"user_id": 1, "restrictions": []}, {"user_id": 2, "restrictions": ["gluten"]}]

    def get_by_user(self, user_id: int):
        profiles = self.get_all()
        for profile in profiles:
            if profile['user_id'] == user_id:
                return profile
        return {}

class SimpleMenuService:
    def create(self, profile, recipes):
        return {"profile": profile['user_id'], "recipes_count": len(recipes), "recipes": recipes}


# Demonstration
def demo_mediator():
    recipe_svc = SimpleRecipeService()
    profile_svc = SimpleProfileService()
    menu_svc = SimpleMenuService()

    # Create mediator
    mediator = MenuCreationMediator(recipe_svc, profile_svc, menu_svc)

    # Create personalized menus
    for i in range (1, 3):
        menu = mediator.create_personalized_menu(i)
        print(f"\nResult: {menu}\n")

if __name__ == "__main__":
    demo_mediator()
