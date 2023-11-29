import NavBar from './PortUser/PortfolioNavbar'
import Hero from "./PortUser/PortfolioHero";
import About from "./PortUser/PortfolioAbout";
import Skills from "./PortUser/PortfolioSkills"
import Projects from "./PortUser/PortfolioProjects"
import Blogs from "./PortUser/PortfolioBlog"
import Contact from './PortUser/PortfolioContact';
import Footer from './PortMain/Footer';

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
                    <Contact />
                </section>
            </div>
                    <Footer />
        </div>
    )
}

export default Portfolio;
