import React from 'react';
import { Timeline }  from 'vertical-timeline-component-for-react';
import TimeLineItem from './TimelineItem';
import Header from './Header';
class TimeLine extends React.Component {
	constructor(props){
		super(props)
		let date = new Date();

		this.state = {
			dates: [],
		}

		for (let i = 0; i < 14; i++) {
			date.setDate(date.getDate() + 1);
			this.state.dates.push(`${date.getFullYear()}-${date.getMonth() + 1}-${date.getDate() + i}`);
		}
	}

	render() {
		return (
			<div>
				<Header></Header>
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