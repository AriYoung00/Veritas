import React, { Component } from "react";
import { API_ENDPOINT_ARTICLES } from './../constants/CONFIG';
import Title from './Title';
const axios = require('axios');

class TopicView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            topic: props.topic,
            date: props.date,
            articles_data: [],
        };

        this.getArticles = this.getArticles.bind(this) 
        
    }
    componentDidMount(){
        let fake_articles = this.getFakeArticles().articles;
        this.setState({
            articles_data: fake_articles,
        });
        // this.getArticles()
    }
    async getArticles() {
        axios.post(API_ENDPOINT_ARTICLES, {
            topic: this.state.topic,
            date: this.state.date
        }).then(function (response) {
            console.log(response);
            return response.data;
        }).then((data) => {
            this.setState({
                articles_data: data.articles
            })
        }).catch(function (error) {
            console.log(error);
        });
    }
    getFakeArticles() {
        return (
            {
                'topic': 'trump',
                'date': '2019-03-30',
                'articles': [
                    {
                        'title': 'Judge rules Trump executive order allowing offshore drilling in Arctic Ocean unlawful',
                        'url': 'https://www.cnn.com/2019/03/30/politics/trump-offshore-drilling-arctic/index.html',
                        'score': 8.9,
                    },
                    {
                        'title': 'Trump: Navy SEAL charged with murder moving to \'less restrictive confinement\'',
                        'url': 'https://www.cnn.com/2019/03/30/politics/donald-trump-eddie-gallagher/index.html',
                        'score': 6.4
                    }
                ],
            }
        )
    }
    render() {
        console.log('articles_data', this.state.articles_data)
        if(this.state.articles_data.length == 0){
            return (
                <div>Loading data ...</div>
            );
        }
        let articles_display = this.state.articles_data.map(({title, url, score}) => {
            return (
                <div>
                    <a href={url}>{title}</a> 
                    <div>{score}</div>
                </div>
            );
        });
        return (<div>
            <Title>{this.state.topic}</Title>
            <div>{this.state.date}</div>
            
            {articles_display}
        </div>);
    }
}

export default TopicView;