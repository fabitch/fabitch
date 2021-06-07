import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import pandas as pd

import yfinance as yf

DATA = yf.Ticker("ABNB")
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
                           {'label': 'Airbnb', 'value': 'ABNB'}
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


def create_card_div_for_graph(figure):
    return html.Div(
        className='card',
        children=[
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
def update_chart_one(ticker, label):
    company_name = label[0]['label']
    charts = []
    # data = yf.Ticker(ticker)
    stock_prices = DATA.history('max')
    title = f"Stock Prices for {company_name}"
    fig = px.line(stock_prices, x=stock_prices.index,
                  y=['Open', 'High', 'Close'], title=title)
    charts.append(create_card_div_for_graph(fig))

    title = f"Daily Returns of {company_name}"
    daily_returns = stock_prices['Close'].pct_change()

    charts.append(create_card_div_for_graph(px.line(daily_returns, title=title)))

    return_dist = daily_returns.round(2).reset_index()
    return_dist = return_dist.groupby('Close').count()

    # TODO: add line chart to bar chart to see distribution
    title = f"Distribution of daily Returns of {company_name} since " \
            f"{min(pd.to_datetime(daily_returns.index))}"
    fig = px.bar(return_dist, title=title)
    charts.append(create_card_div_for_graph(fig))
    return charts


if __name__ == "__main__":
    app.run_server(debug=True)
