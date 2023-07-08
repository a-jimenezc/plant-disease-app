import pandas as pd

def filter_df_for_plot(df_f, precios, dormitorios, baños, tipo, ciudad, zona):
    '''
    Esta función filtra el df para actualizar la página según el input cambie.
    El contexto de uso es en callbacks de la página dashboards.
    '''
    df_f = df_f.copy()
    df_f = df_f[(df_f['precio'] >= precios[0]) & 
                (df_f['precio'] <= precios[1])]
    df_f = df_f[(df_f['no_dormitorios'] >= dormitorios[0]) & 
                (df_f['no_dormitorios'] <= dormitorios[1])]
    df_f = df_f[(df_f['no_baños'] >= baños[0]) & 
                (df_f['no_baños'] <= baños[1])]
    if tipo:
        df_f = df_f[df_f['tipo_de_propiedad'] == tipo]
    if ciudad:
        df_f = df_f[df_f['ciudad'] == ciudad]
    if zona:
        df_f = df_f[df_f['zona'] == zona]
    return df_f