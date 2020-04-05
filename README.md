# Corona statistics

## Install
Clone the repo by
```sh
git glone https://github.com/AckslD/corona_statistics.git
```
and cd into the folder
```sh
cd corona_statistics
```

You need python and the additional packages can be installed by
```sh
pip3 install -r requirements.txt
```

## Plot
![screencast](img/corona_plot.gif)

To plot all countries in an interactive plot do:
```sh
./main.py plot
```
In the plot you can click on countries to remove and add them to the current plot.

To plot for example only Sweden do
```sh
./main.py plot -c Sweden
```
or for plotting Sweden, Netherlands, Italy and China do:
```sh
./main.py plot -c "Sweden,Netherlands,Italy,China"
```

## Data
Data is taken from https://github.com/CSSEGISandData/COVID-19 and in particular this [file](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv)

The local data for plotting etc get updated automatically when executed once a day. You can also force-update by
```sh
./main.py update
```
