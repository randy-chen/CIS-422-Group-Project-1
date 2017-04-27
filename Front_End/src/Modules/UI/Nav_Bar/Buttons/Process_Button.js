import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import {csv} from 'd3-request';

class ProcessButton extends Component {

	constructor (props) {
		super(props);
		
		this.handleClick = this.handleClick.bind(this);
            this.handleProcessResponse = this.handleProcessResponse.bind(this);
      }

      handleProcessResponse(response){
		csv("/output", this.props.handleImportedData);
		console.log(this);
		console.log(response);	

      }



	handleClick(e){

	axios.get('/process')
		.then(this.handleProcessResponse)
		.catch(function (error) {
			console.log("Axios: " + error);
	});	
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
