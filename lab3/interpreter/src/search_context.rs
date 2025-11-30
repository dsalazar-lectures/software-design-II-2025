/*
    search_context.rs
    ---------------------------------------------------------------------------
    This file contains what the expressions need to interpret themselves.
    In this case, the supported ingredients by the program.
    
*/

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