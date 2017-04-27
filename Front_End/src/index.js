import React from 'react';
import ReactDOM from 'react-dom';

import { BrowserRouter as Router, Route } from 'react-router-dom'; 

import UI from './Modules/UI'; 

ReactDOM.render(( 
	<Router>
		<section> 
			<Route exact path="/" component={UI} /> 
		</section>
	</Router> ), 
	document.getElementById('root')
);
