import {connect} from 'react-redux'
import React from 'react'

import {showMyPage, showFeed, showChats} from '../actions/LayoutActions.jsx'
import VerticalButtonBlock from '../components/VerticalButtonBlock.jsx'

const mapStateToProps = (state) => {
    const locked = !state.logOnHandle.logon;

    return {
        locked: locked,
    }
};


const mapDispatchToProps = (dispatch) => {
    return {
        onMyPageClick: () => {
            dispatch(showMyPage());
        },
        onFeedClick: () => {
            dispatch(showFeed());
        },
        onChatClick: () => {
            dispatch(showChats());
        }
    }
};

const VisibleVerticalButtonBlock = connect(mapStateToProps, mapDispatchToProps)(VerticalButtonBlock);
export default VisibleVerticalButtonBlock;