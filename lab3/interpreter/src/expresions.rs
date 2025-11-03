/*
    expressions.rs
    ---------------------------------------------------------------------------
    These are the expressions that build the tree.
    Ingredient and Type are terminal expressions whereas SearchQuery is 
    non-terminal.

*/


use crate::search_context::SearchContext;
/* 
    --------------------------------------------------
        Interface for the concrete expressions
    --------------------------------------------------
*/ 
pub trait IExpression {
    fn interpret(&self, context: &SearchContext) -> ExpressionResult;
}

// Result posibilities
#[derive(Debug)]
pub enum ExpressionResult {
    Text(String),
    List(Vec<String>),
    None,
}

/* 
    --------------------------------------------------
                Terminal expressions
    --------------------------------------------------
*/

pub struct Ingredient;

impl IExpression for Ingredient {
    fn interpret(&self, context: &SearchContext) -> ExpressionResult {

        let mut found_ingredients = vec![];

        for ingredient in &context.available_ingredients {
            if context.text.contains(ingredient) {
                found_ingredients.push(ingredient.clone());
            }
        }

        return ExpressionResult::List(found_ingredients);
    }
}

pub struct Type;

impl IExpression for Type {
    fn interpret(&self, context: &SearchContext) -> ExpressionResult {

        if context.text.contains("dessert") {
            ExpressionResult::Text("Dessert".into())
        } else if context.text.contains("recipe") {
            ExpressionResult:: Text("General".into())
        } else if context.text.contains("breakfast") {
            ExpressionResult::Text("Breakfast".into())
        } else if context.text.contains("dinner") {
            ExpressionResult::Text("Dinner".into())
        } else {
            ExpressionResult::None
        }
    }
}

/* 
    --------------------------------------------------
            Non-Terminal expressions
    --------------------------------------------------
*/
pub struct SearchQuery {
    pub recipe_type: Type,
    pub ingredient: Ingredient,
}

impl IExpression for SearchQuery {

    fn interpret(&self, context: &SearchContext) -> ExpressionResult {
        let r_type = match self.recipe_type.interpret(context) {
            ExpressionResult::Text(t) => Some(t),
            _ => None,
        };

        let ingredients = match self.ingredient.interpret(context) {
            ExpressionResult::List(v) => v,
            _ => vec![],
        };

        let mut include = vec![];
        let mut exclude = vec![];

        if context.text.contains("without") {
            exclude = ingredients;
        } else if context.text.contains("with") {
            include = ingredients;
        }

        ExpressionResult::Text(format!(
            "type: {:?}, include: {:?}, exclude: {:?}", 
            r_type, include, exclude
        ))

    }
}

// Method to create a SearchQuery("constructor")
impl SearchQuery {
    pub fn new() -> Self {
        Self {
            recipe_type: Type,
            ingredient: Ingredient,
        }   
    }
}