import React, { Component } from 'react';
import ReactDOM from 'react-dom';



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
		return (
			<tr onClick={this.handleClick} >
				<td> {this.props.member_data['Full Name']} </td>
			</tr>
					
		);
	}
}

export default TeamMember;
