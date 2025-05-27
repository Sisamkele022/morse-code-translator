// src/components/MorseInput.jsx
import React from "react";

function MorseInput({ value, onChange }) {
  return (
    <textarea
      className="morse-input"
      value={value}
      onChange={(e) => onChange(e.target.value)}
      placeholder="Type text or morse code here..."
      rows={4}
    />
  );
}

export default MorseInput;
