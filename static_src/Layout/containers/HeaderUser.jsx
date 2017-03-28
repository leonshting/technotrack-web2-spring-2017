import {connect} from 'react-redux'
import React from 'react'

import HeaderUser from '../components/HeaderUser.jsx'
import {showLogin} from '../actions/LayoutActions.jsx'

const mapStateToProps = (state) => {
    const logon = state.logOnHandle.logon;
    const username = state.logOnHandle.username;

    return {
        logon: logon,
        username: username
    }
};

const mapDispatchToProps = (dispatch) => {
    return {
        onLoginClick: () => {
            dispatch(showLogin());
        }
    }
};


const VisibleHeaderUser = connect(mapStateToProps, mapDispatchToProps)(HeaderUser);
export default VisibleHeaderUser;