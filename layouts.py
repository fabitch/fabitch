import dash_html_components as html
import dash_core_components as dcc


def create_header():
    header = html.Header(
        className='header'
    )

    return header


def create_sidenav():
    sidenav = html.Aside(
        className='sidenav',
        children=[
            html.Div(
                className='sidenav__list',
                children=[
                    dcc.Dropdown(options=[{'label': 'Test', 'value': 'Test'}],
                                 className='custom-dropdown'),
                    dcc.Dropdown(options=[{'label': 'Test', 'value': 'Test'},
                                          {'label': 'label', 'value': 'value'}],
                                 className='custom-dropdown')
                ]),
        ]
    )
    return sidenav


def create_body():
    main = html.Main(
        className='main',
        children=[html.Header("Test", className='main-header'),
                  html.Div(
                      className='main-overview',
                      children=[
                          html.Div(["Overview"],
                                   className="overview-card"),
                          html.Div(["Overview"],
                                   className="overview-card")
                      ]
                  )
                  ]
    )

    return main
