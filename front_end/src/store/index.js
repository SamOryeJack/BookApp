import {createStore, combineReducers, applyMiddleware, compose} from 'redux';
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk'
import bookReducer from './books'


// connects python in bookv2 to js
const rootReducer = combineReducers({
    book: bookReducer
})
let enhancer
if (process.env.NODE_ENV === 'production'){
    enhancer = applyMiddleware(thunk)
} else {
    const logger = require('redux-logger').default
    const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || composeWithDevTools()
    enhancer = composeEnhancers(applyMiddleware(thunk, logger))
}

const configureStore = (preloadedState) => {
    return createStore(rootReducer, preloadedState, enhancer)
}

export default configureStore