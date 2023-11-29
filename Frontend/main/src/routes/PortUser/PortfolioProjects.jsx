import { Button } from "./PortfolioHero";
import { Title, SubTitle } from "./PortfolioAbout";

export function Select() {
    return (
        <>
            <select name="tags" id="tags" className='border outline-0 max-w-min text-center w-fit'>
                <option value="volvo">Tools</option>
                <option value="saab">developer</option>
                <option value="mercedes">software Engineer</option>
                <option value="audi">Video editor</option>
            </select>
        </>
    )
}

export function DataCard({ title, body, start, end }) {
    return (
        <div className="p-5 border flex flex-col justify-center gap-5 max-w-sm">
            <div className="w-full h-40 border"></div>
            <div><p className="text-center font-bold text-xl">{title}</p></div>
            <div><p>{body}</p></div>
            <div className="flex justify-between">
                <span className="font-medium text-sm">
                    <p>{start}</p>
                    <p>{end}</p>
                </span>
                <Select />
            </div>
            <div><Button value={"Explore"} /></div>
        </div>
    )
}


export default function Projects() {
    return (
        <div>
            <Title name={"awesome works"} />
            <div className="flex flex-wrap gap-5 justify-center">
                <DataCard title={'Project Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Ended: in progress...'} />
                <DataCard title={'Project Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Ended: in progress...'} />
                <DataCard title={'Project Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Ended: in progress...'} />
                <DataCard title={'Project Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Ended: in progress...'} />
            </div>
        </div>
    )
}
