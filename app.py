import pandas as pd
ubicacion_archivo = 'file/ventas.csv'
output_ubicacion  ='output/ventas_cencosud.csv'
df_data = pd.read_csv(ubicacion_archivo, encoding="latin1", dtype=str, keep_default_na=False)

print(df_data)
df_dat1 =df_data.drop(['CANAL_VTA'],axis = 1)
df_data.to_csv(output_ubicacion, sep='|', index=False, header=False)
