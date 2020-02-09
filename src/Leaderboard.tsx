  
import React from 'react';
import LeaderboardEntry from './modules/LeaderboardEntry';
import StemServer from './controllers/ServerControllers';

interface IProps {
}

interface IState {
    users: any[];
}

export default class Leaderboard extends React.Component<IProps, IState> {

  constructor(props:any) {
    super(props);

    this.state = {users: []};

    StemServer.get().onEvent('leaderboard').subscribe((data) => {
        this.setState({
            users: data
        });
      });
  }

  render() {

    const leaderboardJsx: any[] = [];

    this.state.users.forEach((element, index) => {
        leaderboardJsx.push(<LeaderboardEntry key={element[0]} sid={element[0]} name={element[1]} score={element[2]} place={index + 1}></LeaderboardEntry>);
    });

    return (
        <table id="leaderTable">
          <tbody>
            {leaderboardJsx}
          </tbody>
        </table>
    );
  }
}