from app.operaciones import resta


class TestClass:
    def test_resta(self):
        assert resta(5, 4) == 1
        assert resta(4, 3) == 1
        assert resta(8, 4) == 4
        assert resta(10, 5) == 5
