from IUserState import IUserState

class VisitorState(IUserState):
    def changeState(self):
        print("VisitorState: Changing state to RegisteredUserState.")
        self.context.transition_to(RegisteredUserState())
        
    def changeStateJump(self):
        print("VisitorState: Changing state to AdminState.")
        self.context.transition_to(AdminState())
        
    def writeRecipe(self, recipe: str):
        print(f"VisitorState: Cannot write {recipe}, Permission denied. Visitors cannot write recipes.")
        
    def deleteRecipe(self, recipe: str):
        print(f"VisitorState: Cannot write {recipe}, Permission denied. Visitors cannot delete recipes.")
        
class RegisteredUserState(IUserState):
    def changeState(self):
        print("RegisteredUserState: Changing state to AdminState.")
        self.context.transition_to(AdminState())
        
    def changeStateJump(self):
        print("RegisteredUserState: Changing state to VisitorState.")
        self.context.transition_to(VisitorState())
        
    def writeRecipe(self, recipe: str):
        print(f"RegisteredUserState: Writing recipe: {recipe}")
        
    def deleteRecipe(self, recipe: str):
        print(f"RegisteredUserState: Cannot delete {recipe}, Permission denied. Registered users cannot delete recipes.")
        
class AdminState(IUserState):
    def changeState(self):
        print("AdminState: Changing state to RegisteredUserState.")
        self.context.transition_to(RegisteredUserState())
        
    def changeStateJump(self):
        print("AdminState: Changing state to VisitorState.")
        self.context.transition_to(VisitorState())
        
    def writeRecipe(self, recipe: str):
        print(f"AdminState: Writing recipe: {recipe}")
        
    def deleteRecipe(self, recipe: str):
        print(f"AdminState: Deleting recipe: {recipe}")