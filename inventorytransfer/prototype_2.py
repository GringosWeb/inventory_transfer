from gsheets import Sheets

import pandas as pd

sheets = Sheets.from_files('./client_secrets.json', './storage.json')

s = sheets['1MiIgBkgAMmuRJEJ9sksxQAXVzPFNUouhEoOvYtEh-Yc']

s.sheets[0].to_csv('inventario.csv', encoding='utf-8', dialect='excel')

inventory = pd.read_csv('./inventario.csv')

inventory_woocommerce = inventory.drop(columns=["pedaso", "Etiquetas", "Categoria", "sub-Categoria", "tre-Categoria", "Categoria 2", "sub-Categoria 2", "tre-Categoria 2"])

inventory_woocommerce.to_csv("./inventario_woocommerce")

