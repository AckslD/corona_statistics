import sys
import numpy as np
import plotly.graph_objects as go
from scipy.optimize import curve_fit

from data import read_data, get_cases


def sigmoid(x, L, k, x0):
    y = L / (1 + np.exp(-k*(x-x0)))
    return y


def fit_data(xdata, ydata, country):
    popt, pcov = curve_fit(
        sigmoid,
        xdata=xdata,
        ydata=ydata,
        bounds=(
            [0., 0.01, 5],
            [1e9, 0.3, 100],
        ),
    )
    return popt, pcov


def main(country):
    df = read_data()
    df = get_cases(df, country)

    # Only include data from actual outbreak (above 10 cases for now)
    df = df[df > 10]

    xdata = list(range(len(df)))
    ydata = df.values

    # Fit to sigmoid
    popt, pcov = fit_data(xdata, ydata, country)

    # Predict
    x = np.linspace(0, 2 * len(xdata))
    y = sigmoid(x, *popt)

    # Plot
    fig = go.Figure()

    fig.add_trace(go.Scatter(name='data', x=xdata, y=ydata))
    fig.add_trace(go.Scatter(name='fit', x=x, y=y))

    fig.update_yaxes(range=[0, 2 * max(ydata)])
    fig.update_layout(title=f"Prediction (sigmoid) {country}")

    fig.show()


if __name__ == '__main__':
    if len(sys.argv) == 2:
        country = sys.argv[1]
    else:
        country = "China"
    main(country)
