# 执行外部命令并获取它的输出
import subprocess


out_bytes = subprocess.check_output(['netstat', '-an'])
out_text = out_bytes.decode('utf-8')
print(out_bytes)
print(out_text)


try:
    out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'])
except subprocess.CalledProcessError as e:
    out_bytes = e.output
    code = e.returncode

out_bytes = subprocess.check_output(['cmd', 'arg1', 'arg2'], stderr=subprocess.STDOUT, timeout=5)
# 默认收集输入到标准输出的值，stderr收集标准输出和错误输出
# timeout超时机制

out_bytes = subprocess.check_output('grep python | wc > out', shell=True)
# 想让shell执行命令


text = b'''
hello world
this is a test
goodbye
'''
p = subprocess.Popen(['wc'], stdout=subprocess.PIPE, stdin=subprocess.PIPE)
stdout, stderr = p.communicate(text)
out = stdout.decode('utf-8')
err = stderr.decode('utf-8')

# 模块对于依赖tty的外部命令不合适用。例如，你不能使用它来自动化一个用户输入密码的任务(比如一个ssh会话)。这时候，你需要使用到第三方模块了，比如基于著名的expect家族的工具(pexpect或类似的)
