import React from "react";

const QuestionService = ({
  text,
  wronganswer1,
  wronganswer2,
  wronganswer3,
  correctanswer,
}) => (
  <>
    <div className="bg-white text-purple-800 p-10 rounded-lg shadow-md">
      <h2 className="text-2xl">{text}</h2>
    </div>
    <div className="grid grid-cols-2 gap-6 mt-6">
      <button
        className="bg-white p-4 text-purple-800 font-semibold rounded shadow"
        onClick={(e) => console.log(e.target.value)}
      >
        {wronganswer1}
      </button>
      <button className="bg-white p-4 text-purple-800 font-semibold rounded shadow">
        {wronganswer2}
      </button>
      <button className="bg-white p-4 text-purple-800 font-semibold rounded shadow">
        {wronganswer3}
      </button>
      <button className="bg-white p-4 text-purple-800 font-semibold rounded shadow">
        {correctanswer}
      </button>
    </div>
  </>
);

export default QuestionService;
