# -*- coding: utf-8 -*-
"""
Created on Wed Dec 07 09:27:18 2016

@author: Dima
"""
#import PyQt4
#import PyQt4.QtWebEngineWidgets 
#import PyQt5

from PyQt5 import QtWidgets
 
from GUI2 import Ui_TabWidget

import datetime

from sqlalchemy import create_engine

from plotly.offline import plot
import plotly.graph_objs as go

import pandas as pd

class gui2w(Ui_TabWidget):
    def __init__(self, form):
        # Сконфигурировать интерфейс методом из базового класса Ui_Form
        self.setupUi(form)
        # Подключить созданные нами слоты к виджетам
        self.pushButton.clicked.connect(self.PrintVal)
        #self.connect_slots()  
        
#    def connect_slots(self):
#        self.pushButton.clicked.connect(self.PrintVal)
#        return None
            
    def PrintVal (self):
        fname = QtWidgets.QFileDialog.getOpenFileName()[0]
        print(fname)
        if fname != "":
            engine = create_engine(r'sqlite:///'+fname) # Создание подключения к БД 

            fixed_df=pd.read_sql_query('SELECT TabI1.TM AS Time, TabI1.VAL AS I1, TabI2.VAL AS I2, TabI3.VAL AS I3, TabI4.VAL AS I4, TabT1.VAL AS T1, TabT2.VAL AS T2, TabT3.VAL AS T3, TabVac.VAL AS Vac ' 
                                       'FROM DBAVl_sdcsd_CurentMetr_Cur3 TabI1, DBAVl_sdcsd_CurentMetr_Cur30 TabI2, DBAVl_sdcsd_CurentMetr_Cur31 TabI3, DBAVl_sdcsd_CurentMetr_Cur32 TabI4, '
                                            'DBAVl_sdcsd_Par3_AI0 TabT1, DBAVl_sdcsd_Par3_AI1 TabT2,  DBAVl_sdcsd_Par3_AI2 TabT3, '
                                            'DBAVl_sdcsd_Panel1_VIN3 TabVac '
                                       'WHERE Time=TabI2.TM AND Time=TabI3.TM AND Time=TabI4.TM AND Time=TabT1.TM AND Time=TabT2.TM AND Time=TabT3.TM  AND Time=TabVac.TM' , engine, index_col='Time')
            
            fixed_df.rename(lambda TM: datetime.datetime.fromtimestamp(TM),inplace=True) # Преобразоване времени UNIX в обычное время 
            
                    
            fixed_df.loc[fixed_df['I1'] < 0.0005,'I1'] = 0.0 
            fixed_df.loc[fixed_df['I2'] < 0.0005,'I2'] = 0.0 
            fixed_df.loc[fixed_df['I3'] < 0.0005,'I3'] = 0.0 
            fixed_df.loc[fixed_df['I4'] < 0.0005,'I4'] = 0.0 
            fixed_df.loc[fixed_df['T1'] < 0.1,'T1'] = 0.0 
            fixed_df.loc[fixed_df['T2'] < 0.1,'T2'] = 0.0 
            fixed_df.loc[fixed_df['T3'] < 0.1,'T3'] = 0.0 
            fixed_df.loc[fixed_df['Vac'] < 1e-6,'Vac'] = 0.0 
            
            trace1 = go.Scatter(x = fixed_df.index, y = fixed_df['I1'],mode='lines', name='I1',yaxis='y1')
            trace2 = go.Scatter(x = fixed_df.index, y = fixed_df['I2'],mode='lines', name='I2',yaxis='y1')
            trace3 = go.Scatter(x = fixed_df.index, y = fixed_df['I3'],mode='lines', name='I3',yaxis='y1')
            trace4 = go.Scatter(x = fixed_df.index, y = fixed_df['I4'],mode='lines', name='I4',yaxis='y1')
            trace5 = go.Scatter(x = fixed_df.index, y = fixed_df['T1'],mode='lines', name='T1',yaxis='y2')
            trace6 = go.Scatter(x = fixed_df.index, y = fixed_df['T2'],mode='lines', name='T2',yaxis='y2')
            trace7 = go.Scatter(x = fixed_df.index, y = fixed_df['T3'],mode='lines', name='T3',yaxis='y2')
            trace8 = go.Scatter(x = fixed_df.index, y = fixed_df['Vac'],mode='lines', name='Vac',yaxis='y3')
            
            layout = go.Layout(
                xaxis=dict(
                    domain=[0.05, 0.95]
                    ),
                yaxis1=dict(
                    autorange=True,           
                    title='Ток, А',
                    #gridcolor='#1f77b4',
                    titlefont=dict(
                        color='#1f77b4'
                    ),
                    tickfont=dict(
                        color='#1f77b4'
                    )
                ),
                yaxis2=dict(
                    autorange=True,       
                    title='Температура, С',
                    #gridcolor='#ff7f0e',
                    titlefont=dict(
                        color='#ff7f0e'
                    ),
                    tickfont=dict(
                        color='#ff7f0e'
                    ),
                    anchor='free',
                    overlaying='y',
                    side='left',
                    position=0.0
                ),    
                yaxis3=dict(
                    autorange=True,
                    #gridcolor='#d62728',
                    type='log',   
                    title='Вакуум, Torr',          
                    titlefont=dict(
                        color='#d62728'
                    ),
                    tickfont=dict(
                        color='#d62728'
                    ),        
                    anchor='free',
                    overlaying='y',
                    side='right',
                    exponentformat='e',
                    position=0.95
                )
            )
            fig = go.Figure(data=[trace1,trace2,trace3,trace4,trace5,trace6,trace7,trace8], layout=layout)
            plot(fig,filename='temp-plot.html', auto_open=False,)
        else:
            print(2)
        return None


if __name__ == "__main__":
    import sys
    #import pyqtgraph.examples
    #pyqtgraph.examples.run()
    app = QtWidgets.QApplication(sys.argv)
    TabWidget = QtWidgets.QTabWidget()
    ui = gui2w(TabWidget)
    TabWidget.show()
    #ui2.setupUi(TabWidget)
    sys.exit(app.exec_())