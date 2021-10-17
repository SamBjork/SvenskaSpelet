import React, { useEffect, useState } from "react";
import "../../App.css";
import QuestionService from "../QuestionService.js";

const API_URL = "http://127.0.0.1:5000/hello";

function Game() {
  const [questions, setQuestions] = useState([]);
  const [startGame, setStartGame] = useState(false);
  const [asweredCorrect, setAsweredCorrect] = useState(false);
  const [playerName, setPlayerName] = useState("");

  var player;

  useEffect(() => {
    fetch(API_URL)
      .then((res) => res.json())
      .then((data) => {
        setQuestions(data);
      });
  }, []);

  if (startGame) {
    return (
      <div className="background">
        {questions.length > 0 ? (
          <>
            <div className="welcome-container">
              <div className="bg-white text-blue-500 p-1 rounded-lg shadow-md">
                <label>Kör hårt, {playerName}!</label>
              </div>
            </div>
            <QuestionService data={questions[0]} />
          </>
        ) : (
          <div className="welcome-container-loading">
            <div className="welcome-text-loading">
              <h1>Vi håller på att ladda in frågan...</h1>
            </div>
          </div>
        )}
      </div>
    );
  }
  return (
    <div className="background">
      <label>Välkommen, Spelare!</label>
      <br />
      <input
        className="input"
        name="name"
        type="text"
        placeholder="Skriv in ditt namn..."
        onChange={(event) => setPlayerName(event.target.value)}
      />
      <br />
      <input
        className="input"
        type="submit"
        value="Starta!"
        onClick={() => setStartGame(true)}
      />
    </div>
  );
}
// useEffect(() => {
//     // GET request using fetch inside useEffect React hook
//     fetch('http://127.0.0.1:5000/game')
//         .then(response => response.json())
//         .then(data => setTotalReactPackages(data.total));

// // empty dependency array means this effect will only run once (like componentDidMount in classes)
// }, []);

// return (
//     <div className="background">
//         <div className="game-container">
//             <div className="question-container">
//             </div>
//             <div className="wrong-answer">
//             </div>
//             <div className="wrong-answer">
//             </div>
//             <div className="wrong-answer">
//             </div>
//             <div className="right-answer">
//                 <label htmlFor="right-answer"></label>
//             </div>
//         </div>

//     </div>
// )

export default Game;
