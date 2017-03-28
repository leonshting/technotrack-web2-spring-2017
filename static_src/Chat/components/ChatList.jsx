import React from 'react';
import {Button} from 'react-bootstrap';
import {connect} from 'react-redux';
import Chat from './Chat.jsx'

const CHAT_NAME = 'dssdfdsfds';

const chats = [
    {id: 1, content: CHAT_NAME},
    {id: 2, content: CHAT_NAME},
    {id: 3, content: CHAT_NAME},
    {id: 4, content: CHAT_NAME},
    {id: 5, content: CHAT_NAME},
    {id: 6, content: CHAT_NAME},
    {id: 7, content: CHAT_NAME},
    {id: 8, content: CHAT_NAME},

];

class ChatList extends React.Component {

    render() {
        const CHAT_LIST = chats.map(
            (chat) => <Chat key={ chat.id } content={ chat.content } />);

        return (
            <div>
                <div className="chat-list">
                    { CHAT_LIST }
                </div>
            </div>
        )
    }
}

export default ChatList;