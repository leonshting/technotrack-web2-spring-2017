import React from 'react';
import {Button} from 'react-bootstrap';
import {connect} from 'react-redux'

import Post from './Post.jsx'
import {openModal} from '../actions/ModalContainer.jsx'
import {fetchPosts} from '../actions/FetchPosts.jsx'

const POST_TEXT = 'dsfsadhafkldshfljdkhfadskljfhjdskhfndsfsadhafkldshfljdkhfadskljfhjdskhfdsfsadhafkldshfljdkhfadskljfhjdskhf';
const owner = {
    name: 'пипка',
    avaURL: 'c'
};

const posts = [
    {id: 1, content: POST_TEXT, owner: owner},
    {id: 2, content: POST_TEXT, owner: owner},
    {id: 3, content: POST_TEXT, owner: owner},
    {id: 4, content: POST_TEXT, owner: owner},
    {id: 5, content: POST_TEXT, owner: owner},
    {id: 6, content: POST_TEXT, owner: owner},
    {id: 7, content: POST_TEXT, owner: owner},
    {id: 8, content: POST_TEXT, owner: owner},

];

class PostList extends React.Component {

    componentWillMount = () => {
        this.props.onMount();
    };

    render() {
        console.log(this.props.posts);
        const POST_LIST = this.props.posts.map(
            (post) => <Post key={ post.pk } author={ post.author } content={ post.content } modalMounted={ false }/>);

        return (
            <div>
                <Button onClick={this.props.onRefresh}>Fetch New</Button>
                <div className="post-list">
                    <Button onClick={(e) => {
                        e.preventDefault();
                        this.props.dispatch(openModal(null));
                    }}>New Post</Button>
                    { POST_LIST }
                </div>
            </div>
        )
    }
}

PostList.propTypes = {
    user_id: React.PropTypes.number.isRequired,
    user_only: React.PropTypes.bool.isRequired,
    onMount: React.PropTypes.func,
    onRefresh: React.PropTypes.func,
};

PostList = connect()(PostList);
export default PostList;