import pandas

def create_excel(lista_vagas):
    try:
        dataframe_vagas = pandas.DataFrame(lista_vagas)
        dataframe_vagas.to_excel("compilado_vagas.xlsx",index=False,header=False)
        return "compilado_vagas.xlsx"
    except Exception as dataframeError:
        print("Erro ao criar o dataframe."+str(dataframeError))
        return None