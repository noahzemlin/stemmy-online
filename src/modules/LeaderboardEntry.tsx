  
import React from 'react';

interface IProps {
    sid: string;
    name: string;
    score: number;
}

interface IState {

}

export default class LeaderboardEntry extends React.Component<IProps, IState> {
  render() {
    const style={
        backgroundPosition: "0px -48px"
    }
    return (
        <tr>
            <td><div className="sun" style={style}></div></td>
            <td>{this.props.name}</td>
            <td>{this.props.score}</td>
        </tr>
    );
  }
}