/**
 * Created by leonshting on 26.03.17.
 */
import React from 'react';
import {Media} from 'react-bootstrap';
import {connect} from 'react-redux';
import {openModal} from '../actions/ModalContainer.jsx'

class Post extends React.Component {

    constructor(props) {
        super(props);
    }


    render() {
        return (
            <div className="post-container" onClick={() => {
                if (!this.props.modalMounted)
                    return this.props.dispatch(openModal(
                        <Post content={this.props.content} author={this.props.author} modalMounted={ true }/>))
                else
                    return null;
            }}>
                <Media>
                    <Media.Body>
                        <Media.Heading>{ this.props.author.username }</Media.Heading>
                        <p>{ this.props.content }</p>
                    </Media.Body>
                    <hr />
                </Media>
            </div>
        )
    }
}

Post.propTypes = {
    content: React.PropTypes.string.isRequired,
    author: React.PropTypes.shape(
        {
            username: React.PropTypes.string.isRequired
        }
    ),
    modalMounted: React.PropTypes.bool
};

Post = connect()(Post);
export default Post;
