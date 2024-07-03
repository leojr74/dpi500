from PIL import Image
import os
from tkinter.filedialog import askdirectory

nome_pasta_selecionada = askdirectory()
lista_arquivos = os.listdir (nome_pasta_selecionada)
for arquivo in lista_arquivos:
    if '.jpg' in arquivo:
        #print (f'{nome_pasta_selecionada}/{arquivo}')
        img = Image.open(f'{nome_pasta_selecionada}/{arquivo}')
        img.save(f'{nome_pasta_selecionada}/{arquivo}', dpi = (500.0, 500.0))
            

