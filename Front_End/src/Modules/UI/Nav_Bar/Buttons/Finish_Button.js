import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import {CSVLink} from 'react-csv';

class ExportButton extends Component {

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
				<button onClick={this.handleClick} className="nav-btn"> Finish </button>
			</section>
		);
	}
}

export default ExportButton;
