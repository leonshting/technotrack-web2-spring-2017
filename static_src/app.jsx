import React from 'react'

import VisibleModalContainer from './Feed/containers/ModalContainer.jsx';
import VisibleLayout from './Layout/containers/Layout.jsx';
import Login from './Auth/components/LoginForm.jsx';
import VisiblePostList from './Feed/containers/PostList.jsx';
import {doLogin} from './Auth/actions/LoginActions.jsx'


const App = () => {
    return (
        <div>
            <VisibleLayout />
            <VisibleModalContainer />
        </div>
    )
};

export default App;