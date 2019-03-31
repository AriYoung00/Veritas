import React from 'react';
import { API_ENDPOINT_TOPICS, API_ENDPOINT } from './../constants/CONFIG';
import { TimelineItem }  from 'vertical-timeline-component-for-react';
import Topic from './Topic.js';

const axios = require('axios');


class TimeLineItem extends React.Component {
	constructor(props){
		super(props)
		this.state = {
			date: this.props.value,
			topics: [],
		}
	}

	componentDidMount() {
		this.getTopics();
	}

	async getTopics() {
		axios.get(API_ENDPOINT_TOPICS, {
			crossDomain: true,
			params: {
			  date: this.state.date
			}
		}).then(function (response) {
            console.log(response);
            return response.data;
        }).then((data) => {
            this.setState({
                topics: data.topics,
            })
            console.log(this.state.topics);
        }).catch(function (error) {
            console.log(error);
        });
	}

	formatDate(date) {
		date = 	String(date).slice(0, String(date).length-1).split('T');
		let days = String(date[0]).split('-');
		let mins = String(date[1]).split(':');

		let time;
		if (mins[0] == 12)
			time = `12:${mins[1]}pm`;
		else if (mins[0] == 0)
			time = `12:${mins[1]}am`;
		else
			time = mins[0] < 12 ? `${mins[0]}:${mins[1]}am` : `${mins[0] - 12}:${mins[1]}pm`;

		return (`${days[1]}/${days[2]}/${days[0]}, ${time}`);
	}
	
	render() {
		return (
			<TimelineItem 
				dateText={this.formatDate(this.state.date)}
				dateInnerStyle={{ background: '#2FD3F8' }}
				style={{ color: '#2FD3F8' }}
				bodyContainerStyle={{
			      	background: '#E3F5F9',
			      	padding: '20px',
			      	borderRadius: '8px',
			    }}
			>
				{this.state.topics.map((topic) => (
					<Topic date={this.formatDate(this.state.date)} topic={topic} />
				))}
			</TimelineItem>
		);
	}
}

export default TimeLineItem;