// import { useState } from 'react'
import './App.css'
import NavBar from './NavBar.jsx'
import Hero from './Hero.jsx'
import Posts from './Posts.jsx'

function App() {
  return (
    <>
    <div className=''>
      <NavBar />
    <div className='px-20 grid gap-36'>
      <Hero />
      <Posts />
    </div>
    </div>
    </>
  )
}

export default App
