import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import TeamMember from './Team_Member/Team_Member'
import { DropTarget } from 'react-dnd';
const ListContent = ({_caller}) => (

	<tbody>
		{
			_caller.props._team_data.filter(function(obj) {
				if (_caller.props.list_id == 0){
					return (
						(obj['Assigned Team'] == 0) 
						|| 
						(obj['Assigned Team'] == null)
					);
				} else {
					return (obj['Assigned Team'] == _caller.props.list_id);
				}
			}).map(member_data => (
				<TeamMember 
					member_data={member_data}
					requestViewerUpdate={_caller.props.requestViewerUpdate}
				/>
			))
		}
	</tbody>	
); 

const listTarget = {
	drop(props, monitor) {
		const item = monitor.getItem();
		item.data['Assigned Team'] = props.list_id;
		props.requestViewerUpdate();
	}
};

function collect(connect, monitor) {
	return {
		connectDropTarget: connect.dropTarget(),
		isOver: monitor.isOver()
	};
}

class TeamList extends Component {
	constructor(props) {
		super(props);
		this.handleStateUpdate = this.handleStateUpdate.bind(this);
	}

	handleStateUpdate(source){
		this.props.handleStateUpdate(source);
	}
	
	render() {
	
		let List = null;
	
		if (this.props._team_data != null) {
			List = <ListContent 
					list_id = {this.props.list_id}
					_team_data = {this.props._team_data}
					_caller = {this}
				/>;
		}

		const {connectDropTarget, isOver } = this.props;
	
		return connectDropTarget(
			<table>
				<thead>
					<tr>
						<th colspan="3">{this.props.title}</th>
					</tr>
				</thead>
				{List}				
			</table>
		);
	}
}

export default DropTarget("team_view_item", listTarget, collect) (TeamList);
