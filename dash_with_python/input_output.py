import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div(children=[
	dcc.Input(id='inputField', value='', placeholder='Type Something...', type='text'),
	html.Div(id='outputDiv')
])

@app.callback(
	Output(component_id='outputDiv', component_property='children'),
	[Input(component_id='inputField', component_property='value')])
def update_value(inputData):
	return inputData

if __name__ == '__main__':
	app.run_server(debug=True)