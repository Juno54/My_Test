#测试用例命名规范
#文件要以test_开头，或者_test结尾
#类要以Test开头，方法要以test_开头


class Test_caculator:
    @pytest.mark.search
    def test_add(self):
        calc = Caculator()