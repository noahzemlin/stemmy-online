  
import React from 'react';
import StemServer from './controllers/ServerControllers';

interface IProps {
}

interface IState {
    value: string;
}

export default class SubmitForm extends React.Component<IProps, IState> {

  constructor(props:any) {
    super(props);

    this.state = {value: ""};

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(e: any) {
    this.setState({value: e.target.value});
  }

  handleSubmit(e: any) {
    e.preventDefault();
    StemServer.get().send('receive_answer', parseInt(this.state.value));
  }

  render() {
    return (
        <div id="textBox">
            <br/>
            <br/>
    
            <label>Sum up the dice and enter the result:</label>
            <p></p>
            <form onSubmit={this.handleSubmit} onChange={this.handleChange}>
                <input type="text"/>
            </form>
        </div>
    );
  }
}