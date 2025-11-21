namespace Lab3.Emails;

public class BasicEmail : IEmail
{
    private string Recipient { get; set; }
    private string Subject { get; set; }
    private string Body { get; set; }

    public BasicEmail(string recipient, string subject, string body)
    {
        Recipient = recipient;
        Subject = subject;
        Body = body;
    }

    public virtual IEmail Clone()
    {
        return new BasicEmail(Recipient, Subject, Body);
    }

    public void SetRecipient(string recipient)
    {
        Recipient = recipient;
    }

    public string GetRecipient()
    {
        return Recipient;
    }

    public virtual string GetSubject()
    {
        return Subject;
    }

    public virtual string GetBody()
    {
        return Body;
    }
}
