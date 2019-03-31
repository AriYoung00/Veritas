import React, { Component } from 'react';
import TopicView from './js/components/TopicView';
import './App.css';

class App extends Component {
  render() {
    return (
      <div className="App">
        <TopicView topic='trump' date='2019-3-30'></TopicView>
      </div>
    );
  }
}

export default App;
