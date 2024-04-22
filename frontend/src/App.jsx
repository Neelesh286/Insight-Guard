import { useState, useEffect } from 'react';
import axios from 'axios'
// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'
import './App.css'
import Navbar from './components/Navbar';
import {createBrowserRouter, RouterProvider} from 'react-router-dom'
import AboutPage from './components/AboutPage';
import Hero from './components/Hero';


function App({backendUrl}) {
  const router = createBrowserRouter([
    {
      path:"/",
      element: <Hero/>
    },
    {
      path:"/about",
      element: <AboutPage/>
    }
  ])

  const [message, setMessage] = useState('')

  useEffect(()=>{
    axios.get(`${backendUrl}/api/hello-world`)
    .then(response=>{
      setMessage(response.data.message)
    })
    .catch(error=>{
      console.log(error)
    })
  },[])

  
  return(
    <>
      <h1>Hello World From React ⚛️</h1>
      <p>{message} From Django ⚒️</p>
      <Navbar />
      <RouterProvider router={router}/>
    </>
  )
}

export default App
