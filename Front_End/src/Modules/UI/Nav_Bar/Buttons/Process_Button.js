import React, { Component } from 'react';
import ReactDOM from 'react-dom';

class ProcessButton extends Component {

	constructor (props) {
		super(props);
		
		this.handleClick = this.handleClick.bind(this);
	}

	handleClick(e){
		this.props.handlePhaseChange("Exporting");
	}

	render() {

		return (
			<section>
				<button className="nav-btn" onClick={this.handleClick}> Process </button>	
			</section>
		);
	}
}

export default ProcessButton;
