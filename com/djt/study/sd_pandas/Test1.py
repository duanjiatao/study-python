import pandas as pd

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.options.display.precision = 2
pd.options.display.max_colwidth = 50
pd.options.display.expand_frame_repr = False
pd.options.display.show_dimensions = True


def test1():
    print()
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['F', 'M', 'M']}
    df = pd.DataFrame(data)
    print(df)

    print("=" * 50)

    # 创建一个带有行索引和列索引的DataFrame
    df = pd.DataFrame({'name': ['Alice', 'Bob', 'Charlie', 'David'], 'age': [25, 30, 35, 40]},
                      index=['a', 'b', 'c', 'd'])
    print(df)
    print('shape is', df.shape)
    print('size is', df.size)


def test2():
    print()
    # 创建一个Series
    s = pd.Series([1, 2, 3, 4, 5])
    print(s)

    print('=' * 50)
    # 创建一个带有索引的Series
    s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
    print(s)


def test3():
    print()
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['F', 'M', 'M']}
    df = pd.DataFrame(data)
    print(df)
    print('=' * 50)
    print(df.loc[0, 'name'])
    print(df.loc[1, 'age'])
    print(df.loc[:, 'gender'])


def test4():
    print()
    data1 = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 35], 'gender': ['F', 'M', 'M']}
    data2 = {'name': ['David', 'Edward', 'Frank'], 'age': [40, 45, 50], 'gender': ['M', 'M', 'M']}
    df1 = pd.DataFrame(data1)
    df2 = pd.DataFrame(data2)
    print(df1)
    print('=' * 50)
    print(df2)
    print('=' * 50)

    print(pd.concat([df1, df2]))
    print('=' * 50)
    print(pd.merge(df1, df2, on='gender'))
    print('=' * 50)
    print(df1.groupby('gender').mean(True))


def test5():
    print()
    df = pd.read_excel('ebooks.xlsx', sheet_name='Sheet1')
    print(df)
