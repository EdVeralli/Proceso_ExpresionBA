import csv
import os
import sys
import pandas as pd
from os import system
import time


from dotenv import load_dotenv
import os

# from dotenv import dotenv_values
# load_dotenv()
# ultimo_proceso = os.getenv('FECHA')


"""
PONER EN Prestaciones_Lematizadas.csv   Campanas Verdes  --- todo en minuscula, porque asi No la tomo

https://midu.dev/como-deshacer-el-ultimo-commit-git/
git reset --soft HEAD~1

"""




las_top = ["Reparación de vereda","Poda de árbol/despeje de luminaria o semáforo","Reparación de luminaria apagada durante la noche", \
"Mejora de barrido","Propuestas para la mejora en trámites","Extracción de árbol","Plantación de árbol","Desratizar, desinsectar y desinfectar en vía pública", \
"Falta de recolección de restos de poda de arbolado público",\
"Mayor presencia policial",\
"Inconvenientes con trámites",\
"Criaderos de mosquitos",\
"Reparación de luminaria por artefacto roto",\
"Hidrolavado por grafitis/pegatinas",\
"Funcionamiento / mantenimiento de escaleras mecánicas y ascensores- SUBTE",\
"Ocupación indebida de la vereda/calzada por local comercial",\
"Inconvenientes en Hospital Público",\
"Reparación de rampa de accesibilidad",\
"Ocupación indebida por mantero o vendedor ambulante",\
"Vereda sucia por mascotas",\
"Inconvenientes con el personal - SUBTE",\
"Refugio de transporte en mal estado o abandonado",\
"Queja por Contenedores de basura "]




os.chdir("/home/eduardo/GCBA/ExpresionBA/Proceso_ExpresionBA/data/")

f = open("Scores.csv", "w")
linea = 'Observacion'+";"+'prestacion_propuesta' +" ; "+'encontro' +" ; "+'total'+" ; "+'%'+" ; "+'PrestaTestigo_Lemma'+" ; "+'PrestaTestigo_Original'+" ; "+'Id_Original'
f.write(linea+"\n")

f2 = open("Scores_small.csv", "w")
linea = 'Observacion'+" ; "+'prestacion_propuesta' +" ; "+'encontro' +" ; "+'total'+" ; "+'%'+" ; "+'PrestaTestigo_Lemma'+" ; "+'PrestaTestigo_Original'+" ; "+'Id_Original'
f2.write(linea+"\n")

f4 = open("Prestaciones_Lematizadas_limpio.csv", "w")   ## pongo en lowercase
linea = 'Prestacion_Lemma'+" ; "+'Prestacion' 
f4.write(linea+"\n")

f5 = open("Scores_small_50Percent.csv", "w")
linea = 'Observacion'+" ; "+'prestacion_propuesta' +" ; "+'encontro' +" ; "+'total'+" ; "+'%'+" ; "+'PrestaTestigo_Lemma'+" ; "+'PrestaTestigo_Original'+" ; "+'Id_Original'
f5.write(linea+"\n")

f6 = open("Scores_small_40Percent.csv", "w")
linea = 'Observacion'+" ; "+'prestacion_propuesta' +" ; "+'encontro' +" ; "+'total'+" ; "+'%'+" ; "+'PrestaTestigo_Lemma'+" ; "+'PrestaTestigo_Original'+" ; "+'Id_Original'
f6.write(linea+"\n")


i = 0
with open('Prestaciones_Lematizadas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        #print(row[0])
        i = i+1
        if i == 1:
            continue
        lista__stemm = list(row[0].split(" "))
        lista_lemma_presta_stemm = []
        for k in lista__stemm:
            if k[-1]== "o" or k[-1]== "a" or k[-1]== "ó" or k[-1]=="á":
                k2 = k[:-1]
                #print("***************",k)
            else:
                k2 = k
            lista_lemma_presta_stemm.append(k2) 
        #print("**************")
        #print(row[0])
        stemm = ' '.join(lista_lemma_presta_stemm)
        #print(stemm)
        #sys.exit()
        f4.write(stemm.lower()+";"+row[1]+"\n")
           
f4.close()


#sys.exit()

f3 = open("Observaciones_Lematizadas_limpio.csv", "w")  ## pongo en lowercase
linea = 'Observa_Lemma'+" ; "+'Observa' +" ; "+'Presta_Lemma_Clasificada' +" ; "+'Presta_Clasificada'+";"+"ID_orig"
f3.write(linea+"\n")
i = 0

#df = pd.read_csv('Observaciones_Lematizadas.csv', delimiter=';')
#sys.exit()

with open('Observaciones_Lematizadas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        #print(row[0])
        i = i+1
        #row[0] = row[0].replace("'","")
        #row[0] = row[0].replace("‘","")
        el_ide = row[4]
        
        if len(row[0])== 0:
            #print("vacio",row[0])
            continue
        #sys.exit()
        #print(i,row[0])
        if i> 2 and (i<34000 or i > 35000):
            lista__stemm = list(row[0].split(" "))
            lista_lemma_observa_stemm = []
            for k in lista__stemm:
                if len(k)>1:
                    if (k[-1]== "o" or k[-1]== "a" or k[-1]== "ó" or k[-1]=="á"):
                        k2 = k[:-1]
                    else:
                        k2 = k
                else:
                    k2 = k
                    
                lista_lemma_observa_stemm.append(k2) 
            #print("**************")
            #print(row[0])
            #print("-----------------------------")
            lista__stemm = list(row[2].strip().split(" "))
            lista_lemma_presta_old_stemm = []
            for k in lista__stemm:
                if len(k)>1:
                    if k[-1]== "o" or k[-1]== "a" or k[-1]== "ó" or k[-1]=="á":
                        k2 = k[:-1]
                        #print("***************",k)
                    else:
                        k2 = k
                else:
                     k2 = k
                     
                lista_lemma_presta_old_stemm.append(k2) 
     




            old_presta =  ' '.join(lista_lemma_presta_old_stemm)
            stemm = ' '.join(lista_lemma_observa_stemm)
            #print(stemm)            
            f3.write(stemm.lower()+";"+row[1]+";"+old_presta+";"+row[3]+";"+el_ide+"\n")
            
        

#sys.exit()
           

df_lemmas_historico_observa = pd.read_csv('Observaciones_Lematizadas_limpio.csv',sep=';', encoding='utf-8')  ## son las 558 MIL
df_lemmas_historico_observa.dropna(inplace = True) ## elimino rows con NaN  ## son las 558 MIL
#df_lemmas_historico_observa=df_lemmas_historico_observa.drop(df_lemmas_historico_observa.columns[1], axis=1)

df_lemmas_prestaciones = pd.read_csv('Prestaciones_Lematizadas_limpio.csv',sep=';', encoding='utf-8',header=None)  ## son las 289 Prestaciones
df_lemmas_prestaciones.dropna(inplace = True) ## elimino rows con NaN  ## son las 289 Prestaciones
#df_lemmas_prestaciones=df_lemmas_prestaciones.drop(df_lemmas_prestaciones.columns[1], axis=1)
#df_lemmas_prestaciones=df_lemmas_prestaciones.drop(df_lemmas_prestaciones.columns[1], axis=1)

lista_acciones = []

count = 0
for index, row in df_lemmas_historico_observa.iterrows():  ## son las 558 MIL
    lista__observacion = list(row[0].split(" "))
    el_ide = row[4]
    if row[0].find(";")>0:
        #print(row[0])
        #sys.exit()
        continue
    
    #print(row[3])
    if row[3] not in las_top:
        #print("No esta en las top ", row[3])
        #sys.exit()
        continue
    
    count = count+1
    print(count,"\n")
    for index2, row2 in df_lemmas_prestaciones.iterrows():  ## son las 289 Prestaciones
        #print("row2[0]",row2[0])

        palabras = row2[0]  ## en palabras tengo los token de una prestacion
        #print(palabras,"***\n")
        lista__prestacion = list(palabras.split(" "))
        ## veo si alguna palabra de esa lista esta en Lista_observacion
        #sys.exit()
        cant_presta = 0
        cant_encontro = 0
        for k in lista__prestacion:
            cant_presta = cant_presta + 1
            if k in lista__observacion:
                cant_encontro = cant_encontro +1
                #print("encontre prestacion :'"+k+"' en observaciones: '"+' '.join(lista__observacion))
        if cant_encontro>0 and count <= 5000:
            score = (cant_encontro/cant_presta)*100
            id_obs = str(count).rjust(6, "0")
            f2.write(row[0]+";"+palabras+";"+str(cant_encontro)+";"+str(cant_presta)+";"+str(round(score))+";"+row[2]+";"+row[3]+";"+el_ide+"\n")

        if (cant_encontro/cant_presta)*100 >= 50:
            score = (cant_encontro/cant_presta)*100
            id_obs = str(count).rjust(6, "0")
            f5.write(row[0]+";"+palabras+";"+str(cant_encontro)+";"+str(cant_presta)+";"+str(round(score))+";"+row[2]+";"+row[3]+";"+el_ide+"\n")

        if (cant_encontro/cant_presta)*100 >= 40:
            score = (cant_encontro/cant_presta)*100
            id_obs = str(count).rjust(6, "0")
            f6.write(row[0]+";"+palabras+";"+str(cant_encontro)+";"+str(cant_presta)+";"+str(round(score))+";"+row[2]+";"+row[3]+";"+el_ide+"\n")

        
        if count == 5002:
           f2.close()
           
        if cant_encontro>0:
            score = (cant_encontro/cant_presta)*100
            id_obs = str(count).rjust(6, "0")
            f.write(row[0]+";"+palabras+";"+str(cant_encontro)+";"+str(cant_presta)+";"+str(round(score))+";"+row[2]+";"+row[3]+";"+el_ide+"\n")

    f6.write("****"+";"+"****"+";"+"********"+";"+"*******"+";"+"*******"+";"+"******"+";"+"****"+";"+el_ide+"\n")
    #f2.write("****"+";"+"****"+";"+"********"+";"+"*******"+";"+"*******"+";"+"******"+";"+"****"+";"+el_ide+"\n")
    f5.write("****"+";"+"****"+";"+"********"+";"+"*******"+";"+"*******"+";"+"******"+";"+"****"+";"+el_ide+"\n")


f.close()
f2.close()
f3.close()
f5.close()
f6.close()




"""

with open('Lemmas_Prestaciones_Historicas_unique.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')  ## son las 289 Prestaciones
    for row in csv_reader:
        
        lista__prestacion = list(row[0].split(" "))
        
        
        for k in lista__prestacion:
            for index, row in df_lemmas_historico.iterrows():  ## son las 558 MIL
                #print("row[0]",row[0])
                lista__observacion = list(row[0].split(" "))
                if k in lista__observacion:
                   print("encontre prestacion :'"+k+"' en observaciones: '"+' '.join(lista__observacion))
                   #sys.exit()
    
                        
                
            
            
            # with open('Lemmas_procesado.csv') as csv_file:
            #     csv_reader = csv.reader(csv_file, delimiter=';')
            #     for row2 in csv_reader:
            #         print("x aca paso----------------------------------------")
            #         lista_prestacion = list(row[0].split(" "))
            #         if k in lista_prestacion:
            #             print("encontre token :"+k+" en: "+' '.join(lista_prestacion)[:50])
            #             #sys.exit()
            
            
            
#         regla05 = "--------------"  
#         if len(row)==0:
#             break
        
#         regla0= str(row[0]).strip()
#         if "reglas" in regla0:
#                #print("eludo")
#                continue
#         if " | " in regla0:
#                regla0 = regla0.replace(" | ", " or ")
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
#      if i==0:
#          continue

#      for k in varnames:
#          myStr = k
#          myTemplate = "{} = {} " 
#          statement = myTemplate.format(myStr, 0)
#          exec(statement)
#          time.sleep(0.1)
     
#      for j in range(4,45):
#          #print(j)
#          myStr = colnames[j]
#          myVal = df4.iloc[:,j][i]
#          myTemplate = "{} = \"{}\""
#          statement = myTemplate.format(myStr, " ")
#          #print(statement)
#          exec(statement)
     
#      for j in range(4,45):
#          myStr = colnames[j]
#          myVal = df4.iloc[:,j][i]
#          myTemplate = "{} = \"{}\""
#          statement = myTemplate.format(myStr, myVal)
#          f.write(statement+"\n")
         
#          if "-1" in statement:
#              print("***No Aplica..",statement)
#              asacar = statement.replace(' = "-1"',"")
#              lista_noaplica.append(str(i-1)+"-"+asacar) 
             
#          exec(statement)    
#          for t in lista_acciones:
#              exec(t)

#      for k in varnames:
#          myStr = k
#          myTemplate = "{} = {} " 
#          statement = myTemplate.format(myStr, 0)
#          p.write(str(eval(k))+";")

#      p.write( "\t- "+"\n")       

   
   
# f.close()    
# p.close()    


# #sys.exit()
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

# #print(df_dim.index,"///////////")
    
# for i in df_dim.index: 
#     #print(i,"la i")

#     noaplica_dim1 = 0
#     noaplica_dim2 = 0
#     noaplica_dim3 = 0
#     noaplica_dim4 = 0
#     noaplica_dim5 = 0
#     noaplica_dim6 = 0
#     noaplica_dim7 = 0
#     noaplica_dim8 = 0
#     noaplica_dim9 = 0
#     noaplica_dim10 = 0
    
#     lista_noaplica2 = []
#     for u in lista_noaplica:
#         #print(u,"ññññññññññññ")
#         lugar = u.find("-")
#         fila = int(u[:lugar])
#         token = u[lugar+1:]
#         #print(token,"pppppppppppp")       
#         #print(fila,"999999999999999")
#         if fila == i:
#             lista_noaplica2.append(token.strip())    

#     for k in lista_noaplica2:
#         if k in var_dim1:
#             noaplica_dim1 = noaplica_dim1 +1         
#         if k in var_dim2:
#             noaplica_dim2 = noaplica_dim2 +1         
#         if k in var_dim3:
#             noaplica_dim3 = noaplica_dim3 +1         
#         if k in var_dim4:
#             noaplica_dim4 = noaplica_dim4 +1         
#         if k in var_dim5:
#             noaplica_dim5 = noaplica_dim5 +1         
#         if k in var_dim6:
#             noaplica_dim6 = noaplica_dim6 +1         
#         if k in var_dim7:
#             noaplica_dim7 = noaplica_dim7 +1         
#         if k in var_dim8:
#             noaplica_dim8 = noaplica_dim8 +1         
#         if k in var_dim9:
#             noaplica_dim9 = noaplica_dim9 +1         
#         if k in var_dim10:
#             noaplica_dim10 = noaplica_dim10 +1         
    
    
#     sum_dim1 = 0
#     sum_dim2 = 0
#     sum_dim3 = 0
#     sum_dim4 = 0
#     sum_dim5 = 0
#     sum_dim6 = 0
#     sum_dim7 = 0
#     sum_dim8 = 0
#     sum_dim9 = 0
#     sum_dim10 = 0
    
#     sum32 = 0
#     sum40 = 0
   
    
#     varnames = ['varpunkt_p1','varpunkt_p2','varpunkt_p3','varpunkt_p4','varpunkt_p5','varpunkt_p6','varpunkt_p7','varpunkt_p8','varpunkt_p9','varpunkt_p10','varpunkt_p11','varpunkt_p12','varpunkt_p13','varpunkt_p14','varpunkt_p15','varpunkt_p16','varpunkt_p17','varpunkt_p18','varpunkt_p19','varpunkt_p20','varpunkt_p21','varpunkt_p22','varpunkt_p23','varpunkt_p24','varpunkt_p25','varpunkt_p26','varpunkt_p27','varpunkt_p28','varpunkt_p29','varpunkt_p30','varpunkt_p31','varpunkt_p32__1','varpunkt_p32__2','varpunkt_p32__3','varpunkt_p32__4','varpunkt_p32__5','varpunkt_p32__6','varpunkt_p32__7','varpunkt_p32__8','varpunkt_p32__9','varpunkt_p32__10','varpunkt_p33','varpunkt_p34','varpunkt_p35','varpunkt_p36','varpunkt_p37','varpunkt_p38','varpunkt_p39','varpunkt_p40__1','varpunkt_p40__2','varpunkt_p40__3','varpunkt_p40__4','varpunkt_p40__5','varpunkt_p40__6','varpunkt_p40__7','varpunkt_p40__8','varpunkt_p40__9','varpunkt_p40__10','varpunkt_p41']
#     for k in varnames:
#         #print(k +"-"+str(df_dim[k][i]))
#         guion =  k.rfind("__")
#         if guion>0:
#             command = k[:guion]
#         else :
#             command = k
    
#         print(k,"k")
#         print(i,"i")
#         print(df_dim[k][i],"df_dim[k][i]")
#         print("***************************")
#         #sys.exit()
        
        
#         match command:
#             case 'varpunkt_p1':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
#             case 'varpunkt_p2':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
#             case 'varpunkt_p3':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
#             case 'varpunkt_p4':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
#             case 'varpunkt_p5':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
#             case 'varpunkt_p6':
#                 sum_dim1 = sum_dim1 + df_dim[k][i]
                
#             case 'varpunkt_p7':
#                 sum_dim2 = sum_dim2 + df_dim[k][i]
#             case 'varpunkt_p8':
#                 sum_dim2 = sum_dim2 + df_dim[k][i]
#             case 'varpunkt_p9':
#                 sum_dim2 = sum_dim2 + df_dim[k][i]
#             case 'varpunkt_p10':
#                 sum_dim2 = sum_dim2 + df_dim[k][i]
#             case 'varpunkt_p11':
#                 sum_dim2 = sum_dim2 + df_dim[k][i]
                
#             case 'varpunkt_p12':
#                 sum_dim3 = sum_dim3 + df_dim[k][i]
#             case 'varpunkt_p13':
#                 sum_dim3 = sum_dim3 + df_dim[k][i]
#             case 'varpunkt_p14':
#                 sum_dim3 = sum_dim3 + df_dim[k][i]
                
#             case 'varpunkt_p15':
#                 sum_dim4 = sum_dim4 + df_dim[k][i]
#             case 'varpunkt_p16':
#                 sum_dim4 = sum_dim4 + df_dim[k][i]
#             case 'varpunkt_p17':
#                 sum_dim4 = sum_dim4 + df_dim[k][i]
                
#             case 'varpunkt_p18':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p19':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p20':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p21':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p22':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p23':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
#             case 'varpunkt_p24':
#                 sum_dim5 = sum_dim5 + df_dim[k][i]
               
#             case 'varpunkt_p25':
#                 sum_dim6 = sum_dim6 + df_dim[k][i]
#             case 'varpunkt_p26':
#                 sum_dim6 = sum_dim6 + df_dim[k][i]
#             case 'varpunkt_p27':
#                 sum_dim6 = sum_dim6 + df_dim[k][i]
#             case 'varpunkt_p28':
#                 sum_dim6 = sum_dim6 + df_dim[k][i]
                
#             case 'varpunkt_p29':
#                 sum_dim7 = sum_dim7 + df_dim[k][i]
#             case 'varpunkt_p30':
#                 sum_dim7 = sum_dim7 + df_dim[k][i]
                
#             case 'varpunkt_p31':
#                 sum_dim8 = sum_dim8 + df_dim[k][i]
#             case 'varpunkt_p32':
#                 sum32 = sum32 + df_dim[k][i]
#             case 'varpunkt_p33':
#                 sum_dim8 = sum_dim8 + df_dim[k][i]
#             case 'varpunkt_p34':
#                 sum_dim8 = sum_dim8 + df_dim[k][i]
                
#             case 'varpunkt_p35':
#                 sum_dim9 = sum_dim9 + df_dim[k][i]
#             case 'varpunkt_p36':
#                 sum_dim9 = sum_dim9 + df_dim[k][i]
#             case 'varpunkt_p37':
#                 sum_dim9 = sum_dim9 + df_dim[k][i]
                
#             case 'varpunkt_p38':
#                 sum_dim10 = sum_dim10 + df_dim[k][i]
#             case 'varpunkt_p39':
#                 sum_dim10 = sum_dim10 + df_dim[k][i]
#             case 'varpunkt_p40':
#                 sum40 = sum40 + df_dim[k][i]
#             case 'varpunkt_p41':
#                 sum_dim10 = sum_dim10 + df_dim[k][i]
                
#     if sum32 == 1:
#         sum_dim8 = sum_dim8 + 0.7
#     if sum32 == 2:
#         sum_dim8 = sum_dim8 + 0.8
#     if sum32 == 3:
#         sum_dim8 = sum_dim8 + 0.9
#     if sum32 == 4:
#         sum_dim8 = sum_dim8 + 1        
#     if sum32 == 5:
#         sum_dim8 = sum_dim8 + 1.2
#     if sum32 == 6:
#         sum_dim8 = sum_dim8 + 1.3
#     if sum32 == 7:
#         sum_dim8 = sum_dim8 + 1.4
#     if sum32 == 8:
#         sum_dim8 = sum_dim8 + 1.5 
        
        
#     if sum40 == 1:
#         sum_dim10 = sum_dim10 + 0.7
#     if sum40 == 2:
#         sum_dim10 = sum_dim10 + 0.8
#     if sum40 == 3:
#         sum_dim10 = sum_dim10 + 0.9
#     if sum40 == 4:
#         sum_dim10 = sum_dim10 + 1        
#     if sum40 == 5:
#         sum_dim10 = sum_dim10 + 1.2
#     if sum40 == 6:
#         sum_dim10 = sum_dim10 + 1.3
#     if sum40 == 7:
#         sum_dim10 = sum_dim10 + 1.4
   
#     if sum32 >= 100:
#         sum32 = 0
   
#     if sum40 >= 100:
#         sum40 = 0
   
#     total_dim1  = (sum_dim1  / (len(var_dim1) - noaplica_dim1))  *   len(var_dim1) 
#     total_dim2  = (sum_dim2  / (len(var_dim2) - noaplica_dim2))  *   len(var_dim2) 
#     total_dim3  = (sum_dim3  / (len(var_dim3) - noaplica_dim3))  *   len(var_dim3)  
#     total_dim4  = (sum_dim4  / (len(var_dim4) - noaplica_dim4))  *   len(var_dim4)  
#     total_dim5  = (sum_dim5  / (len(var_dim5) - noaplica_dim5))  *   len(var_dim5)  
#     total_dim6  = (sum_dim6  / (len(var_dim6) - noaplica_dim6))  *   len(var_dim6)  
#     total_dim7  = (sum_dim7  / (len(var_dim7) - noaplica_dim7))  *   len(var_dim7)  
#     total_dim8  = (sum_dim8  / (len(var_dim8) - noaplica_dim8))  *   len(var_dim8)  
#     total_dim9  = (sum_dim9  / (len(var_dim9) - noaplica_dim9))  *   len(var_dim9)  
#     total_dim10 = (sum_dim10 / (len(var_dim10)- noaplica_dim10)) *   len(var_dim10)
   
#     print("dimension 1:"+str(total_dim1))
#     print("dimension 2:"+str(total_dim2))
#     print("dimension 3:"+str(total_dim3))
#     print("dimension 4:"+str(total_dim4))
#     print("dimension 5:"+str(total_dim5))
#     print("dimension 6:"+str(total_dim6))
#     print("dimension 7:"+str(total_dim7))
#     print("dimension 8:"+str(total_dim8))
#     print("dimension 9:"+str(total_dim9))
#     print("dimension 10:"+str(total_dim10))
#     print("-----final de un registro---------------------")
   
#     p.write(df_dim["area"][i]+";"+df_dim["nombre_preg_codigo"][i]+";"+str(total_dim1)+";"+str(total_dim2)+";"+str(total_dim3)+";"+str(total_dim4)+";"+str(total_dim5)+";"+str(total_dim6)+";"+str(total_dim7)+";"+str(total_dim8)+";"+str(total_dim9)+";"+str(total_dim10)+"\n")       
         

# p.close()    
# print("-----final del Proceso-------------------")