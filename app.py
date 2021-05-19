import dash
import dash_html_components as html

from layouts import create_header

app = dash.Dash(__name__)

app.layout =\
    html.Div(className='grid-container',
             children=[create_header(),
                       html.Aside(className='sidenav',
                                  children=['Test']),
                       html.Main(className='main',
                                 children=['Test']),
                       html.Footer(className='footer',
                                   children=['Test'])
                       ])

if __name__ == "__main__":
    app.run_server(debug=True)
