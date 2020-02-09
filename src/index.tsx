import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import Leaderboard from './Leaderboard';
import StemServer from './controllers/ServerControllers';
import SubmitForm from './SubmitForm';
import DiceTray from './DiceTray';
import StartButton from './modules/StartButton';
import Stemmy from './Stemmy';

const name: string = prompt("name") || "No Name";

StemServer.init(name);

ReactDOM.render(<SubmitForm />, document.getElementById('textBoxFiller'));
ReactDOM.render(<DiceTray />, document.getElementById('diceBoxFiller'));
ReactDOM.render(<Leaderboard />, document.getElementById('leaderTableFiller'));
ReactDOM.render(<StartButton />, document.getElementById('button'));
ReactDOM.render(<Stemmy />, document.getElementById('stemmy'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
