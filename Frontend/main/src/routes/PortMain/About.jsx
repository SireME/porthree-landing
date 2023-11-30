import React, { useEffect, useState } from "react";
import axios from "axios";


export function Get({ url }) {
    const [data, setData] = useState(null);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await axios.get(url);
                setData(response.data);
            } catch (error) {
                setError(error.message)
            }
        };
        fetchData();
    }, [url]);
    if (error || !data) {
        return null;
    }
    return data;
}

export default function About() {
    const url = 'http://127.0.0.1:8000/api/PothreeAbout/';
    const data = Get({ url });
    if (!data) {
        return 'nothing';
    }
    return (
        <div className='grid grid-cols-1 gap-20'>
            <div className='text-center font-black text-5xl'><h1>About</h1></div>
            <div className='grid grid-cols-2 justify-center gap-20 h-96'>
                <div className="border-4 w-full h-full rounded-xl" style={{ backgroundImage: `url(${data[0].image})` }}></div>
                <div className="grid grid-cols-1 py-10">
                    <div className="text-center font-bold text-2xl">About Porthree</div>
                    <div>
                        <p>{data[0].about}</p>
                    </div>
                    <div><button className="border px-2 font-bold">Read More...</button></div>
                </div>
            </div>
        </div>
    )
}
