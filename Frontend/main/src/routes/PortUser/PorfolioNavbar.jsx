import React from "react";

function NavBar() {
    return (
        <div className="flex justify-between items-center px-10 fixed border w-full">
            <div className=" text-2xl font-bold">UserName</div>
            <div><ul className="flex gap-10">
                <li className="hover:font-medium"><a href="">Home</a></li>
                <li className="hover:font-medium"><a href="">About</a></li>
                <li className="hover:font-medium"><a href="">Projects</a></li>
                <li className="hover:font-medium"><a href="">Posts</a></li>
                <li className="hover:font-medium"><a href="">Contact</a></li>
            </ul></div>
        </div>
    )
}
export default NavBar;
