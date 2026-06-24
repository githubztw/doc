import pandas as pd
# 写入 csv 文件
def write_csv_with_writer():
    # 要写入的数据
    data = [
        ['Alice', 'China', 'Bei jing','test'],
        ['Alice1', 'Japan', 'New York','test'],
        ['Alice2', 'Japan', 'New York','test'],
    ]
    # 列名
    columns = ['name', 'country', 'city', 'skills']
    df = pd.DataFrame(data, columns=columns)
    df.to_csv('./data/csvTest.csv', index=False)
# 读取 csv 文件
def csv_reader():
    df = pd.read_csv('./data/csvTest.csv')
    # 显示数据
    print(df)

write_csv_with_writer()
csv_reader()
    
