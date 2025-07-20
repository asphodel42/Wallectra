import "./App.css";
import { useState } from "react";
import Header from "./components/Header.jsx";

function App() {
  const [loggedIn, setLoggedIn] = useState(true);
  return (
    <>
      <Header loggedIn={loggedIn} />
      <main></main>
    </>
  );
}

export default App;
