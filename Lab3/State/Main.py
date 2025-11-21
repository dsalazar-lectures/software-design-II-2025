from UserContext import UserContext
from UserStates import VisitorState

if __name__ == "__main__":
    # Initial state: Visitor
    user = UserContext(VisitorState())
    
    user.readRecipe("Pancakes")
    user.writeRecipe("Waffles")
    user.deleteRecipe("Pancakes")
    
    print("\n------\n")
    
    # Change state to Registered User
    user.changeState()
    
    user.readRecipe("Pancakes")
    user.writeRecipe("Waffles")
    user.deleteRecipe("Pancakes")
    
    print("\n------\n")
    
    # Change state to Admin
    user.changeState()
    
    user.readRecipe("Pancakes")
    user.writeRecipe("Waffles")
    user.deleteRecipe("Pancakes")
    
    print("\n------\n")
    
    # Admin jumps to Visitor state
    user.changeStateJump()
    
    user.readRecipe("Pancakes")
    
    print("\n------\n")
    
    # Visitor jumps to Admin state
    user.changeStateJump()  
    
    user.readRecipe("Pancakes")