import React, { Component } from 'react';
import ReactDOM from 'react-dom';

import {csv} from 'd3-request';

import FileInput from 'react-fine-uploader/file-input'
import FineUploaderTraditional from 'fine-uploader-wrappers'

import {CSVLink} from 'react-csv';

const uploader = new FineUploaderTraditional({
	options: {
		request: {
			endpoint: './uploads'
		}
	}
})

class ImportButton extends Component {

	constructor (props) {
		super(props);

		this.handleUploadResponse = this.handleUploadResponse.bind(this);
	}

	handleUploadResponse(id, name, response){
		if (response.success){
			this.props.handlePhaseChange("Processing");
			csv("/download", this.props.handleImportedData);
		} else {
			console.log("[Upload Error]: " + response.error);
			alert("[Upload Error]: " + response.error);
			this.props.handlePhaseChange("Importing");
		}

	}

	render() {

		uploader.on('complete', this.handleUploadResponse)

		uploader.on('submitted', (id, name) => {
			this.props.handlePhaseChange("Uploading");
			console.log("[Uploading]: " + name);	
		})

		return (
			<section>
				<FileInput
					accept='.csv'
					uploader={ uploader }
					handlePhaseChange = {this.props.handlePhaseChange}
				>
					<button className="nav-btn"> Import </button>	
				</FileInput>
			</section>
		);
	}
}

export default ImportButton;
