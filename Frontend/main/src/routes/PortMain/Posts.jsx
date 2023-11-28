
export default function Posts() {
    return (
        <div className='grid grid-cols-1 gap-20'>
            <div className='text-center font-black text-5xl'><h1>Posts</h1></div>
            <div className='grid grid-cols-4 justify-between gap-y-10'>

                <div className='border-2 rounded-lg p-3 w-80 grid justify-center grid-cols-1 gap-3'>
                    <div className="w-72 bg-blue h-40 border rounded"></div>
                    <div className="grid gri-cols-1 justify-center gap-y-5 mt-5">
                        <div className="">
                            <h3 className="text-center font-bold text-xl">This is a posts title</h3>
                        </div>
                        <div className="grid grid-cols-3 gap-y-5 -gap-x-10 justify-middle">
                            <div className="bg-blue rounded-3xl w-10 h-10 row-span-3"></div>
                            <div className="-ml-12">Anadu Godwin</div>
                            <div className="font-medium text-sm ">12th sept 22</div>
                            <div className="-ml-12">Software Engineer</div>
                            <div className="">
                                <select name="tags" id="tags" className='border outline-0 max-h-6 text-center rounded-lg w-24'>
                                    <option value="volvo">post tags</option>
                                    <option value="saab">developer</option>
                                    <option value="mercedes">software Engineer</option>
                                    <option value="audi">Video editor</option>
                                </select>
                            </div>
                        </div>
                        <div className="text-center font-bold">
                            <a href="" className="border px-7">Read...</a>
                        </div>
                    </div>
                </div>

                <div className='border-2 rounded-lg p-3 w-80 grid justify-center grid-cols-1 gap-3'>
                    <div className="w-72 bg-blue h-40 border rounded"></div>
                    <div className="grid gri-cols-1 justify-center gap-y-5 mt-5">
                        <div className="">
                            <h3 className="text-center font-bold text-xl">This is a posts title</h3>
                        </div>
                        <div className="grid grid-cols-3 gap-y-5 -gap-x-10 justify-middle">
                            <div className="bg-blue rounded-3xl w-10 h-10 row-span-3"></div>
                            <div className="-ml-12">Anadu Godwin</div>
                            <div className="font-medium text-sm ">12th sept 22</div>
                            <div className="-ml-12">Software Engineer</div>
                            <div className="">
                                <select name="tags" id="tags" className='border outline-0 max-h-6 text-center rounded-lg w-24'>
                                    <option value="volvo">post tags</option>
                                    <option value="saab">developer</option>
                                    <option value="mercedes">software Engineer</option>
                                    <option value="audi">Video editor</option>
                                </select>
                            </div>
                        </div>
                        <div className="text-center font-bold">
                            <a href="" className="border px-7">Read...</a>
                        </div>
                    </div>
                </div>

                <div className='border-2 rounded-lg p-3 w-80 grid justify-center grid-cols-1 gap-3'>
                    <div className="w-72 bg-blue h-40 border rounded"></div>
                    <div className="grid gri-cols-1 justify-center gap-y-5 mt-5">
                        <div className="">
                            <h3 className="text-center font-bold text-xl">This is a posts title</h3>
                        </div>
                        <div className="grid grid-cols-3 gap-y-5 -gap-x-10 justify-middle">
                            <div className="bg-blue rounded-3xl w-10 h-10 row-span-3"></div>
                            <div className="-ml-12">Anadu Godwin</div>
                            <div className="font-medium text-sm ">12th sept 22</div>
                            <div className="-ml-12">Software Engineer</div>
                            <div className="">
                                <select name="tags" id="tags" className='border outline-0 max-h-6 text-center rounded-lg w-24'>
                                    <option value="volvo">post tags</option>
                                    <option value="saab">developer</option>
                                    <option value="mercedes">software Engineer</option>
                                    <option value="audi">Video editor</option>
                                </select>
                            </div>
                        </div>
                        <div className="text-center font-bold">
                            <a href="" className="border px-7">Read...</a>
                        </div>
                    </div>
                </div>

                <div className='border-2 rounded-lg p-3 w-80 grid justify-center grid-cols-1 gap-3'>
                    <div className="w-72 bg-blue h-40 border rounded"></div>
                    <div className="grid gri-cols-1 justify-center gap-y-5 mt-5">
                        <div className="">
                            <h3 className="text-center font-bold text-xl">This is a posts title</h3>
                        </div>
                        <div className="grid grid-cols-3 gap-y-5 -gap-x-10 justify-middle">
                            <div className="bg-blue rounded-3xl w-10 h-10 row-span-3"></div>
                            <div className="-ml-12">Anadu Godwin</div>
                            <div className="font-medium text-sm ">12th sept 22</div>
                            <div className="-ml-12">Software Engineer</div>
                            <div className="">
                                <select name="tags" id="tags" className='border outline-0 max-h-6 text-center rounded-lg w-24'>
                                    <option value="volvo">post tags</option>
                                    <option value="saab">developer</option>
                                    <option value="mercedes">software Engineer</option>
                                    <option value="audi">Video editor</option>
                                </select>
                            </div>
                        </div>
                        <div className="text-center font-bold">
                            <a href="" className="border px-7">Read...</a>
                        </div>
                    </div>
                </div>

                <div className="">
                    <button className='border-2 rounded px-2 font-bold'>More Posts...</button>
                </div>
            </div>
        </div>
    )
}
