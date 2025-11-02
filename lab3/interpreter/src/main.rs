// Include expression.rs and search_context.rs files
mod expresions;
mod search_context;

use std::collections::HashSet;

use crate::expresions::{IExpression, SearchQuery};
use crate::search_context::SearchContext;

/* 
    --------------------------------------------------
                        Client
    --------------------------------------------------
*/
fn main() {
    let supported_ingredients = HashSet::from([
        "pollo".to_string(), 
        "arroz".to_string(),
        "huevo".to_string(),
        "leche".to_string(),
        "chocolate".to_string(),
        "tofu".to_string()
        ]);
    
    let requests = ["recetas con pollo y arroz", "postre sin huevo",
                                "platos con tofu"];

    let interpreter = SearchQuery::new();

    for r in requests {
        let context = SearchContext {
            text: r.to_string(),
            available_ingredients: supported_ingredients.clone(),
        };
        let result = interpreter.interpret(&context);
        println!("Request: {}", r);
        println!("Resultado: {:?}", result);
    }
}
