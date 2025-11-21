namespace Lab3.Emails;

public class DailyRecipeEmail : BasicEmail
{
    private string RecipeName { get; set; }
    private string RecipeDetails { get; set; }

    public DailyRecipeEmail(string recipient, string recipeName, string recipeDetails)
        : base(recipient, string.Empty, string.Empty)
    {
        RecipeName = recipeName;
        RecipeDetails = recipeDetails;
    }

    public override IEmail Clone()
    {
        return new DailyRecipeEmail(GetRecipient(), RecipeName, RecipeDetails);
    }

    public override string GetSubject()
    {
        return RecipeName;
    }

    public override string GetBody()
    {
        return RecipeDetails;
    }
}
