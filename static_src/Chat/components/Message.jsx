import React from 'react';
import {Media} from 'react-bootstrap';
import {connect} from 'react-redux';

class Message extends React.Component {
    constructor(props) {
        super(props);
    }

    render() {
        return <div>
            {this.props.content}
        </div>
    }
}

Message.propTypes = {
    content: React.PropTypes.string.isRequired,
};

export default Message;