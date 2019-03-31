import React from 'react';
import { Link, Route, BrowserRouter as Router } from 'react-router-dom';
import StyledLink from './StyledLink';
import TopicView from './TopicView';

class Topic extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			date: props.date,
			topic: this.props.value,
		}
	}

	render() {
		return (
			<div>
				<Link to='/topicView'>
					<StyledLink>
						{this.state.topic}
					</StyledLink>
				</Link>
			</div>
		);
	}
}

export default Topic;