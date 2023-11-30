import React from "react";

function NavBar() {
    return (
        <div className="flex flex-wrap justify-between items-center px-20 fixed border-b w-full h-20">
            <div className=" text-4xl font-bold">UserName</div>
            <div><ul className="flex gap-10 text-xl">
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
