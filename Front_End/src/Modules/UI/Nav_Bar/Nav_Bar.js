import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Nav_Bar.css';
import ImportButton from './Buttons/Import_Button'
import ProcessButton from './Buttons/Process_Button'
import FinishButton from './Buttons/Finish_Button'
import ExportButton from './Buttons/Export_Button'
import ReactUploadFile from 'react-upload-file';
import {CSVLink} from 'react-csv';


class NavBar extends Component {

	constructor(props) {
		super(props);
		this.handlePhaseChange = this.handlePhaseChange.bind(this);
		this.handleDataChange = this.handleDataChange.bind(this);
		this.handleImportedData = this.handleImportedData.bind(this);
	}

	handlePhaseChange(new_phase) {
		this.props.handlePhaseChange(new_phase);
	}

	handleDataChange(new_team_data) {
		this.props.handleDataChange(new_team_data);
	}

	handleImportedData(error, imported_data) {
		if (error) {
			console.log("Not Imported");
			console.log(error);
		} else {
			console.log("Imported");
			console.log(imported_data);
			this.props.handleDataChange(imported_data);
		}
	}

	render() {

			const buttons = [];

			buttons.push(
				<ImportButton 
					handleImportedData = {this.handleImportedData} 
					handleDataChange = {this.handleDataChange}  
					requestViewerUpdate = {this.requestViewerUpdate} 
					handlePhaseChange = {this.handlePhaseChange} 
					key="ImportButton_0" 
				/>
			);		
			
			buttons.push(
				<ProcessButton
					handlePhaseChange = {this.handlePhaseChange}
					handleImportedData = {this.handleImportedData} 
					handleDataChange = {this.handleDataChange}  
					requestViewerUpdate = {this.requestViewerUpdate} 
					key="ProcessButton_0"
				/>
			);

			buttons.push(
				<FinishButton
					_team_data={this.props._team_data}
					handlePhaseChange = {this.handlePhaseChange}
					key="FinishButton_0"
				/>
			);

		return (
			<div id="nav">
				{(this.props._current_phase == "Importing") && buttons[0]}
				{(this.props._current_phase == "Previewing") && buttons[1]}
				{(this.props._current_phase == "Editing") && buttons[2]}
				{(this.props._current_phase == "Exporting") && 	<ExportButton
					_team_data={this.props._team_data}
					handlePhaseChange = {this.handlePhaseChange}
					key="ExportButton_0"
				/>}
				{(this.props._current_phase == "Uploading") && <p className="Status">Importing</p>}
			</div>
		);
	}
}

export default NavBar;
