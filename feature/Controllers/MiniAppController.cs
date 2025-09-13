using Microsoft.AspNetCore.Mvc;

namespace feature.Controllers
{
    [ApiController]
    [Route("")]
    public class MiniAppController : ControllerBase
    {

        private readonly ILogger<MiniAppController> _logger;

        public MiniAppController(ILogger<MiniAppController> logger)
        {
            _logger = logger;
        }

        [HttpGet]
        public string GetRoot()
        {
            return "Prueba de GET satisfactoria!";
        }

        [HttpPost]
        public string Post([FromBody] TestModel testModel)
        {
            return "Received name: " + testModel.Name;
        }

        [HttpGet("/petName/{petName}")]
        public string GetDoggie(string petName)
        {
            return $"Your pet name is {petName}!"; 
        }
    }
}
