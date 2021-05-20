import dash_html_components as html


def create_header():
    header = html.Header(
        className='header',
        children=[
        ]
    )

    return header


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
