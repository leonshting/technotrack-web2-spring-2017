import fetch from 'isomorphic-fetch'
const base64 = require('base-64');

export const FETCH_POST_REQUEST = {type: 'FETCH_POSTS_REQUEST'};
export const FETCH_POSTS_FAILURE = {type: 'FETCH_POSTS_FAILURE'};
export const FETCH_POSTS_SUCCESS = {type: 'FETCH_POSTS_SUCCESS'};

export const REQUEST_POSTS = 'REQUEST_POSTS';

function requestPosts(user_id) {
    return {
        type: REQUEST_POSTS,
        user: user_id,
    }
}

export const RECEIVE_POSTS = 'RECEIVE_POSTS';

function receivePosts(user_id, json, user_only) {
    console.log(json);
    return {
        type: RECEIVE_POSTS,
        user: user_id,
        posts: json.results,
        user_only: user_only,
        receivedAt: Date.now()
    }
}


export function fetchPosts(user_id, user_only=true) {

    return function (dispatch) {

        dispatch(requestPosts(user_id));

        const headers = new Headers();
        headers.append("Authorization", "Basic " + base64.encode("admin:getitnow"));
        const filter = user_only? `?author=${user_id}` : '';
        return fetch(`/api/post/${filter}`, {headers: headers})
            .then(response => response.json())
            .then(json => dispatch(receivePosts(user_id, json, user_only))
            );
    }
}