# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt
import os
import pandas as pd

def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.

    """
    os.makedirs('docs', exist_ok=True)
    visual_spw(load_data())
    visual_ms(load_data())
    visual_acr(load_data())
    visual_wd(load_data())
    html()

def load_data():
    """
    Carga los datos del archivo files//shipping-data.csv.
    """
    df = pd.read_csv('files/input/shipping-data.csv')
    return df

def visual_spw(df):

    df = df.copy()
    plt.figure()
    counts = df.Warehouse_block.value_counts()

    counts.plot.bar(
        title='Shipping per Warehouse',
        xlabel='Warehouse block',
        ylabel='Record count',
        color = 'tab:blue',
        fontsize = 8,
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/shipping_per_warehouse.png')

def visual_ms(df):
    df = df.copy()
    plt.figure()
    counts = df.Mode_of_Shipment.value_counts()
    counts.plot.pie(
        title='Mode of shipment',
        wedgeprops=dict(width=0.35),
        ylabel='',
        colors = ['tab:blue', 'tab:orange', 'tab:green'],
    )
    plt.savefig('docs/mode_of_shipment.png')

def visual_acr(df):
    df = df.copy()
    plt.figure()
    df = (
        df[['Mode_of_Shipment' , 'Customer_rating']]
        .groupby('Mode_of_Shipment')
        .describe()
    )
    df.columns = df.columns.droplevel()
    df = df[['mean','min','max']]
    plt.barh(
        y=df.index.values,
        width=df['max'].values - 1,
        left=df['min'].values,
        height=0.9,
        color = 'lightgray',
        alpha=0.8,
    )
    colors=[
        'tab:green' if value >= 3 else 'tab:orange' for value in df['mean'].values
    ]
    plt.barh(
        y=df.index.values,
        width=df['mean'].values - 1,
        left=df['min'].values,
        height=0.5,
        color=colors,
        alpha=1,
    )
    plt.title('Average customer rating')
    plt.gca().spines['left'].set_color('gray')
    plt.gca().spines['bottom'].set_color('gray')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/average_customer_rating.png')
    
def visual_wd(df):
    df = df.copy()
    plt.figure()
    df.Weight_in_gms.plot.hist(
        title='Shipped weight distribution',
        color='tab:orange',
        edgecolor='white',
    )
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    plt.savefig('docs/weight_distribution.png')

def html():
    contenido_html = """<!DOCTYPE html>
    <html>
        <body>
            <h1>Shipping dashboard Example</h1>
            <div style='width: 45%; float: left;'>
                <img src='docs/shipping_per_warehouse.png' alt='FIG1'>
                <img src='docs/mode_of_shipment.png' alt='FIG2'>
            </div>
            <div style='width: 45%; float: right;'>
                <img src='docs/average_customer_rating.png' alt='FIG3'>
                <img src='docs/weight_distribution.png' alt='FIG4'>
            </div>
        </body>
    </html>"""

    with open("docs/index.html", "w") as archivo:
        archivo.write(contenido_html)

pregunta_01()