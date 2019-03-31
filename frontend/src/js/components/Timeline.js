import React from 'react';
import { Timeline }  from 'vertical-timeline-component-for-react';
import TimeLineItem from './TimelineItem';

class TimeLine extends React.Component {
	constructor(props){
		super(props)
		let date = new Date();

		this.state = {
			dates: [],
		}

		for (let i = 0; i < 7; i++) {
			this.state.dates.push(`${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate() + i}`);
		}
	}

	render() {
		return (
			<div>
				<Timeline>
					{this.state.dates.map((date, index) => (
						<TimeLineItem value={date} />
					))}
				</Timeline>
			</div>
		);
	}
}

export default TimeLine;