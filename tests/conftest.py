import pytest

from src.classes import Category, Product


@pytest.fixture
def product_item() -> Product:
        return Product("Samsung s20", "Смартфон корейский", 80000, 20)


@pytest.fixture
def category_item() -> Category:
    products = [Product("Samsung QLED", "4K TV", 50000, 5)]
    return Category("Телевизоры", "Устройство отображения фильмов и тв-передач", products)