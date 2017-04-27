import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import {csv} from 'd3-request';
import Header from './Header/Header'
import NavBar from './Nav_Bar/Nav_Bar'
import Importer from './Nav_Bar/Buttons/Import_Button'
import TeamViewer from './Team_Viewer/Team_Viewer'

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

				<p> Status: {this.state._current_phase} </p>
				
				{
					(this.state._current_phase == "Processing") 
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

export default UI;
