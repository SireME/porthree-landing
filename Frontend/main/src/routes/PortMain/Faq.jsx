export default function Faq() {
    return (
        <div className='grid grid-cols-1 gap-20 px-20'>
            <div className='text-center font-black text-5xl'><h1>Frequently Asked Questions <br /> (FAQ)</h1></div>
            <div className="w-full grid gap-4 justify-center">
                <div className="grid grid-cols-1 gap-y-1">
                    <div className="border-2 rounded p-2 w-3/4 text-center justify-self-center"><p>This should be a question?</p></div>
                    <div className="border rounded p-2 w-3/4 justify-self-center"><p>And here should contain the answer to the questions though this should
                        be a drop down but the MVP isn't going to be too fancy yet!</p></div>
                </div>
                <div className="grid grid-cols-1 gap-y-1">
                    <div className="border-2 rounded p-2 w-3/4 text-center justify-self-center"><p>This should be a question?</p></div>
                    <div className="border rounded p-2 w-3/4 justify-self-center"><p>And here should contain the answer to the questions though this should
                        be a drop down but the MVP isn't going to be too fancy yet!</p></div>
                </div>
                <div className="grid grid-cols-1 gap-y-1">
                    <div className="border-2 rounded p-2 w-3/4 text-center justify-self-center"><p>This should be a question?</p></div>
                    <div className="border rounded p-2 w-3/4 justify-self-center"><p>And here should contain the answer to the questions though this should
                        be a drop down but the MVP isn't going to be too fancy yet!</p></div>
                </div>
            </div>
        </div>
    )
}