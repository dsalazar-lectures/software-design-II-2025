from data.ingredient_source import IngredientSource
from proxies.ingredient_source_proxy import IngredientSourceProxy
from app.client import request_ingredient


def main() -> None:
    proxy = IngredientSourceProxy(real_or_factory=lambda: IngredientSource())

    request_ingredient(proxy, "Butter")
    request_ingredient(proxy, "Butter")  # cache

    request_ingredient(proxy, "Milk")
    request_ingredient(proxy, "Milk")  # cache

    request_ingredient(proxy, "Yeast")
    request_ingredient(proxy, "Yeast")  # cache


if __name__ == "__main__":
    main()
