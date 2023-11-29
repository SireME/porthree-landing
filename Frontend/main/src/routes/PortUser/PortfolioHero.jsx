import React from "react";

function Button({ action, value }) {
    return (
        <button onClick={action} className=" border px-2 font-bold w-fit">{value}</button>
    );
}

function Tool(name) {
    return(
        <div className="grid w-full justify-center">
                <div className="border rounded-full  w-10 h-10 justify-self-center"></div>
                <div><p className="font-medium">Tool name</p></div>
            </div>
    )
}

function HeroTools() {
    return (
        <div className="flex py-1 overflow-x-scroll ">
            <Tool/>
            <Tool/>
            <Tool/>
            <Tool/>
            <Tool/>
            <Tool/>
        </div>
    );
}

function Hero() {
    return (
        <>
            <div className="flex justify-between h-auto items-center pt-40 pb-20 border-b-4">
                <div className="w-3/5 grid grid-cols-1 gap-10">
                    <div><p className="font-bold">Software Engineer</p></div>
                    <div><p className="font-bold text-5xl">Anadu Godwin</p></div>
                    <div><p className="font-medium">It is a long established fact that a
                        reader will be distracted by the readable
                        content of a page when looking at its
                        layout. The point of using Lorem Ipsum is
                        that it has a more-or-less normal distribution of
                        letters, as opposed to using 'Content here, content
                        here', making it look like readable English.</p></div>
                    <div><Button value={'Know More...'} /></div>
                </div>
                <div>
                    <div className="font-black text-9xl">AG</div>
                </div>
            </div>
            <p></p>
            <HeroTools />
        </>
    );
}

export { Button };
export default Hero;