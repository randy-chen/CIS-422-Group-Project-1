import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import {CSVLink} from 'react-csv';

class ExportButton extends Component {

	constructor (props) {
		super(props);
	}

	render() {

		return (
			<section>
				<CSVLink
					data={this.props._team_data}
					filename={"output.csv"}
					className="btn btn-primary"
					target="_blank"
				>
					<button className="nav-btn"> Export </button>
				</CSVLink>		
			</section>
		);
	}
}

export default ExportButton;
