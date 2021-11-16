import React from 'react';
import ReactDOM from 'react-dom';
import { Provider } from 'react-redux';


import './index.css';
import App from './App';
import configureStore from './store';
const store = configureStore();

//rendering a virtual dom that will show on DOM
ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}> 
      <App />
    </Provider> 
  </React.StrictMode>,
  //connects virtual dom to 'root' js and browser handshake
  document.getElementById('root')
);

