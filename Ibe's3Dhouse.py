# Importing Packages
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import pyproj
import rasterio
from rasterio.plot import show
from rasterio.windows import from_bounds
# ===============================
User_Choice = '''
Enter:Choose the following Coordinate system you want to give inputs
-- 'b' for "BelgianLamber72"(EPSG: 31370)
-- 'g' for "Web Geographical system(WGS)" (EPSG: 4326)
-- 't' for " International Terrestrial Reference Frame 2014 (ITRF2014)"(EPSG: 7789)
-- 'q' To Quit
'''
data = rasterio.open('DHMVIIDSMRAS1m_k13.tif')
def menu():
    user_input = input(User_Choice)
    while user_input != 'q':
        if user_input == 'b':
            prompt_Belgian_lamber_72()
        elif user_input == 'g':
            prompt_wgs()
        elif user_input == 'q':
            break
        else:
            print('Unknown command. Please try again')
        user_input = input(User_Choice)

def prompt_Belgian_lamber_72():
    coordinate = print('Welcome to Belgian_lamber_72 system! \n Your coordinates please: ')
    long = float(input('Long: '))
    lat = float(input('Lat: '))

    left = long - 100
    right = long + 100
    bottom = lat - 100
    top = lat + 100

    map = data.read(1, window=from_bounds(left, bottom, right, top, data.transform))

    fig = go.Figure(data=[go.Surface(z=map)])
    fig.show()

def prompt_wgs():
    coordinate = print("Welcome in WGS system, Please give your Long/Lat in: ")
    long_coor = float(input("Your longitude: "))
    lat_coor = float(input("Your latitude: "))

    transformer = pyproj.Transformer.from_crs('epsg:4326', 'epsg:31370')
    x_coor, y_coor = transformer.transform(long_coor, lat_coor)
    left = x_coor - 100
    right = x_coor + 100
    bottom = y_coor - 100
    top = y_coor + 100

    map = data.read(1, window=from_bounds(left, bottom, right, top, data.transform))

    fig = go.Figure(data=[go.Surface(z=map)])
    fig.show()
menu()