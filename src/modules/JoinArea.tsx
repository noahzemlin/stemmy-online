  
import React from 'react';
import StemServer from '../controllers/ServerControllers';

interface IProps {

}

interface IState {
    name: string;
    room: string;
    inRoom: string;
}

export default class JoinArea extends React.Component<IProps, IState> {

    constructor(props: any) {
        super(props);

        this.state = {name: "", room: "", inRoom: ""}

        this.handleClick = this.handleClick.bind(this);
        this.handleNameChange = this.handleNameChange.bind(this);
        this.handleRoomChange = this.handleRoomChange.bind(this);
        this.handleStartClick = this.handleStartClick.bind(this);
        this.handleLeaveClick = this.handleLeaveClick.bind(this);

        StemServer.get().onEvent("joined_room").subscribe((data) => {
            let prevState = {...this.state};
            prevState.inRoom = data;
            this.setState(prevState);
          });
    }

    handleNameChange(e: any) {
        let prevState = {...this.state};
        prevState.name = e.target.value;
        this.setState(prevState);
    }

    handleRoomChange(e: any) {
        let prevState = {...this.state};
        prevState.room = e.target.value;
        this.setState(prevState);
    }

    handleClick(e: any) {
        e.preventDefault();
        StemServer.get().send('join_room', [this.state.name, this.state.room]);
    }

    handleStartClick(e: any) {
        StemServer.get().sendWithoutMessage('start');
    }

    handleLeaveClick(e: any) {
        // this is horrible lol, just leave by refreshing the page
        window.location.reload();
    }

    render() {
        if (this.state.inRoom !== "") {
            return (
                <div>
                    <p>Room code: {this.state.inRoom}</p>
                    <button onClick={this.handleStartClick}>Start!</button>
                    <button onClick={this.handleLeaveClick}>Leave</button>
                </div>
            );
        } else {
            return (
                <form id="joinForm">
                    Your Name: <input type="text" id="name" onChange={this.handleNameChange}></input>
                    Room Name: <input type="text" id="room" onChange={this.handleRoomChange}></input>
                    <br />
                    <button onClick={this.handleClick}>Join Room!</button>
                </form>
            );
        }
    }
}