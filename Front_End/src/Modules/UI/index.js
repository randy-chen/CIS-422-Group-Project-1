import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {csv} from 'd3-request';
import Header from './Header/Header'
import NavBar from './Nav_Bar/Nav_Bar'
import Importer from './Nav_Bar/Buttons/Import_Button'
import TeamViewer from './Team_Viewer/Team_Viewer'

import DancingJoesephImage from '../../../public/assets/dancing_joeseph.gif';

import { DragDropContext } from 'react-dnd';
import HTML5Backend from 'react-dnd-html5-backend';

class UI extends Component {
	
	constructor(props) {
		super(props);

		this.state = {
			_team_data: [],
			_current_phase: "Importing",
		}
	
		this.handlePhaseChange = this.handlePhaseChange.bind(this);
		this.handleDataChange = this.handleDataChange.bind(this);
		this.handleViewerUpdateRequest = this.handleViewerUpdateRequest.bind(this);
		this.handleViewerUpdateCompletion = this.handleViewerUpdateCompletion.bind(this);
	
	}

	handleViewerUpdateCompletion(source){
		this.setState({_viewer_isUpToDate:true});
		console.log("viewer completion issued by " + source);
		
	}

	handleViewerUpdateRequest(source){
		this.viewer.requestViewerUpdate(source);
		console.log("TOP: pre_state: " + this.viewer.state._is_up_to_date);
		this.viewer.setState({_is_up_to_date:false});
		console.log("TOP: post_state: " + this.viewer.state._is_up_to_date);
	}

	handlePhaseChange(new_phase){
		this.setState({_current_phase:new_phase});
	}

	handleDataChange(new_team_data){
		this.setState({_team_data:new_team_data});
		this.handleViewerUpdateRequest("Data Change Handler");
	}

	render() {
		return (
			<div className="App">
				<Header key="Header" title="Team Builder"/>
				<NavBar key="Nav_Bar" 
					_current_phase={this.state._current_phase} 
					_team_data={this.state._team_data}
					handlePhaseChange={this.handlePhaseChange}
					requestViewerUpdate = {this.handleViewerUpdateRequest} 
					handleDataChange={this.handleDataChange}
				/>
				{(this.state._current_phase == "Importing") && 
					<div className="directions">
						Welcome!
						<br/> 
						Choose the CSV file by clicking "Import" to begin the process.
					</div>
				}
				{(this.state._current_phase == "Previewing") && 
					<div className="directions">
						Your data has been imported successfully!
						<br/> 
						Next, Click the process button to run the algorithim on your data.
					</div>
				}
				{(this.state._current_phase == "Processing") && 
					<section>
					<div className="directions">
						Processing...
						<br/> 
						Please wait while our algorithim generates an optimal team formation for your data.
					</div>
					<img src={DancingJoesephImage}/>
					</section>
				}
				{(this.state._current_phase == "Editing") && 
					<div className="directions">
						Done!
						<br/> 
						You may make any additional adjustments by dragging team members between teams.
						<br/>
						Once you are satisfied with your data, click finish to prepare the data for exporting.
					</div>
				}	
				{(this.state._current_phase == "Exporting") && 
					<div className="directions">
						Your data is Ready!
						<br/>
						Click the Export button to save your final CSV.
						<br/>
						A file name "output.csv" will be begin downloading.
						<br/>
						In output file, each memeber row representing a memeber will have an addition column names 'Assigned Team' containing a value which indicate the team they have been assigned to.
						<br/>
						In addition to your final formation, two additional formations recomended by our alogorithim will be included.
						<br/>
						Thank you for using our services!
						<br/>
					</div>
				}	
				{
					(this.state._current_phase == "Editing" 
					|| this.state._current_phase == "Previewing") 
					&& 
					<TeamViewer 
						key="Team_Viewer" 
						_team_data={this.state._team_data} 
						completeViewerUpdate = {this.handleViewerUpdateCompletion} 
						requestViewerUpdate = {this.handleViewerUpdateRequest} 
						ref={(viewer) => { this.viewer = viewer; }}
					/>
				}
			</div>
		);
	}
}

export default DragDropContext(HTML5Backend) (UI);
