import pandas as pd
def write_excel_with_pandas():
    # 要写入的数据
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'San Francisco', 'Seattle']
    }
    # 创建 DataFrame
    df = pd.DataFrame(data)
    # 写入 Excel 文件
    df.to_excel('./data/example_pandas.xlsx', index=False)
    
def read_excel_with_pandas():
    # 读取 Excel 文件
    df = pd.read_excel('./data/example_pandas.xlsx')
    print(type(df))
    # 显示数据
    print(df)
    
write_excel_with_pandas()
read_excel_with_pandas()