  
import React from 'react';
import StemServer from './controllers/ServerControllers';

interface IProps {

}

interface IState {
  dice: string[];
}

export default class DiceTray extends React.Component<IProps, IState> {

  constructor(props:any) {
    super(props);

    this.state = {dice: ["roll.gif", "rollAgain.gif", "rolling.gif"]};

    StemServer.get().onEvent('new_dice').subscribe((data: number[]) => {
        this.setState({
          dice: ["roll.gif", "rollAgain.gif", "rolling.gif"]
        });

        let dice: string[] = [];

        data.forEach(element => {
          dice.push(element + "yellow.png")
        });

        setTimeout(() => {this.setState({dice})}, 1000);
      });
  }

  componentDidMount() {
    const pics = ["assets/1yellow.png","assets/2yellow.png","assets/3yellow.png","assets/4yellow.png","assets/5yellow.png","assets/6yellow.png"]
    pics.forEach((picture) => {
        const img = new Image();
        img.src = picture;
    });
}

  render() {

    const diceJsx: any[] = [];

    this.state.dice.forEach((element, index) => {
        diceJsx.push(<div key={index} id="dice" ><img src={"assets/" + element} alt={"a die with " + element + " on it"}></img></div>);
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