namespace Lab3.Emails;

public interface IEmail
{
    IEmail Clone();

    void SetRecipient(string recipient);

    string GetRecipient();

    string GetSubject();

    string GetBody();
}
