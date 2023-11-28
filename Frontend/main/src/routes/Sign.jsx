import { Link } from "react-router-dom"


function SignUpForm() {
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
            <div className="grid grid-cols-1 items-center gap-2">
                <div className="h-40 w-40 border justify-self-center rounded-full"></div>
                <button className="border font-medium">Upload image</button>
            </div>
            <div>
                <form action="" method="get" className="grid grid-cols-1 gap-2">
                    <div className="grid grid-cols-2 gap-2">
                        <input type="text" placeholder="First Name" className="rounded px-5 h-8 w-full outline-0" />
                        <input type="text" placeholder="Last Name" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="text" name="username" id="" placeholder="User Name" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    <div>
                        <input type="password" name="email" id="" placeholder="Password" className="rounded px-5 h-8 w-full outline-0" />
                    </div>
                    {/* <div className="justify-self-start">
                        <input type="checkbox" name="remember" id="" />
                    </div> */}
                    <p className="font-xs">Already have account with Porthree? <Link className="font-medium" to={`/`}>Login</Link></p>
                    <button type="submit" className="border rounded font-bold">Create Acount</button>
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