  
import React from 'react';

interface IProps {
    sid: string;
    name: string;
    score: number;
    place: number;
}

interface IState {

}

export default class LeaderboardEntry extends React.Component<IProps, IState> {
  render() {
    const style={
        backgroundPosition: "0px -48px"
    }
    let position = "sun";
    switch(this.props.place) {
      case 1: position = "first"; break;
      case 2: position = "second"; break;
      case 3: position = "third"; break;
    }
    return (
        <tr>
            <td><div className={position} style={style}></div></td>
            <td>{this.props.name}</td>
            <td>{this.props.score}</td>
        </tr>
    );
  }
}