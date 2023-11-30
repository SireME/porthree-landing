import React from "react"
import { Get } from "./About"
export function Question({ param }) {
    return (<div className="border-2 rounded p-2 w-3/4 text-center justify-self-center"><p>{param}</p></div>)
}
export function Answer({ param }) {
    return (<div className="border rounded p-2 w-3/4 justify-self-center"><p>{param}</p></div>)
}

export default function Faq() {
    const url = 'http://127.0.0.1:8000/api/PothreeFAQ/';
    const data = Get({ url });
    if(!data){
        return('NULL')
    }
    return (
        <div className='grid grid-cols-1 gap-20 px-20'>
            <div className='text-center font-black text-5xl'><h1>Frequently Asked Questions <br /> (FAQ)</h1></div>
            <div className="w-full grid gap-4 justify-center">
                {data.map((item, index) => (
                <div className="grid grid-cols-1 gap-y-1" key={index}>
                    <Question param={item.question}/>
                    <Answer  param={item.answer}/>
                </div>
                ))}
            </div>
        </div>
    )
}