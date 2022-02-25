from app.operaciones import multiplicacion


class TestClass:
    def test_multiplicacion(self):
        assert multiplicacion(5, 4)
