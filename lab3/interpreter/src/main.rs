/*
    main.rs
    ---------------------------------------------------------------------------
    A very small demonstration of the pattern Interpreter in Rust.

    The language to process are the user's search input and an informal grammar
    was defined as follows:

    <search> := <filter_type>?<filter_inclusion/exclusion>?<ingredient>
    <filter_type> := "dinner" | "breakfast" | "dessert" ...
    <filter_inclusion> := "with" <ingredient> ("and" <ingredient>)
    <filter_exclusion> := "without" <ingredient> ("and" <ingredient>)

*/
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
        "chicken".to_string(), 
        "rice".to_string(),
        "egg".to_string(),
        "milk".to_string(),
        "baking powder".to_string(),
        "bread".to_string(),
        "fish".to_string(),
        "potato".to_string(),
        ]);
    
    let requests = ["recipes with chicken and rice", 
                                "dessert without eggs",
                                "breakfast without bread", 
                                "dessert without baking powder", 
                                "recipes with fish",
                                "dinner with potatoes"];

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
