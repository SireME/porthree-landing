import React from "react";
import { Button } from "./PortfolioHero";


export function Title2() {
    return (
        <div className="w-full">
            <h2 className="text-3xl font-bold">Contact</h2>
        </div>
    )
}

function ContactIcon({ text }) {
    return (
        <div className="flex">
            <div className={`w-10 h-10 border ${text ? 'mr-2' : ''}`}></div>
            <div className="flex"><p className="m-auto">{text}</p></div>
        </div>
    );
}

function ContactForm() {
    return (
        <div>
            <form action="" method="post" className="grid gap-3">
                <div className="grid grid-cols-2 gap-2">
                    <div><input type="text" name="" id="" className="outline-none border-2 p-2 rounded w-full" placeholder="Name" /></div>
                    <div><input type="email" name="" id="" className="outline-none border-2 p-2 rounded w-full" placeholder="example@gmail.com" /></div>
                </div>
                <div>
                    <input type="text" name="" id="" className="outline-none border-2 p-2 rounded w-full" placeholder="Subject..." />
                </div>
                <div><textarea name="" id="" cols="30" rows="10" className="outline-none border-2 p-2 rounded w-full" placeholder="Enter message"></textarea></div>
                <div><Button value={'Send'} /></div>
            </form>
        </div>
    );
}

export default function Contact() {
    return (
        <div>
            <Title2 />
            <div className="grid grid-cols-2">
                <div className="grid gap-3">
                    <ContactIcon text={'icon text'} />
                    <ContactIcon text={'icon text'} />
                    <ContactIcon text={'icon text'} />
                    <ContactIcon text={'icon text'} />
                    <div className="flex w-full justify-center gap-2">
                        <ContactIcon />
                        <ContactIcon />
                        <ContactIcon />
                    </div>
                </div>
                <div>
                    <ContactForm />
                </div>
            </div>
        </div>
    )
}
