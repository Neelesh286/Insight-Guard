import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import ImageUploadComponent from './components/ImageUploadComponent.jsx'
import ImageProcessingComponent from './components/ImageProcessing.jsx'
import Navbar from './components/Navbar.jsx'
import Hero from './components/Hero.jsx'
import Analytics from './components/Analytics';
import Cards from './components/Cards';
import Newsletter from './components/Newsletter';
import Footer from './components/Footer.jsx'
import './index.css'

const BACKENDURL = 'http://127.0.0.1:8000'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App backendUrl={BACKENDURL}/>
    <Navbar />
    <Hero />
    <Analytics />
    <Cards />
    <ImageUploadComponent backendUrl={BACKENDURL}/>
    <ImageProcessingComponent backendUrl={BACKENDURL}/>
    <Newsletter />
    <Footer />
  </React.StrictMode>,
)
