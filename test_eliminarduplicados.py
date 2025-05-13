import pytest

# Function to be tested
def eliminar_duplicados(lista):
    return list(set(lista))

# Test cases
def test_eliminar_duplicados():
    assert eliminar_duplicados([1, 2, 2, 3]) == [1, 2, 3] or eliminar_duplicados([1, 2, 2, 3]) == [3, 1, 2]
    assert eliminar_duplicados([]) == []
    assert eliminar_duplicados([1, 1, 1, 1]) == [1]
    assert eliminar_duplicados([1, 2, 3, 4]) == [1, 2, 3, 4] or eliminar_duplicados([1, 2, 3, 4]) == [4, 3, 2, 1]

if __name__ == "__main__":
    pytest.main()