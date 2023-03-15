import json

file_path = r'C:\Users\duanjiatao\Desktop\tmp\testData\data.json'


def test_read():
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件!')
    except LookupError:
        print('指定了未知的编码!')
    except UnicodeDecodeError:
        print('读取文件时解码错误!')


def test_read_line():
    # 通过for-in循环逐行读取
    with open(file_path, mode='r', encoding='utf-8') as f:
        for line in f:
            print(line, end='')

    print('=========================================')

    # 读取文件按行读取到列表中
    with open(file_path, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')


def test_json():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }
    try:
        with open(r'C:\Users\duanjiatao\Desktop\tmp\testData\test_data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    test_json()
