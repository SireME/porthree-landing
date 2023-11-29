import NavBar from './PortUser/PorfolioNavbar'
import Hero from "./PortUser/PortfolioHero";
import About from "./PortUser/PortfolioAbout";
import Skills from "./PortUser/PortfolioSkills"
import Projects from "./PortUser/PortfolioProjects"
import Blogs from "./PortUser/PortfolioBlog"
function Portfolio() {
    return (
        <div>
            <NavBar />
            <div className="px-20">
                <Hero />
                <section className='grid grid-cols-1 gap-20 py-20'>
                    <About />
                    <Skills />
                    <Projects />
                    <Blogs />
                </section>
            </div>
        </div>
    )
}

export default Portfolio;
