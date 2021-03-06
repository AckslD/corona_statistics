#!/usr/bin/env python3

import click

from plot import main as plot_cases
from update import main as update_all
from predict import main as predict_country

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


def check_update(func):
    def new_func(*args, **kwargs):
        update_all(force=False)
        func(*args, **kwargs)
    new_func.__name__ = func.__name__
    return new_func


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """Command line interface for analysing coronavirus cases."""
    pass


########
# plot #
########

@cli.command()
@click.option("-c", "--countries", type=str, default=None,
              help="Choose which countries to plot (default all). "
                   "Seperate contries by , and enclose with '. "
                   "For example -c 'Netherlands,China,Sweden'."
              )
@check_update
def plot(countries):
    if countries is not None:
        countries = [country.strip() for country in countries.split(',')]
    plot_cases(countries)


###########
# predict #
###########
@cli.command()
@click.option("-c", "--country", type=str, default="China",
              help="Choose which country to predict (default China). "
                   "For example -c Sweden."
              )
@check_update
def predict(country):
    predict_country(country)


##########
# update #
##########

@cli.command()
def update():
    update_all(force=True)


if __name__ == '__main__':
    cli()
