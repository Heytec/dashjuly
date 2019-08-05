# build web-based data visualization interfaces
# Sash, dash-renderer, dash-html-components, dash-core-components, and plotly.#pip install dash dash-renderer dash-html-components dash-core-components plotly

#importing things things like graph components), and then HTML components (things like div tags...etc). Next, we begin our app:
import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()





app.layout = html.Div(children=[
    html.H1(children='Dash Tutorials'),
    dcc.Graph(  id='example',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [9, 6, 2, 1, 5], 'type': 'line', 'name': 'Boats'},
                {'x': [1, 2, 3, 4, 5], 'y': [8, 7, 2, 7, 3], 'type': 'bar', 'name': 'Cars'},
            ],
            'layout': {
                'title': 'Basic Dash Example'
            }
        })
])