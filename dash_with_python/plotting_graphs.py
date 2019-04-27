import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

x= [-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[]
for xs in x:
	y.append(xs**2)

app.layout = html.Div(children=[
	html.H1('Learning Dash and Plotting Graphs'),
	dcc.Graph(id='example',
			figure = {
				'data': [
					{'x': [1,2,3,4,5], 'y':[7,6,4,2,1], 'type': 'line', 'name': 'lineChart'},
					{'x': [1,2,3,4,5], 'y':[9,5,1,0,3], 'type': 'bar', 'name': 'barChart'},
					{'x': x, 'y':y, 'fill': 'tozeroy', 'name': 'filledChart'}
				],
				'layout':{
					'title': 'Dash Graph Example'
				}
				
			}
		)
	])

if __name__ == '__main__':
	app.run_server(debug=True)