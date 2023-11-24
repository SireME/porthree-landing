// import { useState } from 'react'
import './App.css'
import NavBar from './NavBar.jsx'
import Hero from './Hero.jsx'
import Posts from './Posts.jsx'
import Projects from './Projects.jsx'
import About from './About.jsx'
import Faq from './Faq.jsx'

function App() {
  return (
    <>
      <div className=''>
        <NavBar />
        <div className='px-20 grid gap-36'>
          <Hero />
          <Posts />
          <Projects />
          <About />
          <Faq />
        </div>
      </div>
    </>
  )
}

export default App
