import React from 'react'
import {Modal} from 'react-bootstrap'
import Post from './Post.jsx'
import PostForm from './PostForm.jsx'


class ModalContainer extends React.Component {

    constructor(props) {
        super(props);

    }

    render() {
        const element = (this.props.element === null)? <PostForm />: this.props.element;
        return (
            <div className="modal-container">
                <Modal show={this.props.opened}
                       onHide={() => this.props.onCloseModal()}>
                    <Modal.Header closeButton>
                        <Modal.Title>{(this.props.element === null)? 'Create Post' : ''}</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                        {element}
                    </Modal.Body>
                </Modal>
            </div>
        );
    }
}

ModalContainer.propTypes = {
    onOpenModal: React.PropTypes.func.isRequired,
    onCloseModal: React.PropTypes.func.isRequired,
    opened: React.PropTypes.bool,
    id: React.PropTypes.number
};

export default ModalContainer;