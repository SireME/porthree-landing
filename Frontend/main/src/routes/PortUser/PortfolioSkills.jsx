import { Title, SubTitle } from "./PortfolioAbout";


function SkillCard({ icon, title, data }) {
    return (
        <div>
            <div className="flex gap-5">
                <div className="w-10 absolute h-10 border-2"></div>
                <div className="ml-14">
                    <SubTitle name={title} />
                    <p>{data}
                    </p>
                </div>
            </div>
        </div>
    )
}


export default function Skills() {
    return (
        <div>
            <Title name={"what i do"} />
            <div className="grid grid-cols-3 gap-5">
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
                <SkillCard title={'Skills title'} data={"Lorem ipsum dolor sit amet consectetur\
                    adipisicing elit. Est labore vero dicta excepturi\
                    sequi hic dignissimos, adipisci libero."} />
            </div>
        </div>
    )
}