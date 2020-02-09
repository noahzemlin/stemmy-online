import React from 'react';
import StemServer from './controllers/ServerControllers';

interface IProps {

}

interface IState {
    stemmyPic: string;
}

export default class Stemmy extends React.Component<IProps, IState> {

    constructor(props: any) {
        super(props);

        this.state = {stemmyPic: "assets/sad.png"};

        StemServer.get().onEvent('leaderboard').subscribe((data:any[]) => {
            let health: number = -50;
            data.forEach(e => {
                if (e[0] === 0) {
                    health = e[2];
                }
            });

            if (health >= -25 && health < 0) {
                this.setState({
                    stemmyPic: "assets/neutral.png"
                });
            }

            if (health >= 0) {
                this.setState({
                    stemmyPic: "assets/stemmy.gif"
                });
            }
          });
    }

    render() {
        return (
            <img src={this.state.stemmyPic} alt="Stemmy!"></img>
        );
    }
}