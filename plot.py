import sys
import plotly.graph_objects as go

from data import read_data, get_cases, COL_COUNTRY


def plot_cases(fig, df, country, province=None):
    df = get_cases(df, country, province=province)
    # Get only cases per day
    fig.add_trace(go.Scatter(name=country, x=df.index, y=df))


def main(countries):
    df = read_data()
    fig = go.Figure()
    if countries is None:
        countries = sorted(set([(country, None) for country in df[COL_COUNTRY]]))
    for country in countries:
        if len(country) == 2:
            country, province = country
        else:
            province = None
        plot_cases(fig, df, country, province=province)

    fig.update_layout(title="Total cases")
    fig.show()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        countries = sys.argv[1:]
    countries = [
        "Netherlands",
        "Sweden",
        "Brazil",
        "China",
    ]
    main(countries)
