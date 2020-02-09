import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';
import Leaderboard from './Leaderboard';
import StemServer from './controllers/ServerControllers';

const name: string = prompt("name") || "No Name";

StemServer.init(name);

ReactDOM.render(<Leaderboard />, document.getElementById('leaderTable'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
