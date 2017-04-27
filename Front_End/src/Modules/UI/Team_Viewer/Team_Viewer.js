import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import './Team_Viewer.css';

import TeamList from './Team_List/Team_List'

class TeamViewer extends Component {
	constructor(props) {
		super(props);
		this.requestViewerUpdate = this.requestViewerUpdate.bind(this);
		this.state = {_is_up_to_date:false}
            this.Lists = [];
		this.number_of_teams = 0;
	}

	requestViewerUpdate(source){
		this.setState({_is_up_to_date:false});
	}

	render() {



		console.log("[PreRender]_upToDate: " + this.state._is_up_to_date);
	
		if(this.state._is_up_to_date == false)
		{
			this.Lists = [];
			this.number_of_teams = 0;

			this.Lists.push(
				<TeamList
					key="TeamList_0"
					list_id={0}
					title="Unassigned"
					_team_data = {this.props._team_data}
					requestViewerUpdate = {this.requestViewerUpdate} 
				/>
			);
	
			this.props._team_data.forEach(function callback(_member_data, index, members) {
				if (_member_data['Assigned Team']){
					if (parseInt(_member_data['Assigned Team']) > this.number_of_teams){
						this.number_of_teams = parseInt(_member_data['Assigned Team']);
					} 
				}
			}.bind(this))
	
			this.number_of_teams += 2;
	
			while (this.Lists.length < this.number_of_teams){
				this.Lists.push(
					<TeamList
						key={"TeamList_" + (this.Lists.length)}
						list_id={this.Lists.length}
						title={"Team " + (this.Lists.length)}
						_team_data = {this.props._team_data}
						requestViewerUpdate = {this.props.requestViewerUpdate} 
					/>
				);
			}

			this.setState({_is_up_to_date:true});


		}
		{console.log("number of teams: " + this.number_of_teams + " lists:")}	
		{console.log(this.Lists)}	
		console.log("[PostRender]_upToDate: " + this.state._is_up_to_date);

		return (
			<div className="App">
				{this.Lists}			
			</div>
		);
	}
}

export default TeamViewer;
