from abc import ABC
import IUserState

class UserContext(ABC):
    _state = None
    
    def __init__(self, state : IUserState):
        self.transition_to(state)
        
    def transition_to(self, state : IUserState):
        print(f"UserContext: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self
        
    # ---- Handlers ----
    
    def changeState(self):
        self._state.changeState()
        
    def changeStateJump(self):
        self._state.changeStateJump()
        
    def readRecipe(self, recipe: str):
        self._state.readRecipe(recipe)
        
    def writeRecipe(self, recipe: str):
        self._state.writeRecipe(recipe)
        
    def deleteRecipe(self, recipe: str):
        self._state.deleteRecipe(recipe)
    
    