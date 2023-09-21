import csv
import os
import sys
import pandas as pd
from os import system
import time

#from dotenv import load_dotenv
import os
import stanza

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')


# from dotenv import dotenv_values
# load_dotenv()
# ultimo_proceso = os.getenv('FECHA')

os.chdir("/home/eduardo/GCBA/ExpresionBA/Proceso_ExpresionBA/data/")

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

set1 = set(stopwords.words('spanish'))
set2 = set(list(punctuation))
stop_words = set1.union(set2)

"""
pip install stanza
"""


# Leo archivo sacado de una query sql
df_hist= pd.read_csv("Prestaciones_Historicas.csv", encoding='utf-8',index_col=False,sep=';', low_memory=False)

df_hist_unique = df_hist.drop_duplicates()



"""
Funcionamiento / mantenimiento de escaleras mecánicas y ascensores- SUBTE 
unifica 
    "Funcionamiento y mantenimiento de ascensores - SUBTE" 
    "Funcionamiento / mantenimiento de escaleras mecánicas - SUBTE"
"""
col_one_list = df_hist_unique['PRESTACION'].tolist()

if "Funcionamiento y mantenimiento de ascensores - SUBTE" in col_one_list:
    print("esta la prestacion vieja --> Funcionamiento y mantenimiento de ascensores - SUBTE\n\n\n\n")

if "Funcionamiento / mantenimiento de escaleras mecánicas - SUBTE" in col_one_list:
    print("esta la prestacion vieja --> Funcionamiento / mantenimiento de escaleras mecánicas - SUBTE\n\n\n\n\n\n")
    
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Funcionamiento y mantenimiento de ascensores - SUBTE": "Funcionamiento / mantenimiento de escaleras mecánicas y ascensores- SUBTE"})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Funcionamiento / mantenimiento de escaleras mecánicas - SUBTE": "Funcionamiento / mantenimiento de escaleras mecánicas y ascensores- SUBTE"})
    
df_hist_unique = df_hist_unique.drop_duplicates()
   
    
sys.exit()


df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Reubicación de contenedor": "Queja por Contenedores de basura "})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Recolección de residuos fuera del contenedor": "Queja por Contenedores de basura "})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Reparación de contenedor": "Queja por Contenedores de basura "})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Vaciado de contenedor": "Queja por Contenedores de basura "})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Lavado de contenedor": "Queja por Contenedores de basura "})
df_hist_unique.PRESTACION = df_hist_unique.PRESTACION.replace({"Instalación de contenedor": "Queja por Contenedores de basura "})


df_hist_unique = df_hist_unique.drop_duplicates()

df_hist_unique.to_csv('Prestaciones_Historicas_unique.csv', index=False, encoding='utf-8',sep=';')


# Leo csv de Prestaciones Top
df_top= pd.read_csv("Top_Prestaciones.csv", encoding='utf-8',index_col=False,sep=';')
df_top = df_top.drop(['N de Solicitudes'], axis=1)
df_top = df_top.drop(['Categoría'], axis=1)


col_one_list = df_top['Prestacion'].tolist()

contador = 0
# for index, row in df_hist_unique.iterrows():
#     if row['PRESTACION'] in col_one_list:
#         contador = contador +1
#         print(contador)
#         print("encontre" ,row['PRESTACION'])
#     # if row['PRESTACION'] not in col_one_list:
#     #     print("NOOOO encontre" ,row['PRESTACION'])        
        

col_one_list = df_hist_unique['PRESTACION'].tolist()

contador = 0
for index, row in df_top.iterrows():
    # if row['Prestacion'] in col_one_list:
    #     contador = contador +1
    #     print(contador)
    #     print("encontre" ,row['Prestacion'])
    if row['Prestacion'] not in col_one_list:
        print("NOOOO encontre" ,row['Prestacion'])        
        

# Leo csv de Prestaciones Top
df_contenedor= pd.read_csv("Contenedores_Prestaciones.csv", encoding='utf-8',index_col=False,sep=';')
df_contenedor = df_contenedor.drop(['N de Soliciutes'], axis=1)
df_contenedor = df_contenedor.drop(['Categoria'], axis=1)

contador = 0
for index, row in df_contenedor.iterrows():
    # if row['Prestacion'] in col_one_list:
    #     contador = contador +1
    #     print(contador)
    #     print("encontre" ,row['Prestacion'])
    if row[0] not in col_one_list:
        print("---------------NOOOO encontre" ,row[0])        


    if row[0] in col_one_list:
        print("!!!!!!! encontre" ,row[0])                



p = open("Prestaciones_Lematizadas.csv", "w")
linea = 'Prestacion_lematizada'+";"+"Presta_Orig"
p.write(linea+"\n")

with open('Prestaciones_Historicas_unique.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)
    for row in csv_reader:
        prestacion  = str(row[0]).strip()
        prestacion_orig  = str(row[0]).strip()
        
        tokens_prestacion  = (word_tokenize(prestacion))
        filtered_prestacion  = [w for w in tokens_prestacion  if not w.lower() in stop_words]

        lista_prestacion = []
        doc = nlp(' '.join(filtered_prestacion))
        for sent in doc.sentences:
            for word in sent.words:
                print( word.text , word.lemma)
                lista_prestacion.append(word.lemma) 
        
        p.write(' '.join(lista_prestacion)+";"+prestacion_orig+"\n")
       
p.close()       

df = pd.read_excel('Resumen contactos 5-22 a 5-23 Con cuest v3.xlsx', index_col=None)



#df= pd.read_csv("expresion.csv", encoding='utf-8',index_col=False,sep=';', low_memory=False)

df = df.drop(['TIPO'], axis=1)
df = df.drop(['CODIGO'], axis=1)
df = df.drop(['ESTADO_GENERAL'], axis=1)
df = df.drop(['ESTADO'], axis=1)
df = df.drop(['CALLE'], axis=1)
df = df.drop(['ALTURA'], axis=1)
df = df.drop(['CANAL_NOMBRE'], axis=1)
df = df.drop(['ESPACIO_PUBLICO'], axis=1)
df = df.drop(['CIUDADANO_NOMBRE'], axis=1)
df = df.drop(['CIUDADANO_APELLIDO'], axis=1)
df = df.drop(['TIPO_DOC'], axis=1)
df = df.drop(['DOCUMENTO'], axis=1)
df = df.drop(['EMAIL_DE_CONTACTO'], axis=1)
#df = df.drop(['FECHA_INGRESO'], axis=1)
df = df.drop(['HISTORIAL_CAMBIOS'], axis=1)
#df = df.drop(['IDENTIFICADOR'], axis=1)
df = df.drop(['CUESTINARIO'], axis=1)

df['year'] = df['FECHA_INGRESO'].dt.year

df_filtered = df[df['year'] == 2023]

#df = df[df["FECHA_INGRESO"].str.contains("2022") == False]  ## SOLO DEJO AÑO 2023

df_filtered = df_filtered.drop(['FECHA_INGRESO'], axis=1)
df_filtered = df_filtered.drop(['year'], axis=1)

column_to_move = df_filtered.pop("IDENTIFICADOR")
df_filtered.insert(2, "IDENTIFICADOR", column_to_move )



df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Reubicación de contenedor": "Queja por Contenedores de basura "})
df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Recolección de residuos fuera del contenedor": "Queja por Contenedores de basura "})
df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Reparación de contenedor": "Queja por Contenedores de basura "})
df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Vaciado de contenedor": "Queja por Contenedores de basura "})
df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Lavado de contenedor": "Queja por Contenedores de basura "})
df_filtered.PRESTACION = df_filtered.PRESTACION.replace({"Instalación de contenedor": "Queja por Contenedores de basura "})


df_filtered.to_csv('df_reducido.csv', index=False, encoding='utf-8',sep=';')


p = open("Observaciones_Lematizadas.csv", "w")
linea = 'Observa_lematizada'+" ; "+'Observa_Orig' +" ; "+"Presta_Lematizada"+";"+"Presta_Orig"";"+"IDENTIFICADOR"
p.write(linea+"\n")


i = 1
lista_acciones = []
with open('df_reducido.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        id_ = row[2]
        prestacion       = str(row[0]).strip()
        prestacion_orig  = str(row[0]).strip()
        
        #print("prestacion:",prestacion_orig)
        
        prestacion2 = prestacion.replace("/"," / ")
        prestacion = prestacion2
        
        tokens_prestacion  = (word_tokenize(prestacion))
        filtered_prestacion  = [w for w in tokens_prestacion  if not w.lower() in stop_words]

        lista_prestacion = []
        doc = nlp(' '.join(filtered_prestacion))
        for sent in doc.sentences:
            for word in sent.words:
                #print( word.text , word.lemma)
                lista_prestacion.append(word.lemma) 

        
        observacion       = str(row[1]).strip()
        observacion_orig  = str(row[1]).strip()

        #print("observacion:",observacion_orig)
        
        observacion2 = observacion.replace("/"," / ")
        observacion = observacion2
        

        tokens_observacion = (word_tokenize(observacion))
        
        filtered_observacion = [w for w in tokens_observacion if not w.lower() in stop_words]

        i = i+1
        print(i)
        lista_observacion = []
        doc = nlp(' '.join(filtered_observacion))
        for sent in doc.sentences:
            for word in sent.words:
                #print( word.text , word.lemma)
                lista_observacion.append(word.lemma) 

        p.write(' '.join(lista_observacion)+";"+observacion_orig+";"+' '.join(lista_prestacion) +";"+prestacion_orig+";"+id_+"\n")
 
        if len(row)==0:
            break
        
        # if i == 100:
        #     p.close()
        #     break

p.close()



"""
https://www.nltk.org/install.html

import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()

"""


#sys.exit()

# print(stopwords.fileids())
# print(stopwords.words('spanish'))

# sample_lines_tokenized = [word_tokenize(line) for line in sample_lines]

# def remove_stopwords(input_text):
#     return [token for token in input_text if token.lower() not in stopwords.words('english')]

# # Apply stopword function
# tokens_without_stopwords = [remove_stopwords(line) for line in sample_lines_tokenized]



# from nltk.tokenize import sent_tokenize
# text = prestacion
# print(sent_tokenize(text), prestacion)


#tokens_prestacion  = (word_tokenize(prestacion))

#filtered_prestacion  = [w for w in tokens_prestacion  if not w.lower() in stop_words]


#sample_lines_tokenized = [word_tokenize(line) for line in prestacion]
        
# Apply stopword function
#tokens_without_stopwords = [remove_stopwords(line) for line in sample_lines_tokenized]
  

#print(filtered_sentence, observacion)

# import these modules
# from nltk.stem import WordNetLemmatizer
 
# lemmatizer = WordNetLemmatizer()

# from nltk.stem import SnowballStemmer
# spanish_stemmer = SnowballStemmer('spanish')
         

#print(*[f'word: {word.text+" "}\tlemma: {word.lemma}' for sent in doc.sentences for word in sent.words], sep='\n')


# lista_prestacion = []
# doc = nlp(' '.join(filtered_prestacion))
# for sent in doc.sentences:
#     for word in sent.words:
#         #print( word.text , word.lemma)
#         lista_prestacion.append(word.lemma) 

       
#sys.exit()

# lista_prestacion = []
# for k in filtered_prestacion:
#     #print(k+":", spanish_stemmer.stem(k))
#     lista_prestacion.append(spanish_stemmer.stem(k)) 
    
# lista_observacion = []
# for k in filtered_observacion:
#     #print(k+":", spanish_stemmer.stem(k))
#     lista_observacion.append(spanish_stemmer.stem(k)) 


#print(' '.join(lista_observacion))

 
# a denotes adjective in "pos"
#print("better :", lemmatizer.lemmatize("better", pos ="a"))

#sys.exit()          




