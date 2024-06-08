# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 21:50:50 2022

@author: eanaya
"""

def calcular_edad(dia_nacio,mes_nacio,anio_nacio,dia_actual,mes_actual,anio_actual)->str:
    mes,dia = divmod(dia_nacio + dia_actual,30)
    anio,mes = divmod(mes + mes_nacio + mes_actual,12)
    anio +=  anio_nacio + anio_actual
    if anio > 12:anio -= 12
    #return f"{anio}:{mes}:{dia}"
    return anio,mes,dia

print(calcular_edad(28,10,1979,20,4,2023))
#print(calcular_edad(7,3,58,12,24,33))

