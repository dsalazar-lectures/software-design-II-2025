var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// Un mensaje cualquiera para el GET al root path: / .
app.MapGet("/", () => "Prueba de GET exitosa!");

// Un mensaje que consuma una propiedad del request de un POST al root path: /
app.MapPost("/", async (HttpRequest request) =>
{
    using var reader = new StreamReader(request.Body);
    var body = await reader.ReadToEndAsync();

    var data = System.Text.Json.JsonSerializer.Deserialize<Dictionary<string, string>>(body);

    if (data != null && data.ContainsKey("name"))
    {
        return Results.Ok($"Nombre recibido: {data["name"]}");
    }

    return Results.BadRequest("Falta la propiedad 'name'.");
});

// Un mensaje mostrando un valor que venga en el URL
app.MapGet("/petName/{pet}", (string pet) =>
{
    return $"Tu mascota se llama {pet}";
});

app.Run();
