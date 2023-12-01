import { useState } from "react"
import { Link } from "react-router-dom"


function SignUpForm() {
    let data = ""
    const [formData, setFormData] = useState({
        FirstName: '',
        LastName: '',
        username: '',
        email: '',
        password: '',
        Password2: '',
    });

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: value,
        }));
    };
}
const handleSubmit = async (e) => {
    e.preventDefault();
    try {
        const response = await axios.post('http://example.com/api/register', formData);
        console.log('Registration successful:', response.data);
    } catch (error) {
        console.error('Registration failed:', error.response.data);
    }
}
return (
    <div className="border bg-blue bg-opacity-70 py-10 px-5 absolute align-self-middle m-auto rounded-xl grid justify-center text-center gap-y-3">
        <div className="font-bold text-2xl">Porthree</div>
        <div className=""><p className="text-sm font-bold">Login to your porthree Dashboard</p></div>
        <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Google</button></div>
        <div className="border rounded-xl font-bold flex justify-center gap-5 py-px"><div className="border rounded-full w-6 h-6"></div><button>Continue with Linkedin</button></div>
        <div className="flex items-center justify-center gap-2">
            <div className="border-b-4 w-1/3"></div>
            OR
            <div className="border-b-4 w-1/3"></div>
        </div>
        <div>
            <form action="" method="get" className="grid grid-cols-1 gap-2">
                <div className="grid grid-cols-2 gap-2">
                    <input type="text" name="FirstName" value={FormData.FirstName} onChange={handleChange} placeholder="First Name" className="rounded px-5 h-8 w-full outline-0" />
                    <input type="text" name="LastName" value={FormData.LastName} onChange={handleChange} placeholder="Last Name" className="rounded px-5 h-8 w-full outline-0" />
                </div>
                <div>
                    <input type="text" name="username" value={FormData.username} onChange={handleChange} id="" placeholder="User Name" className="rounded px-5 h-8 w-full outline-0" />
                </div>
                <div>
                    <input type="email" name="email" value={FormData.email} onChange={handleChange} id="" placeholder="example@gmail.com" className="rounded px-5 h-8 w-full outline-0" />
                </div>
                <div>
                    <input type="password" name="password" value={FormData.password} onChange={handleChange} id="" placeholder="Password" className="rounded px-5 h-8 w-full outline-0" />
                </div>
                <div>
                    <input type="password" name="Password2" value={FormData.Password2} onChange={handleChange} id="" placeholder="Confirm Password" className="rounded px-5 h-8 w-full outline-0" />
                </div>
                <p className="font-xs">Already have account with Porthree? <Link className="font-medium" to={`/`}>Login</Link></p>
                <button type="submit" className="border rounded font-bold">Create Account</button>
            </form>
        </div>
    </div>
)
}

function Forms2() {
    return (

        <div className={`fixed flex justify-center items-center h-screen w-full bg-transparent z-10`}>
            <SignUpForm />
        </div>
    )
}

export default Forms2