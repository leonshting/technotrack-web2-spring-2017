import React from 'react';
import VisibleVerticalButtonBLock from '../containers/VerticalButtonBlock.jsx'
import Header from './Header.jsx'

import Login from '../../Auth/components/LoginForm.jsx'
import VisiblePostList from '../../Feed/containers/PostList.jsx'
import VisibleUserPage from '../../UserPage/containers/UserPage.jsx'
import ChatList from '../../Chat/components/ChatList.jsx'
import {ChatExpanded} from '../../Chat/components/ChatExpanded.jsx'

const chat = {
    id: 1,
    content: 'dfsdfsdfsdfsd',
    messages: [
        {content: 'dsfsdfsddfdsfdf'},
        {content: 'dsfsdfsddfdsfdf'},
        {content: 'dsfsdfsddfdsfdf'},
        {content: 'dsfsdfsddfdsfdf'},
        {content: 'dsfsdfsddfdsfdf'},
        {content: 'dsfsdfsddfdsfdf'},
    ]
};


class Layout extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            currently_shown: ''
        }
    }

    componentWillReceiveProps = (nextProps) => {
        this.setState(
            {
                currently_shown: nextProps.currently_shown,
            }
        );
    };

    choose_view = () => {
        switch (this.props.currently_shown) {
            case 'login':
                return (<Login />);
            case 'feed':
                return (<VisiblePostList user_id={1} user_only={false}/>);
            case 'mypage':
                return (<VisibleUserPage user_id={1}/>);
            case 'chats':
                return (<ChatList />);
            case 'chat':
                return (<ChatExpanded id={chat.id} content={chat.content} messages={chat.messages}/>);
            default:
                return (<Login />)
        }
    };

    render() {
        return <div>
            <Header/>
            <div className="layout-container">
                <VisibleVerticalButtonBLock />
                <div>{this.choose_view()}</div>
            </div>
        </div>
    }

}

export default Layout;