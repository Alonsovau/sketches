import unittest
from unittest.mock import patch
import io
import chapter14.example2


sample_data = io.BytesIO(b'''\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
''')


class Tests(unittest.TestCase):
    @patch('chapter14.example2.urlopen', return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = chapter14.example2.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p,
                         {
                             'IBM': 91.1,
                             'AA': 13.25,
                             'MSFT': 27.72
                         })
# 还有一点，打补丁时我们使用了example2.urlopen来代替urllib.request.urlopen
# 当你创建补丁的时候，你必须使用它们在测试代码中的名称
# 由于测试代码使用了from urllib.request import urlopen
# 那么dowprices()函数中使用的urlopen()函数实际上就位于example2模块了。


if __name__ == '__main__':
    unittest.main()
