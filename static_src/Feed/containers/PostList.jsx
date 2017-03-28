import {connect} from 'react-redux'
import React from 'react'
import PostList from '../components/PostList.jsx'
import {fetchPosts} from '../actions/FetchPosts.jsx'

const mapStateToProps = (state) => {
    const posts = state.PostReceived.posts;
    return {
        posts: posts
    }

};

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onMount: () => {
            console.log('shitshit');
            dispatch(fetchPosts(ownProps.user_id, ownProps.user_only));
        },
        onRefresh: () => {
            dispatch(fetchPosts(ownProps.user_id, ownProps.user_only));
        }
    }
};

const VisiblePostList = connect(mapStateToProps, mapDispatchToProps)(PostList);
export default VisiblePostList;