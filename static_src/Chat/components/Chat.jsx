import React from 'react';
import {Media} from 'react-bootstrap';
import {connect} from 'react-redux';

import {showChat} from '../../Layout/actions/LayoutActions.jsx'

class Chat extends React.Component {

    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div className="chat-container" onClick={() => this.props.dispatch(showChat())}>
                <Media>
                    <Media.Body>
                        <p>{ this.props.content }</p>
                    </Media.Body>
                    <hr />
                </Media>
            </div>
        )
    }
}

Chat.propTypes = {
    content: React.PropTypes.string.isRequired,
};

Chat = connect()(Chat);
export default Chat;