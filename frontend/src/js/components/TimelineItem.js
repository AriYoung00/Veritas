import React from 'react';
import { TimelineItem }  from 'vertical-timeline-component-for-react';
import Topic from './Topic.js';

const axios = require('axios');

class TimeLineItem extends React.Component {
	constructor(props){
		super(props)
		this.state = {
			date: this.props.value,
			topics: ['aadkfjakdjfkadj', 'b', 'c'],
		}
	}

	async getTopics() {
		axios.post(API_ENDPOINT_TOPICS), {
			date: this.state.date,
		}.then(function (response) {
            console.log(response);
            return response.data;
        }).then((data) => {
            this.setState({
                topics: data.topics,
            })
        }).catch(function (error) {
            console.log(error);
        });
	}
	
	render() {
		return (
			<TimelineItem dateText={this.state.date}>
				{this.state.topics.map((topic, index) => (
					<Topic value={topic} />
				))}
			</TimelineItem>
		);
	}
}

export default TimeLineItem;