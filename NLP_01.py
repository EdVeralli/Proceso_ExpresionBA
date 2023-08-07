import csv
import os
import sys
import pandas as pd
from os import system
import time

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

from dotenv import load_dotenv
import os
import stanza

nlp = stanza.Pipeline(lang='es', processors='tokenize,mwt,pos,lemma')


# from dotenv import dotenv_values
# load_dotenv()
# ultimo_proceso = os.getenv('FECHA')

os.chdir("/home/eduardo/GCBA/ExpresionBA/")

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

set1 = set(stopwords.words('spanish'))
set2 = set(list(punctuation))
stop_words = set1.union(set2)
#sys.exit()

# print(stopwords.fileids())
# print(stopwords.words('spanish'))

# sample_lines_tokenized = [word_tokenize(line) for line in sample_lines]

# def remove_stopwords(input_text):
#     return [token for token in input_text if token.lower() not in stopwords.words('english')]

# # Apply stopword function
# tokens_without_stopwords = [remove_stopwords(line) for line in sample_lines_tokenized]

"""
pip install stanza
"""

#sys.exit()

df_hist= pd.read_csv("Prestaciones_Historicas.csv", encoding='utf-8',index_col=False,sep=';', low_memory=False)

df_hist_unique = df_hist.drop_duplicates()

df_hist_unique.to_csv('Prestaciones_Historicas_unique.csv', index=False, encoding='utf-8',sep=';')

p = open("Lemmas_Prestaciones.csv", "w")
#p.write("Lemma;Tokenizado;Original"+"\n")

with open('Prestaciones_Historicas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    next(csv_reader, None)
    for row in csv_reader:
        prestacion  = str(row[0]).strip()
        prestacion_orig  = str(row[0]).strip()
        
        # prestacion2 = prestacion.replace("/"," / ")
        # prestacion = prestacion2
 
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

df= pd.read_csv("expresion.csv", encoding='utf-8',index_col=False,sep=';', low_memory=False)

# for col in df.columns:
#     print(col)

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
df = df.drop(['FECHA_INGRESO'], axis=1)
df = df.drop(['HISTORIAL_CAMBIOS'], axis=1)

# for col in df.columns:
#     print(col)
df["lista_presta"]=""
df["lista_observa"]=""


df.to_csv('df_reducido.csv', index=False, encoding='utf-8',sep=';')

p = open("Observacion_Lematizadas.csv", "w")
linea = 'Observacion_lematizada'+" ; "+'Observa_Orig' +" ; "+"Presta_Orig"+"\n"
p.write(linea+"\n")


i = 1
lista_acciones = []
with open('df_reducido.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        prestacion       = str(row[1]).strip()
        prestacion_orig  = str(row[1]).strip()
        
        prestacion2 = prestacion.replace("/"," / ")
        prestacion = prestacion2
        
        observacion       = str(row[2]).strip()
        observacion_orig  = str(row[2]).strip()
        
        observacion2 = observacion.replace("/"," / ")
        observacion = observacion2
        
        
        # from nltk.tokenize import sent_tokenize
        # text = prestacion
        # print(sent_tokenize(text), prestacion)
        

        #tokens_prestacion  = (word_tokenize(prestacion))
        tokens_observacion = (word_tokenize(observacion))
        
        filtered_observacion = [w for w in tokens_observacion if not w.lower() in stop_words]
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
        i = i+1
        print(i)
        lista_observacion = []
        doc = nlp(' '.join(filtered_observacion))
        for sent in doc.sentences:
            for word in sent.words:
                #print( word.text , word.lemma)
                lista_observacion.append(word.lemma) 



                
        #sys.exit()
        
        # lista_prestacion = []
        # for k in filtered_prestacion:
        #     #print(k+":", spanish_stemmer.stem(k))
        #     lista_prestacion.append(spanish_stemmer.stem(k)) 
            
        # lista_observacion = []
        # for k in filtered_observacion:
        #     #print(k+":", spanish_stemmer.stem(k))
        #     lista_observacion.append(spanish_stemmer.stem(k)) 
        
        p.write(' '.join(lista_observacion)+";"+observacion_orig+";"+prestacion_orig+"\n")
        #print(' '.join(lista_observacion))

         
        # a denotes adjective in "pos"
        #print("better :", lemmatizer.lemmatize("better", pos ="a"))

        #sys.exit()          

        if len(row)==0:
            break

p.close()










"""
df.to_csv('respuesta_final.csv', index=False, encoding='utf-8',sep=',')
df2 = pd.read_csv("respuesta_final.csv", names=colnames,index_col=False, encoding='utf-8')
df2 = df2.drop(labels=0, axis=0)
df2 = df2.fillna('None')  ## cambio los NaN por 0's
df2.to_csv('Responses.csv', index=False, encoding='utf-8',sep=',')
"""


# # Aislo el organismo emisor de las respuestas
# organismos  = df2[["area", "nombre_preg_codigo"]]
# ## TENGO QUE REEMPLAZAR LAS RESPUESTAS CON LETRAS POR NUMEROS
# codigos = pd.read_csv('libro_codigos_16_06.csv',sep=',', encoding='utf-8')

# codigos2 = {}

# for i in range(len(codigos)):
#       pregunta = codigos.iloc[i]['nombre_pregunta']
#       codigo     = codigos.iloc[i]['codigo']
#       categoria=codigos.iloc[i]['categoria']
#       key, value = pregunta+"-"+categoria, codigo
#       codigos2.update({key: value})

# ### Cargo las reglas de negocio en un vector
# lista_acciones = []
# with open('reglas_10_07.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=';')
#     for row in csv_reader:
#         regla05 = "--------------"  
#         if len(row)==0:
#             break
        
#         regla0= str(row[0]).strip()
#         if "reglas" in regla0:
#                 #print("eludo")
#                 continue
#         if " | " in regla0:
#                 regla0 = regla0.replace(" | ", " or ")
#         if not " ^" in regla0  :
#                     regla03 = "if  ("+regla0
#                     regla04 = regla03.replace(",",".")
#                     guion = regla0.find("_")
#                     resp = regla0[:guion]
#                     regla04 = regla03.replace(" = ", " ): varpunkt_"+resp+" = ")      
#                     regla05 = regla04.replace(",",".")
#                     regla05 = regla05.replace("==1","=='1'")
#                     regla05 = regla05.replace("==2","=='2'")
#                     regla05 = regla05.replace("==3","=='3'")
#                     regla05 = regla05.replace("==4","=='4'")
#                     regla05 = regla05.replace("==5","=='5'")
#                     regla05 = regla05.replace("==99","=='99'")

#                     lista_acciones.append(regla05) 
#                     continue
      
#         if  " ^" in regla0  :
#                     corte = regla0.find(" ^")
#                     trailer = regla0[corte:]
#                     header = regla0[:corte]
#                     trailer = trailer.replace(" ^","")
#                     blanco =  trailer.rfind(" ",1)
#                     token = trailer[:blanco]
#                     asigna = trailer[blanco:]
#                     rearmo = "if  ("+token+" in "+header+" ): varpunkt_"+asigna.strip().replace(".","__")
#                     regla05 = rearmo
#                     regla05 = regla05.replace('"" ' ,'"')
#                     lista_acciones.append(regla05) 
#                     continue
# """
# Reglas de Negocio cargadas.
# """

# f = open("nuevo_df.csv", "w")
# linea = 'fecha'+" ; "+'score' +" ; "+'area' +" ; "+'nombre_preg_codigo'+" ; "+'p1_recop_dat'+" ; "+'p2_bases_dat'+" ; "+'p3_control_base'+" ; "+'p4_integr_dat'+" ; "+'p5_tec_integr_dat'+" ; "+'p6_documen_pol_int'+" ; "+'p7_area_cienc_dat'+" ; "+'p8_apli_tec_ciencia_dat'+" ; "+'p9_herra_vis_dat'+" ; "+'p10_apli_pred'+" ; "+'p11_documen_proy_cie_dat'+" ; "+'p12_tien_report'+" ; "+'p13_act_report'+" ; "+'p14_forma_act_report'+" ; "+'p15_disp_dat'+" ; "+'p16_lect_dat_stand'+" ; "+'p17_api_dat'+" ; "+'p18_norm_prot_dat'+" ; "+'p19_tiemp_dat'+" ; "+'p20_clasif_dat_sens'+" ; "+'p21_dat_sens_consent'+" ; "+'p22_destr_minim_dat'+" ; "+'p23_espac_disc_prot_dat'+" ; "+'p24_lineam_pro_dat'+" ; "+'p25_roles_dat'+" ; "+'p26_polit_uso_dat'+" ; "+'p27_documen_cic_v_dat'+" ; "+'p28_capac_pers_gobern_dat'+" ; "+'p29_report_acc_dat'+" ; "+'p30_sist_acc_info'+" ; "+'p31_revis_cal_dat'+" ; "+'p32_metr_cal_dat'+" ; "+'p33_proc_cal_dat'+" ; "+'p34_per_espec_cal_dat'+" ; "+'p35_interc_dat'+" ; "+'p36_mecan_prop_comp_dat'+" ; "+'p37_pers_espec_reut_dat'+" ; "+'p38_model_dat'+" ; "+'p39_grad_documen_dat'+" ; "+'p40_documen_mod_dat'+" ; "+'p41_pers_espec_model_dat'+" ; "+'sugerencias'
# f.write(linea+"\n")

# for i in df2.index: 
#     linea = df2['fecha'][i]+" ; "+str(codigos2.get('score'+"-"+df2['score'][i]))+";"+str(codigos2.get('area'+"-"+df2['area'][i]))+";"+str(codigos2.get('nombre_preg_codigo'+"-"+df2['nombre_preg_codigo'][i]))+";"+str(codigos2.get('p1_recop_dat'''+"-"+df2['p1_recop_dat'][i]))+";"+str(codigos2.get('p2_bases_dat'+"-"+df2['p2_bases_dat'][i]))+";"+str(codigos2.get('p3_control_base'+"-"+df2['p3_control_base'][i]))+";"+str(codigos2.get('p4_integr_dat'+"-"+df2['p4_integr_dat'][i]))+";"+str(codigos2.get('p5_tec_integr_dat'+"-"+df2['p5_tec_integr_dat'][i]))+";"+str(codigos2.get('p6_documen_pol_int'+"-"+df2['p6_documen_pol_int'][i]))+";"+str(codigos2.get('p7_area_cienc_dat'+"-"+df2['p7_area_cienc_dat'][i]))+";"+str(codigos2.get('p8_apli_tec_ciencia_dat'+"-"+df2['p8_apli_tec_ciencia_dat'][i]))+";"+str(codigos2.get('p9_herra_vis_dat'+"-"+df2['p9_herra_vis_dat'][i]))+";"+str(codigos2.get('p10_apli_pred'+"-"+df2['p10_apli_pred'][i]))+";"+str(codigos2.get('p11_documen_proy_cie_dat'+"-"+df2['p11_documen_proy_cie_dat'][i]))+";"+str(codigos2.get('p12_tien_report'+"-"+df2['p12_tien_report'][i]))+";"+str(codigos2.get('p13_act_report'+"-"+df2['p13_act_report'][i]))+";"+str(codigos2.get('p14_forma_act_report'+"-"+df2['p14_forma_act_report'][i]))+";"+str(codigos2.get('p15_disp_dat'+"-"+df2['p15_disp_dat'][i]))+";"+str(codigos2.get('p16_lect_dat_stand'+"-"+df2['p16_lect_dat_stand'][i]))+";"+str(codigos2.get('p17_api_dat'+"-"+df2['p17_api_dat'][i]))+";"+str(codigos2.get('p18_norm_prot_dat'+"-"+df2['p18_norm_prot_dat'][i]))+";"+str(codigos2.get('p19_tiemp_dat'+"-"+df2['p19_tiemp_dat'][i]))+";"+str(codigos2.get('p20_clasif_dat_sens'+"-"+df2['p20_clasif_dat_sens'][i]))+";"+str(codigos2.get('p21_dat_sens_consent'+"-"+df2['p21_dat_sens_consent'][i]))+";"+str(codigos2.get('p22_destr_minim_dat'+"-"+df2['p22_destr_minim_dat'][i]))+";"+str(codigos2.get('p23_espac_disc_prot_dat'+"-"+df2['p23_espac_disc_prot_dat'][i]))+";"+str(codigos2.get('p24_lineam_pro_dat'+"-"+df2['p24_lineam_pro_dat'][i]))+";"+str(codigos2.get('p25_roles_dat'+"-"+df2['p25_roles_dat'][i]))+";"+str(codigos2.get('p26_polit_uso_dat'+"-"+df2['p26_polit_uso_dat'][i]))+";"+str(codigos2.get('p27_documen_cic_v_dat'+"-"+df2['p27_documen_cic_v_dat'][i]))+";"+str(codigos2.get('p28_capac_pers_gobern_dat'+"-"+df2['p28_capac_pers_gobern_dat'][i]))+";"+str(codigos2.get('p29_report_acc_dat'+"-"+df2['p29_report_acc_dat'][i]))+";"+str(codigos2.get('p30_sist_acc_info'+"-"+df2['p30_sist_acc_info'][i]))+";"+str(codigos2.get('p31_revis_cal_dat'+"-"+df2['p31_revis_cal_dat'][i]))+";"+df2['p32_metr_cal_dat'][i]+";"+str(codigos2.get('p33_proc_cal_dat'+"-"+df2['p33_proc_cal_dat'][i]))+";"+str(codigos2.get('p34_per_espec_cal_dat'+"-"+df2['p34_per_espec_cal_dat'][i]))+";"+str(codigos2.get('p35_interc_dat'+"-"+df2['p35_interc_dat'][i]))+";"+str(codigos2.get('p36_mecan_prop_comp_dat'+"-"+df2['p36_mecan_prop_comp_dat'][i]))+";"+str(codigos2.get('p37_pers_espec_reut_dat'+"-"+df2['p37_pers_espec_reut_dat'][i]))+";"+str(codigos2.get('p38_model_dat'+"-"+df2['p38_model_dat'][i]))+";"+str(codigos2.get('p39_grad_documen_dat'+"-"+df2['p39_grad_documen_dat'][i]))+";"+df2['p40_documen_mod_dat'][i]+";"+str(codigos2.get('p41_pers_espec_model_dat'+"-"+df2['p41_pers_espec_model_dat'][i]))    
#     f.write(linea+"\n")
# f.close()    

# df4 = pd.read_csv("nuevo_df.csv", names=colnames,index_col=False, encoding='utf-8',sep=';')
# del df4['sugerencias']

# print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
# print("*-*-*-*-*-*-*-*-*-*-*-*-**-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

# f = open("Valores.csv", "w")
# p = open("Puntajes.csv", "w")

# titulo_puntaje = 'varpunkt_p1'+';'+'varpunkt_p2'+';'+'varpunkt_p3'+';'+'varpunkt_p4'+';'+'varpunkt_p5'+';'+'varpunkt_p6'+';'+'varpunkt_p7'+';'+'varpunkt_p8'+';'+'varpunkt_p9'+';'+'varpunkt_p10'+';'+'varpunkt_p11'+';'+'varpunkt_p12'+';'+'varpunkt_p13'+';'+'varpunkt_p14'+';'+'varpunkt_p15'+';'+'varpunkt_p16'+';'+'varpunkt_p17'+';'+'varpunkt_p18'+';'+'varpunkt_p19'+';'+'varpunkt_p20'+';'+'varpunkt_p21'+';'+'varpunkt_p22'+';'+'varpunkt_p23'+';'+'varpunkt_p24'+';'+'varpunkt_p25'+';'+'varpunkt_p26'+';'+'varpunkt_p27'+';'+'varpunkt_p28'+';'+'varpunkt_p29'+';'+'varpunkt_p30'+';'+'varpunkt_p31'+';'+'varpunkt_p32__1'+';'+'varpunkt_p32__2'+';'+'varpunkt_p32__3'+';'+'varpunkt_p32__4'+';'+'varpunkt_p32__5'+';'+'varpunkt_p32__6'+';'+'varpunkt_p32__7'+';'+'varpunkt_p32__8'+';'+'varpunkt_p32__9'+';'+'varpunkt_p32__10'+';'+'varpunkt_p33'+';'+'varpunkt_p34'+';'+'varpunkt_p35'+';'+'varpunkt_p36'+';'+'varpunkt_p37'+';'+'varpunkt_p38'+';'+'varpunkt_p39'+';'+'varpunkt_p40__1'+';'+'varpunkt_p40__2'+';'+'varpunkt_p40__3'+';'+'varpunkt_p40__4'+';'+'varpunkt_p40__5'+';'+'varpunkt_p40__6'+';'+'varpunkt_p40__7'+';'+'varpunkt_p40__8'+';'+'varpunkt_p40__9'+';'+'varpunkt_p40__10'+';'+'varpunkt_p41'+';'+'Nulo'
# p.write(titulo_puntaje+"\n")

# lista_noaplica = []

# for i in df4.index: 
#       if i==0:
#           continue

#       for k in varnames:
#           myStr = k
#           myTemplate = "{} = {} " 
#           statement = myTemplate.format(myStr, 0)
#           exec(statement)
#           time.sleep(0.1)
     
#       for j in range(4,45):
#           #print(j)
#           myStr = colnames[j]
#           myVal = df4.iloc[:,j][i]
#           myTemplate = "{} = \"{}\""
#           statement = myTemplate.format(myStr, " ")
#           #print(statement)
#           exec(statement)
     
#       for j in range(4,45):
#           myStr = colnames[j]
#           myVal = df4.iloc[:,j][i]
#           myTemplate = "{} = \"{}\""
#           statement = myTemplate.format(myStr, myVal)
#           f.write(statement+"\n")
         
#           if "-1" in statement:
#               print("***No Aplica..",statement)
#               asacar = statement.replace(' = "-1"',"")
#               lista_noaplica.append(asacar) 
             
#           exec(statement)    
#           for t in lista_acciones:
#               exec(t)

#       for k in varnames:
#           myStr = k
#           myTemplate = "{} = {} " 
#           statement = myTemplate.format(myStr, 0)
#           p.write(str(eval(k))+";")

#       p.write( "\t- "+"\n")       

   
   
# f.close()    
# p.close()    

# """
# Ahora evaluo las puntuaciones por cada linea de respuestas
# """


# final01 = pd.read_csv('Puntajes.csv',sep=';', encoding='utf-8',index_col=False)

# final01.reset_index(drop=True, inplace=True)
# organismos.reset_index(drop=True, inplace=True)


# final02 = final01.join(organismos)

# final03 = final02.drop(['Nulo'], axis=1)
# final03.to_csv('Scores_Totales.csv', index=False, encoding='utf-8',sep=';')


# """
# Aca la lectura de los puntajes , acumular x cada dimension y generar CSV resultados
# """

# p = open("Score_Final.csv", "w")
# Score_Final_titulo = 'Area'+";"+"Organismo"+";"+'Fuente de información/Integración'+';'+'Ciencia de datos'+';'+'Actualidad de Reportes/productos'+';'+'Disponibilización'+';'+'Protección de datos'+";"+'Gobernanza de datos'+';'+'Gestión de acceso a datos'+';'+'Calidad de los datos'+';'+'Reutilización de datos'+';'+'Modelo de datos'
# p.write(Score_Final_titulo+"\n")


# var_dim1 = ['p1_recop_dat','p2_bases_dat','p3_control_base','p4_integr_dat','p5_tec_integr_dat','p6_documen_pol_int']
# var_dim2 = ['p7_area_cienc_dat','p8_apli_tec_ciencia_dat','p9_herra_vis_dat','p10_apli_pred','p11_documen_proy_cie_dat']
# var_dim3 = ['p12_tien_report','p13_act_report','p14_forma_act_report']
# var_dim4 = ['p15_disp_dat','p16_lect_dat_stand','p17_api_dat']
# var_dim5 = ['p18_norm_prot_dat','p19_tiemp_dat','p20_clasif_dat_sens','p21_dat_sens_consent','p22_destr_minim_dat','p23_espac_disc_prot_dat','p24_lineam_pro_dat']
# var_dim6 = ['p25_roles_dat','p26_polit_uso_dat','p27_documen_cic_v_dat','p28_capac_pers_gobern_dat']
# var_dim7 = ['p29_report_acc_dat','p30_sist_acc_info']
# var_dim8 = ['p31_revis_cal_dat','p32_metr_cal_dat','p33_proc_cal_dat','p34_per_espec_cal_dat']
# var_dim9 = ['p35_interc_dat','p36_mecan_prop_comp_dat','p37_pers_espec_reut_dat']
# var_dim10 = ['p38_model_dat','p39_grad_documen_dat','p40_documen_mod_dat','p41_pers_espec_model_dat']

# df_dim = pd.read_csv("Scores_Totales.csv",index_col=False, encoding='utf-8',sep=';')

# noaplica_dim1 = 0
# noaplica_dim2 = 0
# noaplica_dim3 = 0
# noaplica_dim4 = 0
# noaplica_dim5 = 0
# noaplica_dim6 = 0
# noaplica_dim7 = 0
# noaplica_dim8 = 0
# noaplica_dim9 = 0
# noaplica_dim10 = 0

# for k in lista_noaplica:
#     if k in var_dim1:
#         noaplica_dim1 = noaplica_dim1 +1         
#     if k in var_dim2:
#         noaplica_dim2 = noaplica_dim2 +1         
#     if k in var_dim3:
#         noaplica_dim3 = noaplica_dim3 +1         
#     if k in var_dim4:
#         noaplica_dim4 = noaplica_dim4 +1         
#     if k in var_dim5:
#         noaplica_dim5 = noaplica_dim5 +1         
#     if k in var_dim6:
#         noaplica_dim6 = noaplica_dim6 +1         
#     if k in var_dim7:
#         noaplica_dim7 = noaplica_dim7 +1         
#     if k in var_dim8:
#         noaplica_dim8 = noaplica_dim8 +1         
#     if k in var_dim9:
#         noaplica_dim9 = noaplica_dim9 +1         
#     if k in var_dim10:
#         noaplica_dim10 = noaplica_dim10 +1         


# for i in df_dim.index: 
#       sum_dim1 = 0
#       sum_dim2 = 0
#       sum_dim3 = 0
#       sum_dim4 = 0
#       sum_dim5 = 0
#       sum_dim6 = 0
#       sum_dim7 = 0
#       sum_dim8 = 0
#       sum_dim9 = 0
#       sum_dim10 = 0
     
#       sum32 = 0
#       sum40 = 0

     
     
#       for k in varnames:
#           #print(k +"-"+str(df_dim[k][i]))
#           guion =  k.rfind("__")
#           if guion>0:
#               command = k[:guion]
#           else :
#               command = k
         
#           match command:
#               case 'varpunkt_p1':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
#               case 'varpunkt_p2':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
#               case 'varpunkt_p3':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
#               case 'varpunkt_p4':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
#               case 'varpunkt_p5':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
#               case 'varpunkt_p6':
#                   sum_dim1 = sum_dim1 + df_dim[k][i]
                 
#               case 'varpunkt_p7':
#                   sum_dim2 = sum_dim2 + df_dim[k][i]
#               case 'varpunkt_p8':
#                   sum_dim2 = sum_dim2 + df_dim[k][i]
#               case 'varpunkt_p9':
#                   sum_dim2 = sum_dim2 + df_dim[k][i]
#               case 'varpunkt_p10':
#                   sum_dim2 = sum_dim2 + df_dim[k][i]
#               case 'varpunkt_p11':
#                   sum_dim2 = sum_dim2 + df_dim[k][i]
                 
#               case 'varpunkt_p12':
#                   sum_dim3 = sum_dim3 + df_dim[k][i]
#               case 'varpunkt_p13':
#                   sum_dim3 = sum_dim3 + df_dim[k][i]
#               case 'varpunkt_p14':
#                   sum_dim3 = sum_dim3 + df_dim[k][i]
                 
#               case 'varpunkt_p15':
#                   sum_dim4 = sum_dim4 + df_dim[k][i]
#               case 'varpunkt_p16':
#                   sum_dim4 = sum_dim4 + df_dim[k][i]
#               case 'varpunkt_p17':
#                   sum_dim4 = sum_dim4 + df_dim[k][i]
                 
#               case 'varpunkt_p18':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p19':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p20':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p21':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p22':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p23':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
#               case 'varpunkt_p24':
#                   sum_dim5 = sum_dim5 + df_dim[k][i]
                
#               case 'varpunkt_p25':
#                   sum_dim6 = sum_dim6 + df_dim[k][i]
#               case 'varpunkt_p26':
#                   sum_dim6 = sum_dim6 + df_dim[k][i]
#               case 'varpunkt_p27':
#                   sum_dim6 = sum_dim6 + df_dim[k][i]
#               case 'varpunkt_p28':
#                   sum_dim6 = sum_dim6 + df_dim[k][i]
                 
#               case 'varpunkt_p29':
#                   sum_dim7 = sum_dim7 + df_dim[k][i]
#               case 'varpunkt_p30':
#                   sum_dim7 = sum_dim7 + df_dim[k][i]
                 
#               case 'varpunkt_p31':
#                   sum_dim8 = sum_dim8 + df_dim[k][i]
#               case 'varpunkt_p32':
#                   sum32 = sum32 + df_dim[k][i]
#               case 'varpunkt_p33':
#                   sum_dim8 = sum_dim8 + df_dim[k][i]
#               case 'varpunkt_p34':
#                   sum_dim8 = sum_dim8 + df_dim[k][i]
                 
#               case 'varpunkt_p35':
#                   sum_dim9 = sum_dim9 + df_dim[k][i]
#               case 'varpunkt_p36':
#                   sum_dim9 = sum_dim9 + df_dim[k][i]
#               case 'varpunkt_p37':
#                   sum_dim9 = sum_dim9 + df_dim[k][i]
                 
#               case 'varpunkt_p38':
#                   sum_dim10 = sum_dim10 + df_dim[k][i]
#               case 'varpunkt_p39':
#                   sum_dim10 = sum_dim10 + df_dim[k][i]
#               case 'varpunkt_p40':
#                   sum40 = sum40 + df_dim[k][i]
#               case 'varpunkt_p41':
#                   sum_dim10 = sum_dim10 + df_dim[k][i]
                 
#       if sum32 == 1:
#           sum_dim8 = sum_dim8 + 0.7
#       if sum32 == 2:
#           sum_dim8 = sum_dim8 + 0.8
#       if sum32 == 3:
#           sum_dim8 = sum_dim8 + 0.9
#       if sum32 == 4:
#           sum_dim8 = sum_dim8 + 1        
#       if sum32 == 5:
#           sum_dim8 = sum_dim8 + 1.2
#       if sum32 == 6:
#           sum_dim8 = sum_dim8 + 1.3
#       if sum32 == 7:
#           sum_dim8 = sum_dim8 + 1.4
#       if sum32 == 8:
#           sum_dim8 = sum_dim8 + 1.5 
         
         
#       if sum40 == 1:
#           sum_dim10 = sum_dim10 + 0.7
#       if sum40 == 2:
#           sum_dim10 = sum_dim10 + 0.8
#       if sum40 == 3:
#           sum_dim10 = sum_dim10 + 0.9
#       if sum40 == 4:
#           sum_dim10 = sum_dim10 + 1        
#       if sum40 == 5:
#           sum_dim10 = sum_dim10 + 1.2
#       if sum40 == 6:
#           sum_dim10 = sum_dim10 + 1.3
#       if sum40 == 7:
#           sum_dim10 = sum_dim10 + 1.4

#       if sum32 >= 100:
#           sum32 = 0

#       if sum40 >= 100:
#           sum40 = 0

#       total_dim1  = sum_dim1  / (len(var_dim1) - noaplica_dim1)
#       total_dim2  = sum_dim2  / (len(var_dim2) - noaplica_dim2)
#       total_dim3  = sum_dim3  / (len(var_dim3) - noaplica_dim3)
#       total_dim4  = sum_dim4  / (len(var_dim4) - noaplica_dim4)
#       total_dim5  = sum_dim5  / (len(var_dim5) - noaplica_dim5)
#       total_dim6  = sum_dim6  / (len(var_dim6) - noaplica_dim6)
#       total_dim7  = sum_dim7  / (len(var_dim7) - noaplica_dim7)
#       total_dim8  = sum_dim8  / (len(var_dim8) - noaplica_dim8)
#       total_dim9  = sum_dim9  / (len(var_dim9) - noaplica_dim9)
#       total_dim10 = sum_dim10 / (len(var_dim10)- noaplica_dim10)

#       print("dimension 1:"+str(total_dim1))
#       print("dimension 2:"+str(total_dim2))
#       print("dimension 3:"+str(total_dim3))
#       print("dimension 4:"+str(total_dim4))
#       print("dimension 5:"+str(total_dim5))
#       print("dimension 6:"+str(total_dim6))
#       print("dimension 7:"+str(total_dim7))
#       print("dimension 8:"+str(total_dim8))
#       print("dimension 9:"+str(total_dim9))
#       print("dimension 10:"+str(total_dim10))
#       print("-----final de un registro---------------------")

#       p.write(df_dim["area"][i]+";"+df_dim["nombre_preg_codigo"][i]+";"+str(total_dim1)+";"+str(total_dim2)+";"+str(total_dim3)+";"+str(total_dim4)+";"+str(total_dim5)+";"+str(total_dim6)+";"+str(total_dim7)+";"+str(total_dim8)+";"+str(total_dim9)+";"+str(total_dim10)+"\n")       
     

# p.close()    
# print("-----final del Proceso-------------------")