import { Button } from "./PortfolioHero";
import { Title, SubTitle } from "./PortfolioAbout";
import { DataCard } from "./PortfolioProjects";
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


export default function Blogs() {
    return (
        <div>
            <Title name={"My posts"} />
            <div className="flex flex-wrap gap-5 justify-center">
                <DataCard title={'Post Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Updated: 6-12-2023'} />
                <DataCard title={'Post Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Updated: 6-12-2023'} />
                <DataCard title={'Post Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Updated: 6-12-2023'} />
                <DataCard title={'Post Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Updated: 6-12-2023'} />
                <DataCard title={'Post Title'}
                    body={"It is a long established fact\
                    that a reader will be distracted by \
                    the readable content of a page when \
                    looking at its layout."}
                    start={'Started: 6-12-2023'}
                    end={'Updated: 6-12-2023'} />
            </div>
        </div>
    )
}
