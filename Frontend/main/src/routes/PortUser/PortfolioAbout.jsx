import React from "react";
import { Button } from "./PortfolioHero";


export function Title({ name }) {
    return (
        <div className="w-full text-center text-5xl font-bold mb-10 uppercase">
            <h2>{name}</h2>
        </div>
    )
}

export function SubTitle({ name }) {
    return (
        <div className="text-2xl font-medium mb-2 uppercase">
            <h2>{name}</h2>
        </div>
    )
}

function DataCard({ date, location, title, data }) {
    return (
        <div className="flex gap-5">
            <div>
                <p className="w-20 font-medium">{date}</p>
                <p className="font-bold text-l">{location}</p>
            </div>
            <div>
                <h4 className="font-bold text-xl border-t">{title}</h4>
                <p>{data}
                </p>
            </div>
        </div>
    )
}

function Education() {
    return (
        <div className="grid  gap-5">
            <SubTitle name={"Education"} />
            <DataCard date={"2023-2030"}
                location={'Cameroon'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
            <DataCard date={"2023-2030"}
                location={'Cameroon'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
            <DataCard date={"2023-2030"}
                location={'Cameroon'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
        </div>
    )
}

function Experience() {
    return (
        <div className="grid  gap-5">
            <SubTitle name={"Experience"} />
            <DataCard date={"2023-2030"}
                location={'Google'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
            <DataCard date={"2023-2030"}
                location={'Google'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
            <DataCard date={"2023-2030"}
                location={'Google'}
                title={'Barrow pushing'}
                data={"Lorem ipsum, dolor sit amet consectetur\
                adipisicing elit.Repudiandae iste facilis sit \
                dignissimos voluptatem nesciunt laudantium eligendi \
                quis at et."} />
        </div>
    )
}

function Expert() {
    return (
        <div>
            <SubTitle name={"EXPERT IN"} />
            <div className="mb-5">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Eius, quibusdam exercitationem? Magni sint delectus facilis,
                    dolore repudiandae harum vero modi.
                </p>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Eius, quibusdam exercitationem? Magni sint delectus facilis,
                    dolore repudiandae harum vero modi.
                </p>
            </div>
            <div>
                <Button value={"DOWNLOAD CV"} />
            </div>
        </div>
    )
}

function Who() {
    return (
        <div className="grid">
            <SubTitle name={"WHO AM I?"} />
            <div className="mb-5">
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Eius, quibusdam exercitationem? Magni sint delectus facilis,
                    dolore repudiandae harum vero modi.
                </p>
                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.
                    Eius, quibusdam exercitationem? Magni sint delectus facilis,
                    dolore repudiandae harum vero modi.
                </p>
            </div>
            <div>
                <Button value={"DOWNLOAD CV"} />
            </div>

        </div>
    )
}

export default function About() {
    return (
        <div className="grid gap-20">
            <Title name={"About Me"} />
            <div className="flex justify-center gap-10">
                <Who />
                <Expert />
            </div>
            <div className="flex justify-center gap-10">
                <Education />
                <Experience />
            </div>
        </div>
    )
}

