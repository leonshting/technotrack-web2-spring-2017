import React from 'react'
import {connect} from 'react-redux'

import VisiblePostList from '../../Feed/containers/PostList.jsx'
import {fetchUser} from '../actions/FetchUserInfo.jsx'

class UserPage extends React.Component {

    constructor(props) {
        super(props);
    }

    componentWillMount = () => {
        this.props.onMount();
    };

    render() {
        console.log(this.props);
        return (
            <div>
                { this.props.username }
                <VisiblePostList user_id={this.props.user_id} user_only={true}/>
            </div>

        );
    }
}

UserPage.propTypes =
    {
        user_id: React.PropTypes.number.isRequired,
        onMount: React.PropTypes.func,
    };


export default UserPage;