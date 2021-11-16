import React from 'react';
import {BrowserRouter, Route, Switch} from 'react-router-dom';

// import ReadingPage from './components/ReadingPage';
import Library from './components/library/Library';

function App() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path='/library'>
          <Library/>
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default App;
