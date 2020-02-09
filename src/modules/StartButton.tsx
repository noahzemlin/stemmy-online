  
import React from 'react';
import StemServer from '../controllers/ServerControllers';

interface IProps {

}

interface IState {

}

export default class StartButton extends React.Component<IProps, IState> {

    constructor(props: any) {
        super(props);

        this.handleClick = this.handleClick.bind(this);
    }

    handleClick(e: any) {
        StemServer.get().sendWithoutMessage('start');
    }

    render() {
        return (
            <p onClick={this.handleClick}>Start!</p>
        );
    }
}