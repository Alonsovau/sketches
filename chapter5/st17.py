# 将字节写入文本文件
import sys
# sys.stdout.write(b'hello\n')
sys.stdout.buffer.write(b'hello\n')