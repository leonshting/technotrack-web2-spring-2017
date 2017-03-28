/**
 * Created by leonshting on 23.03.17.
 */

import ReactDOM from 'react-dom';
import React from 'react';
import {Provider} from 'react-redux'
import {applyMiddleware, createStore, combineReducers} from 'redux'
import thunkMiddleware from 'redux-thunk'
import logger from 'redux-logger'
import 'babel-polyfill'

import modalVisibilityReducer from './Feed/reducers/ModalContatiner.jsx'
import {PostRequested, PostReceived} from './Feed/reducers/FetchPosts.jsx'
import {logOnHandle} from './Auth/reducers/LoginReducers.jsx'
import {showWindow} from './Layout/reducers/Layout.jsx'
import {userReceived} from './UserPage/reducers/FetchUserInfo.jsx'

import App from './app.jsx'

const initialState = {
    modalVisibilityReducer: {showModal: false, modal_element: null},
    logOnHandle: {logon: false, username: '', token: ''},
    showWindow: {currently_shown: ''},
    userReceived: {user_id: -1, username: '', email: '',  lastUpdated: 0}
};

let reducers = combineReducers(
    {
        modalVisibilityReducer,
        PostReceived,
        PostRequested,
        logOnHandle,
        showWindow,
        userReceived,
    }
);

let store = createStore(
    reducers,
    initialState,
    applyMiddleware(
        thunkMiddleware,
        logger
    )
);

ReactDOM.render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);