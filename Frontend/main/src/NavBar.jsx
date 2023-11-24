import './App.css'

function NavLinks() {
    return(
        <div>
                <ul className='flex gap-5 font-medium sm:bg-red'>
                    <li className='hover:underline'><a href="#">Home</a></li>
                    <li className='hover:underline'><a href="#">About</a></li>
                    <li className='hover:underline'><a href="#">Contact</a></li>
                </ul>
            </div>
    )
}

function Logo() {
    return(
        <div className='font-bold text-blue-900 text-2xl'><a href="#">Porthree</a></div>
    )
}

function Login() {
    return(
    <div className='border border-slate-800 px-2 py-1rounded-lg'>
        <button>signup/Login</button>
    </div>
    )
}

function NavSearch() {
    return(
    <div className='flex align-center p-1 rounded-lg'>
        <select name="tags" id="tags" className='border outline-0 max-h-6 text-center'>
            <option value="volvo">tags</option>
            <option value="saab">developer</option>
            <option value="mercedes">software Engineer</option>
            <option value="audi">Video editor</option>
        </select>
        <input type='text' placeholder='Search here...' className='p-1 h-6 outline-0 border-b font-medium' /> 
        <button className='border border-slate-300 px-2 h-6 rounded-r'>Search</button>
    </div>
    )
}

export default function NavBar(){
    return(
        <div className='flex items-baseline justify-between align-center border-b px-20 py-4 fixed w-full bg-blue bg-opacity-50'>
            <Logo />
            <NavLinks />
            <NavSearch />
            <Login />
        </div>
    )
}
