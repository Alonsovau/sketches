# 重新抛出被捕获异常
def example():
    try:
        int('N/A')
    except ValueError:
        print("Didn't work")
        raise


example()