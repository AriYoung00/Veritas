import React from 'react';

export function formatDate(date) {
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

	return (`${days[1]}/${days[2]}/${days[0]}, ${time} UTC`);
}