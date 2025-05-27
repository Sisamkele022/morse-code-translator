// src/components/ButtonGroup.jsx
import React from "react";

function ButtonGroup({ onEncode, onDecode }) {
  return (
    <div className="button-group">
      <button onClick={onEncode}>Encode</button>
      <button onClick={onDecode}>Decode</button>
    </div>
  );
}

export default ButtonGroup;
