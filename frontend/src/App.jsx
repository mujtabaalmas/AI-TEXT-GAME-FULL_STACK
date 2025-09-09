import './App.css'
import {BrowserRouter as Router, Routes, Route} from "react-router-dom"
import StoryLoader from "./components/StoryLoader"
import StoryGenerator from "./components/StoryGenerator.jsx";

function App() {
  return (
    <Router>
      <div className="app-container">
        <header>
          <h1>AI TEXT BASED STORY GAME</h1>
        </header>
        <main>
          <Routes>
            <Route path={"/story/:id"} element={<StoryLoader />} />
            <Route path={"/"} element={<StoryGenerator />}/>
          </Routes>
          
        </main>
       
      </div>
      <div className='footer'> Created by Mujtaba Almas 2025 All rights Revserved</div>
    </Router>
  )
}

export default App