import csv
from datetime import datetime

import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
import numexpr as ne


def create_function_from_text(btn_name, function: str, x_before: float, x_after: float, x_height: int):
    print(function)
    x = np.linspace(x_before, x_after, x_height)
    y = ne.evaluate(function)
    print(y)
    if btn_name == "linear":
        interpolation_2d(x, y, x_height)
    elif btn_name == "spline":
        spline_interpolation(x, y, x_height)


def get_data_from_file(btn_name, x_array, y_array, x_height):
    x_current = list()
    y_current = list()

    for x in x_array:
        x_current.append(float(x.replace(',', '.')))

    for y in y_array:
        y_current.append(float(y.replace(',', '.')))
    if btn_name == "linear":
        interpolation_2d(x_current, y_current, x_height)
    elif btn_name == "spline":
        spline_interpolation(x_current, y_current, x_height)


def choose_function(btn_name, function_name: str, x_before: float, x_after: float, x_height: int):
    x = np.linspace(x_before, x_after, x_height)
    case_dict = {
        "cos": np.cos(x),
        "sin": np.sin(x),
        "exp": np.exp(x ** 2)
    }
    y = case_dict.get(function_name)
    if btn_name == "linear":
        interpolation_2d(x, y, x_height)
    elif btn_name == "spline":
        spline_interpolation(x, y, x_height)


def interpolation_2d(x, y, x_height):
    xnew = np.linspace(x[0], x[-1], x_height * 10)
    f1 = interpolate.interp1d(x, y, kind='linear')
    f2 = interpolate.interp1d(x, y, kind='quadratic')
    f3 = interpolate.interp1d(x, y, kind='cubic')
    write_to_csv("linear_data.csv", xnew, f1(xnew))
    write_to_csv("quadratic_data.csv", xnew, f2(xnew))
    write_to_csv("cubic_data.csv", xnew, f3(xnew))
    plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--r', xnew, f3(xnew), '--g')
    plt.legend(['Данные', 'Линейная', 'Квадратичная', 'Кубическая'], loc='best')
    plt.show()


def spline_interpolation(x, y, x_height):
    sp1 = interpolate.splrep(x, y)
    x2 = np.linspace(x[0], x[-1], x_height * 10)
    y2 = interpolate.splev(x2, sp1)
    write_to_csv("spline_data.csv", x2, y2)
    plt.plot(x, y, 'o', x2, y2)
    plt.legend(['Данные', 'Линейная'], loc='best')
    plt.show()


def write_to_csv(file_name, x_array, y_array):
    with open(file_name, mode='a') as result_file:
        writer = csv.writer(result_file, delimiter=';', quoting=csv.QUOTE_MINIMAL)

        x_save = list('x')
        y_save = list('y')

        for x in x_array:
            x_save.append(str(x).replace('.', ','))
        for y in y_array:
            y_save.append(str(y).replace('.', ','))

        time = ['Время записи:', datetime.now()]
        writer.writerow(time)
        writer.writerow(x_save)
        writer.writerow(y_save)
