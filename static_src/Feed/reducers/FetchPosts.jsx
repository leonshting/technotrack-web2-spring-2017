import React from 'react'
import {REQUEST_POSTS, RECEIVE_POSTS} from '../actions/FetchPosts.jsx'

export const PostRequested = (state, action) => {
    if(state === undefined) {
        return {posts_received: false, posts_requested: false, user: 0};
    }

    switch (action.type) {
        case REQUEST_POSTS:
            return Object.assign({}, state, {posts_received: false, posts_requested: true, user: action.user});
        default:
            return state;
    }
};

export const PostReceived = (state, action) => {
    if(state === undefined) {
        return {posts_received: false, posts_requested: false, user: 0, posts: [], lastUpdated: 0};
    }

    switch (action.type) {
        case RECEIVE_POSTS:
            console.log(action);
            return Object.assign({}, state,
                {
                    posts_received: true,
                    user: action.user,
                    posts: action.posts,
                    lastUpdated: action.receivedAt
                });
        default:
            return state;
    }
};