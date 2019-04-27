import dash
import dash_html_components as html
from dash_canvas import DashCanvas

app = dash.Dash(__name__)

app.layout = html.Div([
	html.H3('Draw on the canvas'),
	html.Div([
		DashCanvas(
		id='drawingCanvas',
		hide_buttons=['select', 'zoom', 'pan', 'rectangle'],
		)
	]),
	
])

if __name__ == '__main__':
	app.run_server(debug=True)

