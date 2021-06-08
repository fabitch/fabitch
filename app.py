import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

import yfinance as yf

app = dash.Dash(__name__)

app.layout = \
    html.Main(
        className='main',
        children=[
            html.Div(
                className='control-panel-wrapper',
                children=[
                   dcc.Dropdown(
                       id='ticker',
                       options=[
                           {'label': 'Airbnb', 'value': 'ABNB'},
                           {'label': 'Umicore SA', 'value': 'UMI.BR'},
                           {'label': 'Quantumscape', 'value': 'QS'},
                           {'label': 'E.on SE', 'value': 'EONGY'},
                           {'label': 'Volkswagen Group', 'value': 'VOW.DE'},
                           {'label': 'Taiwan Semiconductor Manufacturing Company (TSMC)', 'value': 'TSM'},
                           {'label': 'Oatly Group AB', 'value': 'OTLY'},
                       ],
                       value='ABNB'
                   )
                ]
            ),
            html.Div(
                className='main-overview',
                id='overview-container'
            ),
            html.Div(
                className='table-container',
                children=[
                    html.Div(
                        id='table-div',
                        style={'width': '100%'}
                    )
                ]
            ),
            html.Div(
                className='main-cards',
                id='charts'
            ),
            html.Div(
                className='main-cards chart-collection',
                id='warehouse-pie',
            )
        ]
    )


def create_card_div_for_graph(figure, title: str):
    return html.Div(
        className='card',
        children=[
            html.P(title),
            html.Div(
                dcc.Graph(figure=figure),
                style={'width': '100%'}
            ),
        ]
    )


@app.callback(
    Output(component_id='charts', component_property='children'),
    Input(component_id='ticker', component_property='value'),
    State(component_id='ticker', component_property='options')
)
def update_chart_one(ticker, options):
    company_name = [x['label'] for x in options if x['value'] == ticker][0]
    charts = []
    data = yf.Ticker(ticker)
    stock_prices = data.history('max')
    title = f"Stock Prices for {company_name}"
    fig = px.line(stock_prices, x=stock_prices.index,
                  y=['Open', 'High', 'Close'],
                  labels={'value': f"Stock price in {data.info['currency']}"}
                  )
    charts.append(create_card_div_for_graph(fig, title))

    title = f"Daily Returns of {company_name}"
    daily_returns = stock_prices['Close'].pct_change()

    charts.append(create_card_div_for_graph(px.line(daily_returns), title))

    # TODO: add line chart to bar chart to see distribution
    title = f"Distribution of daily Returns of {company_name} since " \
            f"{min(pd.to_datetime(daily_returns.index))}"
    # TODO: dynamically compute bin number
    fig = px.histogram(daily_returns, x=daily_returns.values,
                       nbins=100)

    charts.append(create_card_div_for_graph(fig, title))
    return charts


if __name__ == "__main__":
    app.run_server(debug=True)
