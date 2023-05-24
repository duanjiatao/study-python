import json

import toml

config = toml.load('config.toml')


def test_conf():
    """
    测试读取toml配置文件
    :return:
    """
    print()

    print(json.dumps(config, indent=4, ensure_ascii=False))
    print('=' * 20)
    db_test = config['databases']['test']
    print('name =', db_test['name'])
    print('host =', db_test['host'])
    print('port =', db_test['port'])
    print('username =', db_test['username'])
    print('password =', db_test['password'])
    print('ss =', db_test['ss'])
