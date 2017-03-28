import React from 'react';
import {Media} from 'react-bootstrap';
import {connect} from 'react-redux';
import Message from './Message.jsx'

export class ChatExpanded extends React.Component {

    constructor(props) {
        super(props);
    }


    render() {
        console.log(this.props);
        return (
            <div className="chat-container">
                <Media>
                    <Media.Body>
                        <p>{ this.props.content }</p>
                    </Media.Body>

                    { this.props.messages.map(
                        (message, i) => <Message key={ i } content={ message.content }/>) }
                    <hr />
                </Media>
            </div>
        )
    }
}

//make it required later
ChatExpanded.propTypes = {
    id: React.PropTypes.number,
    content: React.PropTypes.string,
    messages: React.PropTypes.array,
};