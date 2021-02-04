import pandas

def get_metadata_indexes(sn="Dataset"):
    # data = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", sheet_name=sn, na_values=['*'])
    df = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", sheet_name=sn, na_values=['*'])
    valor_inicial = None
    valor_final = None
    for index,row in df.iterrows():
        if str(row[0]).startswith("#"):
            if not valor_inicial:
                valor_inicial = index
        elif valor_inicial:
            if not valor_final:
                valor_final = index
        if valor_inicial and valor_final:
            # return (df.iloc[valor_inicial : valor_final, :])
            return valor_inicial,valor_final
    return None


def get_data_indexes(sn="Dataset"):
    df = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", sheet_name=sn, na_values=['*'])
    valor_inicial = None
    valor_final = None
    for index,row in df.iterrows():
        if str(row[0]).startswith("!"):
            if not valor_inicial:
                valor_inicial = index
        elif valor_inicial:
            if not valor_final:
                valor_final = index
        if valor_inicial and valor_final:
            # return (df.iloc[valor_inicial: :, :])
            return valor_inicial,valor_final
    return None

def get_metadata(filename, start_position, end_position):
    # cargame archivo como df a partir de la start_position hasta la end_position
    # return dataframe
    df = pandas.read_excel(filename)
    file_metadata = df.iloc[start_position : end_position, :]
    return file_metadata
    

def get_data(filename, start_position, end_position):
    # cargame archivo como df a partir de la start_position hasta la end_position
    # return dataframe
    df = pandas.read_excel(filename)
    file_data = df.iloc[start_position : :, :]
    return file_data

print(get_metadata_indexes())

# def read_xls(sn="Dataset"):
#     data = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", sheet_name=sn,skiprows=22, na_values=['*'])
#     metadata = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", 
#     sheet_name=sn, skip_footer=3163, na_values=['*'])

#     # data[data.Unnamed.str.startswith("!")]
#     # columns = df.columns
#     # ind = df.index
#     # print(df.shape)
#     print(metadata)


# read_xls()

# skiprows : list-like

# Filas para omitir al principio (indexadas en 0)

# skip_footer : int, predeterminado 0

# Filas al final para omitir (indexadas en 0)
# if __name__ == "__main__":
#     read_xls()

# df = pandas.read_excel("datasets/Park2019-HTGeneExpression_v3.0.xlsx", sheet_name=sn, na_values=['*'])
# for sheet_name in xl.sheet_names:
#   reader = df.parse(sheet_name, chunksize=1000)
#   for chunk in reader:
#       print(chunk)