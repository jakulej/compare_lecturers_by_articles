// import { useState } from 'react'
import './App.css'
import Header from "./Header"
import Footer from "./Footer"
import Main from "./Main"

function App() {
    // const [count, setCount] = useState(0)

    return (
        <div className="app">
            <Header/>
            <Main/>
            <Footer/>
        </div>
    )
}

export default App
