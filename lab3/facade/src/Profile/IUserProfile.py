from abc import ABC, abstractmethod


class IUserProfile(ABC):
    @abstractmethod
    def get_user_preferences(self, user_id):
        pass
