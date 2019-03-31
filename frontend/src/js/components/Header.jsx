import React, { Component } from "react";
import Subtitle from './Subtitle';
class Header extends Component {
    render() {
        var imgStyle = {
            width: '300px',
        }
        return (
          <div className="App">
                <img src={require("./../../logo.png")}  style={imgStyle}></img>
          </div>
        );
    }
}
export default Header;