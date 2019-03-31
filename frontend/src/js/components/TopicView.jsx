import React, { Component } from "react";
import { API_ENDPOINT_ARTICLES } from './../constants/CONFIG';
import Title from './Title';
import Subtitle from './Subtitle';
import StyledLink from './StyledLink'
import Header from './Header';
import styled from 'styled-components';
import ReactTable from "react-table";
import { formatDate } from '../util/formatDate';

const axios = require('axios');

const Wrapper = styled.div`
    text-align: left;
    margin-left: 200px;
    margin-top: 50px;
    margin-bottom: 30px;
`
const Score = styled.div`
    font-size: 2em;
`
class TopicView extends Component {
    constructor(props) {
        super(props);
        this.state = {
            topic: props.location.state.topic,
            date: props.location.state.date,
            articles_data: [],
        };
        this.getArticles = this.getArticles.bind(this)
    }
    componentDidMount() {
        // let fake_articles = this.getFakeArticles().articles;
        // this.setState({
        //     articles_data: fake_articles,
        // });
         this.getArticles()
    }
    async getArticles() {
        axios.get(API_ENDPOINT_ARTICLES, {
            params: {
                topic: this.state.topic,
                date: this.state.date
            }
        }).then(function (response) {
            console.log(response)
            return response.data;
        }).then((data) => {
            this.setState({
                articles_data: data,
            })
            console.log(this.state.articles_data);
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

    renderScoreColor(score) {
        if (score > 5)
            return '#1ebf44'
        else 
            return '#c12f1f'
    }

    render() {
        console.log('articles_data', this.state.articles_data)
        if (this.state.articles_data == null) {
            return (
                <div>Loading data ...</div>
            );
        }

        let articles_display = this.state.articles_data.map(({ title, url, score }) => {
            return (
                <div style={{width: '1500px', 'padding-left': '15em', 'padding-bottom': '1em'}}>
                    <div style={{ display: 'inline-block', width: '90%'}}>
                        <StyledLink href={url}>{title}</StyledLink>
                    </div>
                    <div style={{ float: 'right', width: '10%'}}>
                        <Score style={{ color: this.renderScoreColor(score) }}>{score}</Score>
                    </div>
                </div>
            );
        });
        return (<div>
            <Header />
            <Wrapper>
                <Title>Topic: {this.state.topic}</Title>
                <Subtitle>Date: {formatDate(this.state.date)}</Subtitle>
            </Wrapper>
            <div style={{'padding-bottom': '5em'}}>
                {articles_display}
            </div>
        </div>);
    }
}

export default TopicView;