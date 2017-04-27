import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Header.css';

class Header extends Component {
	render() {
		return (
			<div className="App">
				<div className="App-header">
					<h2>{this.props.title}</h2>
				</div>
			</div>
		);
	}
}

export default Header;
