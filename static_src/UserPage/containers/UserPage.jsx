import {connect} from 'react-redux'
import React from 'react'
import UserPage from '../components/UserPage.jsx'
import {fetchUser} from '../actions/FetchUserInfo.jsx'


const mapStateToProps = (state) => {
    return {
        username: state.userReceived.username,
        user_id_fetched: state.userReceived.user_id,
        email: ''
    }
};

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onMount: () => {
            dispatch(fetchUser(ownProps.user_id));
        }
    }
};
const VisibleUserPage = connect(mapStateToProps, mapDispatchToProps)(UserPage);
export default VisibleUserPage;