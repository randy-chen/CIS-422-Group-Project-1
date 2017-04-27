import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import { DragSource } from 'react-dnd';

const memberSource = {
	beginDrag(props) {
		// Return the data describing the dragged item
		const item = { data: props.member_data };
		return item;
	},

	endDrag(props, monitor, component) {
		if (!monitor.didDrop()) {
			return;
		}
	}
};

function collect(connect, monitor) {
	return {
	// Call this function inside render()
	// to let React DnD handle the drag events:
	connectDragSource: connect.dragSource(),
	// You can ask the monitor about the current drag state:
	isDragging: monitor.isDragging()
	};
}

class TeamMember extends Component {
	constructor(props) {
		super(props);
		this.handleClick = this.handleClick.bind(this);
	}

	handleClick(e){
		console.log(this.props.member_data['Assigned Team']);
		this.props.member_data['Assigned Team'] = 0;
		console.log(this);
		console.log(this.props.member_data['Assigned Team']);
		this.props.requestViewerUpdate("Hurraaaaaaaaaay");
	}

	render() {
		
		const {data} = this.props;
		const { isDragging, connectDragSource } = this.props;

		return connectDragSource(
			<tr>
				<td>{!isDragging && this.props.member_data['Full Name']}</td>
			</tr>
					
		);
	}
}

export default DragSource("team_view_item", memberSource, collect) (TeamMember);
