// import { useState } from 'react'
// import './App.css'
import NavBar from './PortMain/NavBar.jsx'
import Hero from './PortMain/Hero.jsx'
import Posts from './PortMain/Posts.jsx'
import Projects from './PortMain/Projects.jsx'
import About from './PortMain/About.jsx'
import Faq from './PortMain/Faq.jsx'
import Footer from './PortMain/Footer.jsx'


function App() {
  return (
    <>
      <div className='grid gap-2'>
        <NavBar />
        <div className='px-20 grid gap-36'>
          <Hero />
          <Posts />
          <Projects />
          <About />
          <Faq />
        </div>
        <Footer />
      </div>

    </>
  )
}

export default App
