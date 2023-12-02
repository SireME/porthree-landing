import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import axios from 'axios';

function SignTop() {
    return (
        <>
            <div className="font-bold text-2xl">Porthree</div>
            <div className=""><p className="text-sm font-bold">Login to your porthree Dashboard</p></div>
            <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Google</button></div>
            <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Linkedin</button></div>
            <div className="flex items-center justify-center gap-2">
                <div className="border-b-4 w-1/3"></div>
                OR
                <div className="border-b-4 w-1/3"></div>
            </div>
        </>
    )
}


function SignUpForm(props) {
    /* this is to set the current ser state */
    const [currentUser, setCurrentUser] = useState(props.currentUser);

    /* implementing the seUser function effect */
    useEffect(() => {
        setCurrentUser(props.currentUser);
    }, [props.currentUser]);

    /* handles form change */
    const handleChange = (e) => {
        let { name, value } = e.target;

        /* this is not currently useful */
        if (e.target.type === "checkbox") {
            value = e.target.checked;
        }
        /* update item on change */
        const updatedUser = { ...currentUser, [name]: value };
        setCurrentUser(updatedUser);
    };

    const { toggle, onSave } = props;

    return (
        <div className="border bg-blue bg-opacity-70 py-10 px-5 absolute align-self-middle m-auto rounded-xl grid justify-center text-center gap-y-3">
            <SignTop />
            <div>
                <form className="grid grid-cols-1 gap-2">
                    <div className="grid grid-cols-2 gap-2">
                        <input type="text" name="first_name" id="first_name" value={currentUser.first_name} onChange={handleChange} placeholder="First Name" className="rounded px-5 h-8 w-full outline-0" />
                        <input type="text" name="last_name" id="last_name" value={currentUser.last_name} onChange={handleChange} placeholder="Last Name" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="text" name="user_name" id="user_name" value={currentUser.user_name} onChange={handleChange} placeholder="User Name" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="email" name="email" id="email" value={currentUser.email} onChange={handleChange} placeholder="example@gmail.com" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="password" name="password" id="password" value={currentUser.password} onChange={handleChange} placeholder="Password" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <p className="font-xs">Already have account with Porthree? <Link className="font-medium" to={`/`}>Login</Link></p>
                    <button type="submit" className="border rounded font-bold" onClick={() => onSave(currentUser)}>Create Account</button>
                </form>
            </div>
        </div>
    )
}

export default function Forms2() {
    const [currentUser, setCurrentUser] = useState({
        first_name: "",
        last_name: "",
        user_name: "",
        email: "",
        password: "",
    });

    const handleSubmit = (item) => {
        axios.post("http://127.0.0.1:8000/api/User/", item)
        .then(response => {
            // Handle the response, if needed
            console.log(response);
        })
    };


    const createUser = () => {
        const data = { first_name: "", last_name: "", user_name: "", email: "", password: "", };
        setCurrentUser(data);
    };

    return (

        <div className={`fixed flex justify-center items-center h-screen w-full bg-transparent z-10`}>
            <SignUpForm  currentUser={currentUser} onSave={handleSubmit} />
        </div>
    )
}
