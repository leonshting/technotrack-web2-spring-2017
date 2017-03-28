import React from 'react'
import {Button, FormGroup, FormControl, ControlLabel} from 'react-bootstrap'
import {connect} from 'react-redux';
import {createPost} from '../actions/CreatePost.jsx'


class PostForm extends React.Component {

    constructor(props) {
        super(props);
        this.state = {value: ''};
    }

    handleChange = (e) => {
        this.setState({value: e.target.value});
    };

    render() {
        return (
            <form>
                <FormGroup
                    controlId="post-form">
                    <ControlLabel>Submit New Post</ControlLabel>
                    <FormControl type="text"
                                 placeholder="Enter the content of your new post"
                                 value={this.state.value}
                                 onChange={this.handleChange}
                    />
                    <FormControl.Feedback />
                </FormGroup>
                <Button type="submit" onClick={(e) => {
                    e.preventDefault();
                    this.props.dispatch(createPost(0, {content: this.state.value}));
                }}>
                    Send Post!!!!!!
                </Button>
            </form>
        )
    }
}

PostForm = connect()(PostForm);
export default PostForm;