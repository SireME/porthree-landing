// import { useState } from 'react'
import './App.css'
import NavBar from './NavBar.jsx'
import Hero from './Hero.jsx'
import Posts from './Posts.jsx'
import Projects from './Projects.jsx'
import About from './About.jsx'
import Faq from './Faq.jsx'
import Footer from './Footer.jsx'

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
