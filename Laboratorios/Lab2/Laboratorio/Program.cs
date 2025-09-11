using Microsoft.AspNetCore.Builder;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Hosting;

var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

// GET al root path ("/")
app.MapGet("/", () => "Mensaje GET desde el root path logrado con éxito.");

// Request del POST al root path ("/")
app.MapPost("/", async (HttpContext context) =>
{
    var data = await context.Request.ReadFromJsonAsync<PetRequest>();
    return Results.Ok($"El nombre digitado es: {data?.Name}");
});

// 3. GET con parámetro en la URL
app.MapGet("/petName/{name}", (string name) =>
{
    return $"Su mascota se llama: {name}";
});

app.Run();

public record PetRequest(string Name);
