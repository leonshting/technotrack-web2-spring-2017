import fetch from 'isomorphic-fetch'
const base64 = require('base-64');

import {fetchPosts} from './FetchPosts.jsx'
import {closeModal} from '../actions/ModalContainer.jsx'

export function createPost(user, data) {

    return function (dispatch) {

        const headers = new Headers();
        headers.append("Authorization", "Basic " + base64.encode("admin:getitnow"));
        headers.append('Content-Type', 'application/json; charset=utf-8');
        return fetch(`/api/post/`,
            {
                headers: headers,
                method: 'POST',
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(dispatch(closeModal()))
            .then(dispatch(fetchPosts(user)));
    }
}