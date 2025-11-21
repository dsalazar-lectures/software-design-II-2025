using Lab3.Emails;

namespace Lab3;

class Program
{
    static void Main(string[] args)
    {
        DailyRecipeEmail recipe = new DailyRecipeEmail("chef@example.com", "Today's Recipe", "Try this pasta.");

        var recipients = new string[]
        {
            "alice@example.com",
            "bob@example.com",
            "carol@example.com"
        };

        foreach (string recipient in recipients)
        {
            var email = recipe.Clone() as DailyRecipeEmail;
            if (email == null)
            {
                throw new NullReferenceException("Cloned email is null or of incorrect type.");
            }
            email.SetRecipient(recipient);
            SendEmail(email);
        }
    }

    static void SendEmail(IEmail email)
    {
        Console.WriteLine($"Sending Email to {email.GetRecipient()} - Subject: {email.GetSubject()}, Body: {email.GetBody()}");
    }
}
