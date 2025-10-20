from abc import ABC, abstractmethod
import UserContext

class IUserState(ABC):
    
    @property
    def context(self):
        return self._context
        
    def context(self, context : UserContext):
        self._context = context
    
    def readRecipe(self, recipe: str):
        print(f"Reading recipe: {recipe}")
        
    @abstractmethod
    def changeState(self):
        pass
    
    @abstractmethod
    def changeStateJump(self):
        pass
        
    @abstractmethod
    def writeRecipe(self, recipe: str):
        pass
        
    @abstractmethod
    def deleteRecipe(self, recipe: str):
        pass