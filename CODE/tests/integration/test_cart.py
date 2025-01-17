import os
import sys
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'../../src/integration')))

from carts import ShoppingCart













@pytest.fixture
def shoppingCart():
       return ShoppingCart()

@pytest.mark.integration
def test_add_and_remove_shopping_cart(shoppingCart):
    #teste para adicionar
    result = shoppingCart.add_item("Café", 50)
    assert result == "Café added"
    
    #test para remover
    remove_result = shoppingCart.remove_item("Café")
    assert remove_result == "Café removed"