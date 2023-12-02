import React, { useState, useEffect } from "react";
import {
    Button,
    Modal,
    ModalHeader,
    ModalBody,
    ModalFooter,
    Form,
    FormGroup,
    Input,
    Label,
} from "reactstrap";

/**
 * supposed to handle user data and interaction with api
 */
const CustomModal = (props) => {
    const [activeItem, setActiveItem] = useState(props.activeItem);

    /**
     * selected todo item to be edited
     */
    useEffect(() => {
        setActiveItem(props.activeItem);
    }, [props.activeItem]);

    /**
     * handles change in form
     */
    const handleChange = (e) => {
        let { name, value } = e.target;

        if (e.target.type === "checkbox") {
            value = e.target.checked;
        }

        const updatedItem = { ...activeItem, [name]: value };
        setActiveItem(updatedItem);
    };
    /**
     * toggle : is a function used to control the Modal’s state (i.e., open or close the modal).
     * onSave : is a function that is called to save the edited values of the Todo item.
    */
    const { toggle, onSave } = props;

    return (
        <Modal isOpen={true} toggle={toggle}>
            <ModalHeader toggle={toggle}>Todo Item</ModalHeader>
            <ModalBody>
                <Form>
                    <FormGroup>
                        <Label for="todo-title">Title</Label>
                        <Input
                            type="text"
                            id="todo-title"
                            name="title"
                            value={activeItem.title}
                            onChange={handleChange}
                            placeholder="Enter Todo Title"
                        />
                    </FormGroup>
                    <FormGroup>
                        <Label for="todo-description">Description</Label>
                        <Input
                            type="text"
                            id="todo-description"
                            name="description"
                            value={activeItem.description}
                            onChange={handleChange}
                            placeholder="Enter Todo description"
                        />
                    </FormGroup>
                    <FormGroup check>
                        <Label check>
                            <Input
                                type="checkbox"
                                name="completed"
                                checked={activeItem.completed}
                                onChange={handleChange}
                            />
                            Completed
                        </Label>
                    </FormGroup>
                </Form>
            </ModalBody>
            <ModalFooter>
                <Button color="success" onClick={() => onSave(activeItem)}>
                    Save
                </Button>
            </ModalFooter>
        </Modal>
    );
};

export default CustomModal;
