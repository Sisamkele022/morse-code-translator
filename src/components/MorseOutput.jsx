// src/components/MorseOutput.jsx
import React from "react";

function MorseOutput({ value }) {
  return (
    <div className="morse-output">
      <h2>Output:</h2>
      <pre>{value}</pre>
    </div>
  );
}

export default MorseOutput;
