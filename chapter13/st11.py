# 给简单脚本增加日志功能
import logging
import logging.config


def main():
    logging.basicConfig(
        filename='app.log',
        level=logging.WARNING,
        format='%(levelname)s: %(asctime)s: %(message)s'
    )
    hostname = 'www.python,org'
    item = 'spam'
    filename = 'data.csv'
    mode = 'r'
    logging.critical('Host %s unknown ', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')
# 日志级别，从上到下依次升高，例如error就生成上面两个


def main2():
    logging.config.fileConfig('logconfig.ini')
    hostname = 'www.python2,org'
    item = 'spam2'
    filename = 'data2.csv'
    mode = 'r'
    logging.critical('Host %s unknown ', hostname)
    logging.error("Couldn't find %r", item)
    logging.warning('Feature is deprecated')
    logging.info('Opening file %r, mode=%r', filename, mode)
    logging.debug('Got here')


if __name__ == '__main__':
    main()
    main2()
# https://docs.python.org/3/howto/logging-cookbook.html
