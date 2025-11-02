use std::collections::HashSet;

/* 
    --------------------------------------------------
            Necessary context for the search
    --------------------------------------------------
*/
pub struct SearchContext {
    pub text: String,
    pub available_ingredients: HashSet<String>,
}