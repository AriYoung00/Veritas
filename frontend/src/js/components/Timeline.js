import React from 'react';
import { Timeline }  from 'vertical-timeline-component-for-react';
import TimeLineItem from './TimelineItem';
import Header from './Header';
import Title from './Title';
class TimeLine extends React.Component {
	constructor(props){
		super(props)
		let date = new Date();

		this.state = {
			dates: [],
		}

		for (let i = 0; i < 8; i++) {
			date.setMinutes(date.getMinutes() - 30);
			let minutes = date.getMinutes() < 30 ? '00' : '30';
			let day = date.getDate() < 10 ? '0' + date.getDate() : date.getDate();
			let month = (date.getMonth() + 1) < 10 ? '0' + (date.getMonth() + 1) : date.getMonth() + 1;
			let hour = date.getHours() < 10? '0' + date.getHours() : date.getHours();
			this.state.dates.push(`${date.getFullYear()}-${month}-${day}T${hour}:${minutes}:00Z`);
		}
		console.log(this.state.dates)
	}

	render() {
		return (
			<div>
				<Header></Header>
				<Title>Timeline</Title>
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