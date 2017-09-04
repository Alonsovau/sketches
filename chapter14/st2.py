# 在单元测试中给对象打补丁
from unittest.mock import patch


# @patch('example.func')
# def test1(x, mock_func):
#     example.func(x)
#     mock_func.assert_called_with(x)
#
# with patch('example.func') as mock_func:
#     example.func(x)
#     mock_func.assert_called_with(x)
#
# p = patch('example.func')
# mock_func = p.start()
# example.func(x)
# mock_func.assert_called_with(x)
# p.stop()


x = 42
with patch('__main__.x'):
    print(x)
    print(type(x))
print(x)
# 原来的值会在装饰器或上下文管理器完成后自动恢复过来，默认被MagicMock实例替代
with patch('__main__.x', 'patched_value'):
    print(x)
    print(type(x))
print(x)
