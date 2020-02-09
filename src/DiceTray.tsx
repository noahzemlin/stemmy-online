  
import React from 'react';
import StemServer from './controllers/ServerControllers';

interface IProps {
}

interface IState {
    dice: number[]
}

export default class DiceTray extends React.Component<IProps, IState> {

  constructor(props:any) {
    super(props);

    this.state = {dice: [3, 1, 4]};

    StemServer.get().onEvent('new_dice').subscribe((data) => {
        this.setState({
            dice: data
        });
      });
  }

  render() {

    const diceJsx: any[] = [];

    this.state.dice.forEach(element => {
        diceJsx.push(<div key={element} id="dice"><img src={"assets/" + element + "yellow.png"} alt={"a die with " + element + " on it"}></img></div>);
    });

    return (
        <div id="diceBox">
            <br/>
            <br/>
            {diceJsx}
        </div>
    );
  }
}